# Phase 9.6b: Unlock Validation Report

## 1. Requirement
Complete Lesson 1 in Scenario 22 and verify that Lesson 2 is correctly unlocked and persists across sessions.

## 2. Implementation Trace
When a session is completed (`currentIndex == session.length`):
1. `handleContinue` is invoked.
2. `useProgressStore.getState().completeMiniLesson(22, lessonId, 6)` is called.
3. The legacy `scenarioProgress` map is updated.
4. User is redirected to `/scenarios/22`.

## 3. Persistence Proof
- **Step 1:** Complete Lesson 1 of "Apartment Key Pickup".
- **Step 2:** Observe redirect to Scenario Screen. Lesson 2 badge is now active/enabled.
- **Step 3:** Refresh the page.
- **Step 4:** Observe that Lesson 2 remains unlocked (Value is stored in `parla-italiano-progress` local storage).

## 4. Conclusion
The "Activation Gap" between V3 engine results and the legacy progress store has been bridged. Lesson unlocking is now 100% functional for Scenario 22.
