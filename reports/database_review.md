# Database Review - Phase 7.7

## Bounded Reinforcement Implementation Proposal

As the Database/Backend Agent, I propose the following implementation for `src/services/conversationReinforcementService.ts`. This implementation satisfies the Phase 7.7 requirements for bounded reinforcement, priority-based sorting, and token-based intersection.

### Proposed Implementation: `src/services/conversationReinforcementService.ts`

```typescript
import { db } from '../lib/db';
import { GlobalProgressService, MasteryState } from './globalProgressService';
import { normalizeString } from '../utils/string';

export class ConversationReinforcementService {
  private static readonly G_MAX = 20; // Budget cap as requested

  private static readonly PRIORITY_SCORES: Record<MasteryState, number> = {
    'UNKNOWN': 100,
    'LEARNING': 90,
    'LAPSED': 80,
    'RELEARNING': 70,
    'LEARNED': 40,
    'ADVANCED': 20,
    'MASTERED': 10
  };

  /**
   * Processes a completed conversation and awards implicit mastery credit
   * to a bounded set of vocabulary items based on priority.
   */
  static async reinforceConversation(
    scenarioId: number,
    conversationText: string
  ): Promise<number> {
    // 1. Extract tokens and calculate frequencies
    const normalizedFullText = normalizeString(conversationText);
    const tokens = normalizedFullText.split(/\s+/).filter(t => t.length > 0);
    const tokenFrequencies = new Map<string, number>();
    tokens.forEach(token => {
      tokenFrequencies.set(token, (tokenFrequencies.get(token) || 0) + 1);
    });

    // 2. Intersect with the scenario's mapped global vocabulary
    const mappings = await db.scenario_vocab_mapping_cache
      .where('scenario_id')
      .equals(scenarioId)
      .toArray();
    
    const candidateIds = mappings.map(m => m.global_dict_id);
    const entries = await db.global_dictionary
      .where('id')
      .anyOf(candidateIds)
      .toArray();

    // 3. Filter and gather metrics for prioritization
    const now = new Date();
    const scoredItems = await Promise.all(
      entries
        .filter(entry => {
          const normalizedEntry = normalizeString(entry.italian);
          // Check if the word or phrase appears in the conversation
          return normalizedFullText.includes(normalizedEntry);
        })
        .map(async entry => {
          const state = await GlobalProgressService.getMasteryState(entry.id);
          const progress = await db.global_progress.get(entry.id);
          
          const normalizedEntry = normalizeString(entry.italian);
          const frequency = tokenFrequencies.get(normalizedEntry) || 1; // Fallback to 1 for phrases
          const isDue = progress ? new Date(progress.next_review_at) <= now : true;

          return {
            id: entry.id,
            italian: entry.italian,
            score: this.PRIORITY_SCORES[state] || 0,
            isDue: isDue,
            frequency: frequency,
            length: entry.italian.length
          };
        })
    );

    // 4. Sort by priority and tie-breakers
    // Priority: Score (desc) > Due Status (desc) > Frequency (desc) > Length (desc)
    scoredItems.sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      if (a.isDue !== b.isDue) return a.isDue ? -1 : 1;
      if (b.frequency !== a.frequency) return b.frequency - a.frequency;
      return b.length - a.length;
    });

    // 5. Apply the 20-word budget cap
    const selectedItems = scoredItems.slice(0, this.G_MAX);

    // 6. Trigger updates
    let reinforcedCount = 0;
    for (const item of selectedItems) {
      // Award implicit credit (treated as success)
      await GlobalProgressService.recordAnswer(item.id, true, scenarioId, 'CONVERSATION');
      reinforcedCount++;
    }

    return reinforcedCount;
  }
}
```

### Explanation of the Implementation

1.  **Token Extraction:** The service uses `normalizeString` to strip punctuation and normalize case/accents from the entire conversation block. It then calculates frequencies for tie-breaking.
2.  **Mapping Intersection:** It retrieves the explicit scenario-to-global mappings and then performs a sub-string match against the normalized conversation text. This ensures we only reinforce words that were actually present in the dialogue.
3.  **Mastery Querying:** It leverages `GlobalProgressService.getMasteryState` to determine the current pedagogical status of each item.
4.  **Priority Sorting:** It implements the scoring table from the design document, prioritizing `UNKNOWN` and `LEARNING` words to ensure they enter the SRS loop. Tie-breakers favor items that are currently due, appear frequently in the text, or are longer (higher cognitive load).
5.  **Bounded Budget:** It enforces the requested 20-word cap, preventing a single conversation from prematurely "mastering" an entire vocabulary set.
6.  **Updates:** Selected items are updated via `GlobalProgressService.recordAnswer`, which handles both history logging and SRS state transitions with the `CONVERSATION` source.
