import Dexie, { type EntityTable } from 'dexie';
import { foundationLessons } from '@shared/data/foundations';
import { scenarios } from '@shared/data/scenarios';

// Schema definitions matching src/db/schema.ts as closely as possible in Dexie
export interface AppMetadata {
  key: string;
  value: string;
  updated_at: string;
}

export interface FoundationLesson {
  id: number;
  title: string;
  description: string;
  pass_score: number;
  sort_order: number;
}

export interface FoundationTerm {
  id: string;
  lesson_id: number;
  italian: string;
  english: string;
  note?: string;
  sort_order: number;
}

export interface FoundationExercise {
  id: string;
  lesson_id: number;
  kind: string;
  prompt: string;
  answer: string;
  options_json?: string;
  sort_order: number;
}

export interface Scenario {
  id: number;
  category: string;
  title: string;
  description: string;
  sort_order: number;
}

export interface ScenarioVocabulary {
  id: string;
  scenario_id: number;
  italian: string;
  english: string;
  correct_streak_required: number;
  sort_order: number;
}

export interface ScenarioPhrase {
  id: string;
  scenario_id: number;
  italian: string;
  english: string;
  pass_score: number;
  sort_order: number;
}

export interface ScenarioSentence {
  id: string;
  scenario_id: number;
  italian: string;
  english: string;
  grammar_point: string;
  pass_score: number;
  sort_order: number;
}

export interface SrsItem {
  item_id: string;
  item_type: 'foundation' | 'vocabulary' | 'phrase' | 'sentence';
  scenario_id?: number;
  foundation_lesson_id?: number;
  italian: string;
  english: string;
  correct_streak: number;
  attempts: number;
  correct_attempts: number;
  due_at: string;
  last_reviewed_at?: string;
}

class ParlaItalianoDatabase extends Dexie {
  app_metadata!: EntityTable<AppMetadata, 'key'>;
  foundation_lessons!: EntityTable<FoundationLesson, 'id'>;
  foundation_terms!: EntityTable<FoundationTerm, 'id'>;
  foundation_exercises!: EntityTable<FoundationExercise, 'id'>;
  scenarios!: EntityTable<Scenario, 'id'>;
  scenario_vocabulary!: EntityTable<ScenarioVocabulary, 'id'>;
  scenario_phrases!: EntityTable<ScenarioPhrase, 'id'>;
  scenario_sentences!: EntityTable<ScenarioSentence, 'id'>;
  srs_items!: EntityTable<SrsItem, 'item_id'>;

  constructor() {
    super('ParlaItalianoDB');
    this.version(1).stores({
      app_metadata: 'key',
      foundation_lessons: 'id, sort_order',
      foundation_terms: 'id, lesson_id, sort_order',
      foundation_exercises: 'id, lesson_id, sort_order',
      scenarios: 'id, category, sort_order',
      scenario_vocabulary: 'id, scenario_id, sort_order',
      scenario_phrases: 'id, scenario_id, sort_order',
      scenario_sentences: 'id, scenario_id, sort_order',
      srs_items: 'item_id, item_type, scenario_id, foundation_lesson_id, due_at',
    });
  }
}

export const db = new ParlaItalianoDatabase();

export async function setupDatabase() {
  const count = await db.app_metadata.count();
  if (count === 0) {
    await seedDatabase();
  }
  return db;
}

