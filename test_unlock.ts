const fs = require('fs');

// We simulate the exact flow
const state = {
  scenarioProgress: {}
};

function resolveScenarioProgress(progress: any, scenarioId: number) {
  return progress[scenarioId] ?? { miniLessonsCompleted: [] };
}

function withConversationGate(progress: any, totalLessons: number) {
  return progress;
}

function completeMiniLesson(scenarioId: number, lessonId: string, totalLessons: number) {
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

// User completes lesson l1
completeMiniLesson(22, 'l1', 6);

// Now in view
const scenario = { id: 22, miniLessons: [{id: 'l1'}, {id: 'l2'}] };
const progress = state.scenarioProgress[scenario.id] || { miniLessonsCompleted: [] };
const completedLessons = progress.miniLessonsCompleted || [];

const isCompleted = completedLessons.includes('l1');
console.log("Lesson 1 completed:", isCompleted);

const idx = 1; // Lesson 2
const lesson = scenario.miniLessons[idx];
const prevLessonId = scenario.miniLessons[idx - 1].id;
const isUnlocked = completedLessons.includes(prevLessonId);
console.log("Lesson 2 unlocked:", isUnlocked);

