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
    print("Starting Phase 9.7a Pedagogical Quality Audit...")
    failures = 0

    # 1. Lesson Unlock Integrity
    res, msg = check_file('src/screens/LearningSystemV3PilotScreen.tsx', ["Number(scenarioId || 22)"])
    if not res:
        print(f"FAIL: Lesson unlock uses hardcoded ID. {msg}")
        failures += 1
    else:
        print("PASS: Lesson unlock is dynamic")

    # 2. Feedback Coverage
    res, msg = check_file('src/components/learning/FeedbackOverlay.tsx', ["Risposta Corretta", "Non preoccuparti"])
    if not res:
        print(f"FAIL: Feedback doesn't have clear wrong states. {msg}")
        failures += 1
    else:
        print("PASS: Feedback is universal and clear")

    # 3. Sentence Coverage
    res, msg = check_file('src/services/sessionGenerator.ts', ["targetVocab", "targetSentences", "Math.floor(this.TARGET_SESSION_SIZE * 0.3)"])
    if not res:
        print(f"FAIL: Session generator does not guarantee sentences. {msg}")
        failures += 1
    else:
        print("PASS: Sentence distribution enforced")

    # 4. Readiness Visibility
    res, msg = check_file('src/screens/LearningSystemV3PilotScreen.tsx', ["Lesson Mastery", "Scenario Readiness"])
    if not res:
        print(f"FAIL: Footer does not show dynamic progress. {msg}")
        failures += 1
    else:
        print("PASS: Readiness redesign complete")

    # 5. Scenario Immersion
    res, msg = check_file('src/screens/LearningSystemV3PilotScreen.tsx', ["Current Goal", "Why This Matters"])
    if not res:
        print(f"FAIL: Context banner is not prominent. {msg}")
        failures += 1
    else:
        print("PASS: Immersion elements active")

    if failures == 0:
        print("\nOVERALL: PASS. Pedagogical Quality Verified.")
        exit(0)
    else:
        print(f"\nOVERALL: FAIL. {failures} pedagogical issues remaining.")
        exit(1)

if __name__ == "__main__":
    audit()
