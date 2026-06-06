import { GlobalProgressService, MasteryState } from './globalProgressService';
import { db } from '../lib/db';

const REINFORCEMENT_BUDGET_CAP = 20;

const PRIORITY_SCORES: Record<MasteryState, number> = {
  'LAPSED': 100,
  'RELEARNING': 90,
  'UNKNOWN': 80,
  'LEARNING': 70,
  'LEARNED': 40,
  'ADVANCED': 20,
  'MASTERED': 10
};

// Tokenizer matching the python linguistic_extractor
function tokenize(text: string): string[] {
  const lower = text.toLowerCase();
  const noPunct = lower.replace(/[.,!?;:""“”«»()[\]{}]/g, "");
  return noPunct.split(/\s+/).filter(w => w.length > 0 && isNaN(Number(w)));
}

export class ConversationReinforcementService {
  /**
   * Processes a completed conversation and awards bounded implicit mastery credit.
   */
  static async reinforceConversation(
    scenarioId: number, 
    mistakes: number,
    conversationText: string
  ): Promise<number> {
    
    // 1. Tokenize conversation text to find Active Vocabulary
    const encounteredTokensArray = tokenize(conversationText);
    const encounteredTokens = new Set(encounteredTokensArray);
    
    // Calculate token frequencies for tie-breaking
    const tokenFrequency: Record<string, number> = {};
    for (const t of encounteredTokensArray) {
      tokenFrequency[t] = (tokenFrequency[t] || 0) + 1;
    }

    // 2. Fetch scenario mapped global IDs
    let globalIds: string[] = [];
    try {
      const mappings = await db.scenario_vocab_mapping_cache
        .where({ scenario_id: scenarioId })
        .toArray();
      
      if (mappings.length > 0) {
        globalIds = mappings.map(m => m.global_dict_id);
      } else {
        // Prototype Fallback
        const res = await fetch('/scenario_vocab_mapping.json');
        if (res.ok) {
          const data = await res.json();
          const scenario = await db.scenarios.get(scenarioId);
          if (scenario) {
            const slugKey = Object.keys(data).find(k => k.includes(scenario.category) && k.includes(scenario.title.toLowerCase().replace(/[^a-z0-9]/g, '_')));
            if (slugKey && data[slugKey]) {
              globalIds = data[slugKey].map((m: any) => m.global_id);
            }
          }
        }
      }
    } catch (e) {
      console.warn("Failed to fetch mappings", e);
      return 0;
    }

    // 3. Filter down to ONLY actually encountered vocabulary
    const activeGlobalIds: string[] = [];
    const entries = await db.global_dictionary.bulkGet(globalIds);
    
    for (let i = 0; i < globalIds.length; i++) {
      const entry = entries[i];
      if (entry) {
        const itemTokens = tokenize(entry.italian);
        const isEncountered = itemTokens.length > 0 && itemTokens.every(t => encounteredTokens.has(t));
        if (isEncountered) {
          activeGlobalIds.push(globalIds[i]);
        }
      }
    }

    if (activeGlobalIds.length === 0) return 0;

    // 4. Priority Scoring & Sorting
    const progressRecords = await db.global_progress.bulkGet(activeGlobalIds);
    const scoredItems = activeGlobalIds.map((gid, index) => {
      const progress = progressRecords[index];
      const entry = entries.find(e => e?.id === gid);
      
      // Derive mastery state
      let state: MasteryState = 'UNKNOWN';
      if (progress) {
        if (progress.mastery_level >= 4) state = 'MASTERED';
        else if (progress.mastery_level === 3) state = 'ADVANCED';
        else if (progress.mastery_level >= 1) state = 'LEARNED';
        else if (progress.correct_streak === 0 && progress.total_attempts > 0) state = 'LAPSED';
        else state = 'LEARNING';
      }

      let score = PRIORITY_SCORES[state];
      
      // Frequency bonus (up to +4 points)
      if (entry) {
        const freq = tokenFrequency[tokenize(entry.italian)[0]] || 1;
        score += Math.min(4, freq);
      }
      
      return { gid, score, state };
    });

    scoredItems.sort((a, b) => b.score - a.score);

    // 5. Apply Budget Cap
    const budgetedItems = scoredItems.slice(0, REINFORCEMENT_BUDGET_CAP);

    // 6. Award Reinforcement
    const isPerfect = mistakes === 0;
    const isGood = mistakes > 0 && mistakes <= 2;
    const isSuccess = isPerfect || isGood;

    const itemsToUpdate = budgetedItems
      .filter(item => ['LEARNED', 'ADVANCED', 'MASTERED', 'LAPSED', 'RELEARNING'].includes(item.state))
      .map(item => ({ globalId: item.gid, isCorrect: isSuccess }));

    if (itemsToUpdate.length > 0) {
      await GlobalProgressService.recordBatchResults(itemsToUpdate, scenarioId, 'CONVERSATION');
    }

    return isSuccess ? itemsToUpdate.length : 0;
  }
}
