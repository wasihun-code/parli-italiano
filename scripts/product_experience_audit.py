import os

def check_file(path, required_strings):
    try:
        with open(path, 'r') as f:
            content = f.read()
            for string in required_strings:
                if string not in content:
                    return False, f"Missing: {string}"
        return True, "Pass"
    except Exception as e:
        return False, str(e)

def audit():
    print("Starting Phase 9.7 Product Experience Audit...")
    failures = 0

    # Defect 1: Fullscreen Mode
    res, msg = check_file('src/components/FooterNav.tsx', ["'/train'"])
    if not res:
        print(f"FAIL (Defect 1): FooterNav not hidden on /train. {msg}")
        failures += 1
    else:
        print("PASS: Immersive Mode Active")

    # Defect 2: Exercise Layout
    res, msg = check_file('src/components/learning/exercises/SpellingExercise.tsx', ["maxWidth: 600", "padding: spacing.xxl", "fontSize: 40"])
    if not res:
        print(f"FAIL (Defect 2): Spelling layout not dominant. {msg}")
        failures += 1
    else:
        print("PASS: Layout Redesigned")

    # Defect 3: Listening Redesign
    res, msg = check_file('src/components/learning/exercises/ListenExercise.tsx', ["Ascolta e seleziona", "options.map"])
    if not res:
        print(f"FAIL (Defect 3): ListenExercise is not a recognition task. {msg}")
        failures += 1
    else:
        print("PASS: Listening Rebuilt")

    # Defect 6: Error Handling
    res, msg = check_file('src/components/learning/FeedbackOverlay.tsx', ["Risposta Corretta", "Non preoccuparti"])
    if not res:
        print(f"FAIL (Defect 6): FeedbackOverlay error states not updated. {msg}")
        failures += 1
    else:
        print("PASS: Error Handling Enhanced")

    # Defect 7: Lesson Unlock
    res, msg = check_file('src/screens/MiniLessonScenarioView.tsx', ["lesson.unlockCriteria === 'none'"])
    if not res:
        print(f"FAIL (Defect 7): Unlock logic not defaulting correctly. {msg}")
        failures += 1
    else:
        print("PASS: Lesson Unlock Fixed")

    # Defect 8: Scenario Immersion
    res, msg = check_file('src/screens/LearningSystemV3PilotScreen.tsx', ["Conversation Stage", "Current Goal", "Why This Matters", "Conversation Preview"])
    if not res:
        print(f"FAIL (Defect 8): Scenario immersion elements missing. {msg}")
        failures += 1
    else:
        print("PASS: Scenario Immersion Present")

    # Defect 10: Sentence Training Rebalance
    res, msg = check_file('src/services/learningPathGenerator.ts', ["exerciseType: 'Spelling'", "exerciseType: 'Listen'"])
    if not res:
        print(f"FAIL (Defect 10): Sentences not mapped to active pilot exercises. {msg}")
        failures += 1
    else:
        print("PASS: Sentence Training Rebalanced")

    if failures == 0:
        print("\nOVERALL: PASS. Ready for Production.")
        exit(0)
    else:
        print(f"\nOVERALL: FAIL. {failures} defects remaining.")
        exit(1)

if __name__ == "__main__":
    audit()
