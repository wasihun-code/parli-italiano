import { 
  PathGenerationInput, 
  PathGenerationResult, 
  LearningStep
} from '../types/learningPath';

/**
 * LearningPathGenerator
 * 
 * A pure function engine that transforms scenario data and user state 
 * into a deterministic sequence of exercises.
 */
export class LearningPathGenerator {

  /**
   * Generates a learning path based on scenario content and global mastery.
   */
  static generatePath(input: PathGenerationInput): PathGenerationResult {
    const { scenarioId, scenarioData, globalMastery, reviewQueue } = input;
    
    // 1. Build Chronology Index
    const chronology = this.buildChronologyIndex(scenarioData);
    
    // 2. Combine and Sort All Items by Chronology
    const allItems = [
      ...scenarioData.vocabulary.map(v => ({ ...v, itemType: 'vocabulary' as const })),
      ...scenarioData.phrases.map(p => ({ ...p, itemType: 'phrase' as const })),
      ...scenarioData.sentences.map(s => ({ ...s, itemType: 'sentence' as const }))
    ].sort((a, b) => 
      (chronology.get(a.id) ?? 9999) - (chronology.get(b.id) ?? 9999)
    );

    // 3. Separate Review items from New items
    const reviewItems = allItems.filter(item => reviewQueue.includes(item.id));
    const newItems = allItems.filter(item => !reviewQueue.includes(item.id));

    // 4. Adaptation: Determine global mastery percent
    const masteryCount = Object.values(globalMastery).filter(v => v >= 0.8).length;
    const masteryPercent = allItems.length > 0 ? (masteryCount / allItems.length) * 100 : 0;
    
    const steps: LearningStep[] = [];

    // 5. Sequence Generation - REVIEWS FIRST
    for (const item of reviewItems) {
      const mastery = globalMastery[item.id] ?? 0;
      steps.push(...this.getItemSteps(item, mastery, masteryPercent, true));
    }

    // 6. Sequence Generation - NEW ITEMS SECOND
    for (const item of newItems) {
      const mastery = globalMastery[item.id] ?? 0;
      steps.push(...this.getItemSteps(item, mastery, masteryPercent, false));
    }

    // 5. Add Conversation Steps at the end
    for (const conv of scenarioData.scriptedConversations) {
      steps.push({
        id: `${conv.id}-conversation`,
        itemId: conv.id,
        type: 'conversation',
        exerciseType: 'Conversation',
        masteryContribution: 1.0
      });
    }


    const finalSteps = this.applyAdaptationFinal(steps, masteryPercent);

    return {
      path: { scenarioId, steps: finalSteps },
      stats: {
        totalSteps: finalSteps.length,
        recognitionCount: finalSteps.filter(s => ['Listen', 'ListenChoose', 'Match', 'Reading'].includes(s.exerciseType)).length,
        recallCount: finalSteps.filter(s => ['BuildSentence', 'Recall', 'Assembly'].includes(s.exerciseType)).length,
        productionCount: finalSteps.filter(s => ['Dictation', 'Speaking', 'Spelling'].includes(s.exerciseType)).length
      }
    };
  }

  private static getItemSteps(item: any, mastery: number, masteryPercent: number, isReview: boolean): LearningStep[] {
    let steps: LearningStep[] = [];
    
    if (item.itemType === 'vocabulary') {
      steps = this.getVocabSteps(item.id, mastery, masteryPercent);
    } else if (item.itemType === 'phrase') {
      steps = this.getPhraseSteps(item.id, mastery, masteryPercent);
    } else if (item.itemType === 'sentence') {
      steps = this.getSentenceSteps(item.id, mastery, masteryPercent);
    }

    if (isReview) {
      // Mark as review type if it's the specific review exercise, 
      // but usually we just reuse the production checks for review.
      // Rule 4: Review items must not bypass mastery logic.
      // If an item is in review queue but has low mastery, it follows full flow.
      // If it has high mastery, it follows shortened flow.
    }

    return steps;
  }

  private static buildChronologyIndex(data: any): Map<string, number> {
    const index = new Map<string, number>();
    let counter = 0;

    if (!data.scriptedConversations) return index;

    for (const conv of data.scriptedConversations) {
      for (const msg of conv.messages) {
        // Host Messages -> Sentences/Vocabulary
        this.indexText(msg.text, data, index, counter++);
        // Choices -> Phrases/Vocabulary
        if (msg.choices) {
          for (const choice of msg.choices) {
            if (choice.isCorrect) {
              this.indexText(choice.text, data, index, counter++);
            }
          }
        }
      }
    }
    return index;
  }

