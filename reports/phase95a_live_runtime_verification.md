# Phase 9.5A: Live Runtime Verification

## 1. Summary

The Learning System V3 architecture is currently operating as a **sidecar layer**. While the V3 engine (`LearningPathGenerator`), registry, and pilot renderer are implementation-complete and verified via automated audits, they are not yet wired into the primary user experience. The production environment continues to serve the "Apartment Key Pickup" scenario using the legacy V1/V2 static screens.

## 2. Route Verification

| Question | Answer |
| :--- | :--- |
| **Route for Apartment Key Pickup** | `/scenarios/22/lesson/:lessonId/train` |
| **Active Component** | `MiniLessonTrainingScreen` |
| **V3 Pilot Reachable?** | **NO** (Orphan route) |
| **V3 Generator Used in Prod?** | **NO** |
| **V3 Renderer Used in Prod?** | **NO** |

## 3. Detailed Trace

### Route: `/scenarios/22/lesson/:lessonId/train`
This is the live route rendered when a user clicks a mini-lesson for Apartment Key Pickup.
- **Component:** `MiniLessonTrainingScreen`
- **Execution Path:**
  1. `MiniLessonTrainingScreen` extracts `scenarioId` (22) from params.
  2. It loads `scenario.miniLessons` from the static `scenarios` registry.
  3. It manually iterates through `section.exerciseIds`.
  4. It performs a manual lookup for each ID in the `vocabulary`, `phrases`, or `sentences` arrays.
  5. It renders a hard-coded multiple-choice UI.
- **Pedagogical Status:** Alphabetical ordering (V2) is enforced because the component reads the `exerciseIds` directly from the static `mini_lessons.json` file.

### Component: `LearningSystemV3PilotScreen`
- **Status:** **ORPHAN**.
- **Proof:** `src/App.tsx` contains NO route for `LearningSystemV3PilotScreen`. The component is imported but never used in the `<Routes>` tree.
- **Accessibility:** Reachable ONLY via manual modification of `App.tsx` or a dev-only hook. Normal users cannot access it.

### V3 Logic Integration
- **`LearningPathGenerator`:** Only imported in the orphan `LearningSystemV3PilotScreen`. Not used in `MiniLessonTrainingScreen`, `VocabularyTrainingScreen`, etc.
- **`ExerciseRenderer`:** Only imported in the orphan `LearningSystemV3PilotScreen`. Not used in production lesson screens.
- **Pilot Exercises (`Listen`, `Match`, `Spelling`):** These components are currently private to the V3 pilot and are not used by the production learning flow.

## 4. Component Tree Trace (Live Production)

When a user opens **accommodation/apartment_key_pickup**:

```text
[App]
  └── [BrowserRouter]
        └── [Routes]
              └── [Route path="/scenarios/:scenarioId/lesson/:lessonId/train"]
                    └── [MiniLessonTrainingScreen]
                          ├── [Screen]
                          │     └── [Header]
                          ├── [Tts (lib)]
                          ├── [FeedbackMessage]
                          └── [PrimaryButton]
```

**Note:** This tree contains **Zero** V3 architecture components.

## 5. Conclusion

Phase 9.5 has successfully built a parallel "V3 universe", but the "V2 universe" is still the one users live in. The V3 architecture is a **Proof of Concept Sidecar** that is ready for activation but currently dormant in production.

**Risk:** Users are still facing the "Alphabetical Trap" and static lessons because the implementation of V3 has not yet crossed the "Activation Gap" into the actual route definitions.
