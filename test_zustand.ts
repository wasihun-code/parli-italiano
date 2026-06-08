import { emptyScenarioProgress } from './src/store/progressStore';

function resolveScenarioProgress(progress: any, scenarioId: number) {
  return progress[scenarioId] ?? emptyScenarioProgress;
}

function withConversationGate(progress: any, totalLessons: number) {
  const allMiniLessonsDone = progress.miniLessonsCompleted && progress.miniLessonsCompleted.length >= totalLessons;
  return { ...progress, conversationUnlocked: allMiniLessonsDone };
}

let state = { scenarioProgress: {} };

function completeMiniLesson(scenarioId: number, lessonId: string, totalLessons: number) {
  const existing = resolveScenarioProgress(state.scenarioProgress, scenarioId);
  const currentCompleted = existing.miniLessonsCompleted || [];
  const nextCompleted = currentCompleted.includes(lessonId) 
    ? currentCompleted 
    : [...currentCompleted, lessonId];
  
  state = {
    scenarioProgress: {
      ...state.scenarioProgress,
      [scenarioId]: withConversationGate({
        ...existing,
        miniLessonsCompleted: nextCompleted,
      }, totalLessons),
    },
  };
}

completeMiniLesson(22, 'l1', 6);
console.log(JSON.stringify(state, null, 2));

// Complete again to see if it duplicates
completeMiniLesson(22, 'l1', 6);
console.log(JSON.stringify(state, null, 2));
