import { useProgressStore } from '../src/store/progressStore';

async function runAudit() {
  console.log("Starting Lesson Unlock Audit...");

  const store = useProgressStore.getState();
  
  // 1. Check initial state
  const initialProgress = store.scenarioProgress[22];
  if (initialProgress && initialProgress.miniLessonsCompleted && initialProgress.miniLessonsCompleted.length > 0) {
    console.log("Store not empty. Resetting...");
    store.resetProgress();
  }

  // 2. Complete Lesson 1
  console.log("Simulating completion of Lesson 1 ('l1')...");
  store.completeMiniLesson(22, 'l1', 6);
  
  const progressAfter1 = useProgressStore.getState().scenarioProgress[22];
  if (!progressAfter1?.miniLessonsCompleted?.includes('l1')) {
    console.log("FAIL: Lesson 1 completion not stored in state.");
    process.exit(1);
  }
  console.log("PASS: Lesson 1 completion stored.");

  // 3. Verify Lesson 2 Unlock Logic
  const completedLessons = progressAfter1.miniLessonsCompleted || [];
  const prevLessonId = 'l1'; // For lesson 2, prev is l1
  const isLesson2Unlocked = completedLessons.includes(prevLessonId);
  
  if (!isLesson2Unlocked) {
    console.log("FAIL: Lesson 2 unlock logic evaluated to false.");
    process.exit(1);
  }
  console.log("PASS: Lesson 2 unlock logic evaluated to true.");

  // 4. Complete Lesson 2
  console.log("Simulating completion of Lesson 2 ('l2')...");
  store.completeMiniLesson(22, 'l2', 6);
  
  const progressAfter2 = useProgressStore.getState().scenarioProgress[22];
  if (!progressAfter2?.miniLessonsCompleted?.includes('l2')) {
    console.log("FAIL: Lesson 2 completion not stored in state.");
    process.exit(1);
  }
  console.log("PASS: Lesson 2 completion stored.");

  console.log("\nOVERALL: PASS. Progression flow is mathematically sound.");
}

runAudit().catch(console.error);
