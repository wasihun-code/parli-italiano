// Web implementation of analytics
// In a real app, you'd initialize Firebase here.
// import { getAnalytics, logEvent as fbLogEvent } from "firebase/analytics";

export async function logEvent(name: string, params?: Record<string, unknown>) {
  console.log(`[Analytics] ${name}`, params);
  // fbLogEvent(analytics, name, params);
}

export function trackFoundationLessonCompleted(lessonId: number, score: number) {
  return logEvent('foundation_lesson_completed', { lessonId, score });
}

export function trackScenarioVocabularyCompleted(scenarioId: number) {
  return logEvent('scenario_vocabulary_completed', { scenarioId });
}

export function trackScenarioPhraseCompleted(scenarioId: number, score: number) {
  return logEvent('scenario_phrase_completed', { scenarioId, score });
}

export function trackScenarioSentenceCompleted(scenarioId: number, score: number) {
  return logEvent('scenario_sentence_completed', { scenarioId, score });
}

export function trackConversationStarted(scenarioId: number) {
  return logEvent('conversation_started', { scenarioId });
}

export function recordJsError(error: Error) {
  console.error('[Crashlytics-Web-Stub]', error);
}

export async function setCrashlyticsUserId(userId: string) {
  console.log('[Analytics] setUserId', userId);
}