async function seedDatabase() {
  await db.transaction('rw', [
    db.app_metadata,
    db.foundation_lessons,
    db.foundation_terms,
    db.foundation_exercises,
    db.scenarios,
    db.scenario_vocabulary,
    db.scenario_phrases,
    db.scenario_sentences,
    db.srs_items,
  ], async () => {
    // Seed Foundation Lessons
    for (const [index, lesson] of foundationLessons.entries()) {
      await db.foundation_lessons.put({
        id: lesson.id,
        title: lesson.title,
        description: lesson.description,
        pass_score: 90,
        sort_order: index + 1,
      });

      for (const [tIndex, term] of lesson.terms.entries()) {
        await db.foundation_terms.put({
          id: term.id,
          lesson_id: lesson.id,
          italian: term.italian,
          english: term.english,
          note: term.note,
          sort_order: tIndex + 1,
        });

        await db.srs_items.put({
          item_id: term.id,
          item_type: 'foundation',
          foundation_lesson_id: lesson.id,
          italian: term.italian,
          english: term.english,
          correct_streak: 0,
          attempts: 0,
          correct_attempts: 0,
          due_at: new Date(0).toISOString(),
        });
      }

      for (const [eIndex, exercise] of lesson.exercises.entries()) {
        await db.foundation_exercises.put({
          id: exercise.id,
          lesson_id: lesson.id,
          kind: exercise.kind,
          prompt: exercise.prompt,
          answer: exercise.answer,
          options_json: exercise.options ? JSON.stringify(exercise.options) : undefined,
          sort_order: eIndex + 1,
        });
      }
    }

    // Seed Scenarios
    for (const [index, scenario] of scenarios.entries()) {
      await db.scenarios.put({
        id: scenario.id,
        category: scenario.category,
        title: scenario.title,
        description: scenario.description,
        sort_order: index + 1,
      });

      for (const [vIndex, term] of scenario.vocabulary.entries()) {
        await db.scenario_vocabulary.put({
          id: term.id,
          scenario_id: scenario.id,
          italian: term.italian,
          english: term.english,
          correct_streak_required: 3,
          sort_order: vIndex + 1,
        });

        await db.srs_items.put({
          item_id: term.id,
          item_type: 'vocabulary',
          scenario_id: scenario.id,
          italian: term.italian,
          english: term.english,
          correct_streak: 0,
          attempts: 0,
          correct_attempts: 0,
          due_at: new Date(0).toISOString(),
        });
      }

      for (const [pIndex, phrase] of scenario.phrases.entries()) {
        await db.scenario_phrases.put({
          id: phrase.id,
          scenario_id: scenario.id,
          italian: phrase.italian,
          english: phrase.english,
          pass_score: 85,
          sort_order: pIndex + 1,
        });
      }

      for (const [sIndex, sentence] of scenario.sentences.entries()) {
        await db.scenario_sentences.put({
          id: sentence.id,
          scenario_id: scenario.id,
          italian: sentence.italian,
          english: sentence.english,
          grammar_point: sentence.grammarPoint,
          pass_score: 80,
          sort_order: sIndex + 1,
        });
      }
    }

    await db.app_metadata.put({ key: 'seed_version', value: '1', updated_at: new Date().toISOString() });
  });
}

// Repository functions matching vocabularyRepository.ts
export async function loadScenarioHeader(scenarioId: number) {
  return await db.scenarios.get(scenarioId);
}

export async function loadScenarioVocabulary(scenarioId: number) {
  const rows = await db.scenario_vocabulary
    .where('scenario_id')
    .equals(scenarioId)
    .sortBy('sort_order');
  return rows.map(r => ({
    id: r.id,
    scenarioId: r.scenario_id,
    italian: r.italian,
    english: r.english,
    correctStreakRequired: r.correct_streak_required,
    sortOrder: r.sort_order,
  }));
}

export async function loadScenarioPhrases(scenarioId: number) {
  const rows = await db.scenario_phrases
    .where('scenario_id')
    .equals(scenarioId)
    .sortBy('sort_order');
  return rows.map(r => ({
    id: r.id,
    scenarioId: r.scenario_id,
    italian: r.italian,
    english: r.english,
    passScore: r.pass_score,
    sortOrder: r.sort_order,
  }));
}

export async function loadScenarioSentences(scenarioId: number) {
  const rows = await db.scenario_sentences
    .where('scenario_id')
    .equals(scenarioId)
    .sortBy('sort_order');
  return rows.map(r => ({
    id: r.id,
    scenarioId: r.scenario_id,
    italian: r.italian,
    english: r.english,
    grammarPoint: r.grammar_point,
    passScore: r.pass_score,
    sortOrder: r.sort_order,
  }));
}

export async function loadScenarioConversationVocabulary(scenarioId: number) {
  const vocab = await db.scenario_vocabulary.where('scenario_id').equals(scenarioId).toArray();
  const phrases = await db.scenario_phrases.where('scenario_id').equals(scenarioId).toArray();
  const sentences = await db.scenario_sentences.where('scenario_id').equals(scenarioId).toArray();
  
  return [
    ...vocab.map(v => v.italian),
    ...phrases.map(p => p.italian),
    ...sentences.map(s => s.italian),
  ];
}
