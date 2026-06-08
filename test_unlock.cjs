const fs = require('fs');

// Simulate the store
let state = {
  scenarioProgress: {}
};

const emptyScenarioProgress = {
  vocabularyCompleted: false,
  phraseScore: 0,
  phraseCompleted: false,
  sentenceScore: 0,
  sentenceCompleted: false,
  conversationUnlocked: false,
  skipTestUsed: false,
  miniLessonsCompleted: [],
};

function resolveScenarioProgress(progress, scenarioId) {
  return progress[scenarioId] ?? emptyScenarioProgress;
}

function withConversationGate(progress, totalLessons) {
  const allMiniLessonsDone = totalLessons !== undefined && 
                             progress.miniLessonsCompleted && 
                             progress.miniLessonsCompleted.length >= totalLessons;

  return {
    ...progress,
    conversationUnlocked:
      (progress.vocabularyCompleted &&
      progress.phraseCompleted &&
      progress.sentenceCompleted) || 
      allMiniLessonsDone,
  };
}

function completeMiniLesson(scenarioId, lessonId, totalLessons) {
  const existing = resolveScenarioProgress(state.scenarioProgress, scenarioId);
  const currentCompleted = existing.miniLessonsCompleted || [];
  const nextCompleted = currentCompleted.includes(lessonId) 
    ? currentCompleted 
    : [...currentCompleted, lessonId];
  
  state.scenarioProgress = {
    ...state.scenarioProgress,
    [scenarioId]: withConversationGate({
      ...existing,
      miniLessonsCompleted: nextCompleted,
    }, totalLessons),
  };
}

// 1. User completes lesson l1
completeMiniLesson(22, 'l1', 6);

console.log("State after completion:", JSON.stringify(state, null, 2));

// 2. User goes to view
const scenario = { id: 22, miniLessons: [{id: 'l1'}, {id: 'l2'}] };
const progress = state.scenarioProgress[scenario.id] || emptyScenarioProgress;
const completedLessons = progress.miniLessonsCompleted || [];

const isCompleted = completedLessons.includes('l1');
console.log("Lesson 1 completed:", isCompleted);

const idx = 1; // Lesson 2
const lesson = scenario.miniLessons[idx];
const prevLessonId = scenario.miniLessons[idx - 1].id;
const isUnlocked = completedLessons.includes(prevLessonId);
console.log("Lesson 2 unlocked:", isUnlocked);