  private static indexText(text: string, data: any, index: Map<string, number>, position: number) {
    const lowerText = text.toLowerCase();
    
    // Check Sentences
    for (const s of data.sentences) {
      if (!index.has(s.id) && text.includes(s.italian)) {
        index.set(s.id, position);
      }
    }

    // Check Phrases
    for (const p of data.phrases) {
      if (!index.has(p.id) && text.includes(p.italian)) {
        index.set(p.id, position);
      }
    }

    // Check Vocab
    const tokens = lowerText.split(/[\s,.'!?]+/);
    for (const v of data.vocabulary) {
      if (!index.has(v.id) && tokens.includes(v.italian.toLowerCase())) {
        index.set(v.id, position);
      }
    }
  }

  private static getVocabSteps(id: string, mastery: number, globalMasteryPercent: number): LearningStep[] {
    if (mastery >= 0.8) {
      return [
        { id: `${id}-spelling`, itemId: id, type: 'vocabulary', exerciseType: 'Spelling', masteryContribution: 0.8 },
        { id: `${id}-speaking`, itemId: id, type: 'vocabulary', exerciseType: 'Speaking', masteryContribution: 1.0 }
      ];
    }

    const steps: LearningStep[] = [
      { id: `${id}-listen`, itemId: id, type: 'vocabulary', exerciseType: 'Listen', masteryContribution: 0.1 },
      { id: `${id}-listenchoose`, itemId: id, type: 'vocabulary', exerciseType: 'ListenChoose', masteryContribution: 0.2 },
      { id: `${id}-match`, itemId: id, type: 'vocabulary', exerciseType: 'Match', masteryContribution: 0.2 },
      { id: `${id}-build`, itemId: id, type: 'vocabulary', exerciseType: 'BuildSentence', masteryContribution: 0.4 },
      { id: `${id}-recall`, itemId: id, type: 'vocabulary', exerciseType: 'Recall', masteryContribution: 0.4 },
      { id: `${id}-spelling`, itemId: id, type: 'vocabulary', exerciseType: 'Spelling', masteryContribution: 0.8 },
      { id: `${id}-speaking`, itemId: id, type: 'vocabulary', exerciseType: 'Speaking', masteryContribution: 1.0 }
    ];

    // 25% Mastery: Accelerated Recall
    if (globalMasteryPercent >= 25 && mastery > 0.4) {
        return steps.filter(s => !['ListenChoose'].includes(s.exerciseType));
    }

    return steps;
  }

  private static getPhraseSteps(id: string, mastery: number, _globalMasteryPercent: number): LearningStep[] {
    if (mastery >= 0.8) {
        return [
          { id: `${id}-spelling`, itemId: id, type: 'phrase', exerciseType: 'Spelling', masteryContribution: 1.0 }
        ];
    }
    return [
      { id: `${id}-listen`, itemId: id, type: 'phrase', exerciseType: 'Listen', masteryContribution: 0.2 },
      { id: `${id}-match`, itemId: id, type: 'phrase', exerciseType: 'Match', masteryContribution: 0.4 },
      { id: `${id}-spelling`, itemId: id, type: 'phrase', exerciseType: 'Spelling', masteryContribution: 1.0 }
    ];
  }

  private static getSentenceSteps(id: string, mastery: number, _globalMasteryPercent: number): LearningStep[] {
    if (mastery >= 0.8) {
        return [
          { id: `${id}-spelling`, itemId: id, type: 'sentence', exerciseType: 'Spelling', masteryContribution: 1.0 }
        ];
    }
    return [
      { id: `${id}-listen`, itemId: id, type: 'sentence', exerciseType: 'Listen', masteryContribution: 0.2 },
      { id: `${id}-match`, itemId: id, type: 'sentence', exerciseType: 'Match', masteryContribution: 0.4 },
      { id: `${id}-spelling`, itemId: id, type: 'sentence', exerciseType: 'Spelling', masteryContribution: 1.0 }
    ];
  }

  private static applyAdaptationFinal(steps: LearningStep[], masteryPercent: number): LearningStep[] {
    if (masteryPercent >= 100) {
      // Conversation-Only path. But we keep Production checks on a small sample of items as specified.
      // Actually, let's just return conversation steps + production steps for items.
      return steps.filter(s => s.exerciseType === 'Conversation' || ['Dictation', 'Speaking'].includes(s.exerciseType));
    }
    
    // Additional adaptation filters can go here (e.g., safety floor)
    return steps;
  }
}
