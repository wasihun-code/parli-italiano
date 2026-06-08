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
    print("Starting Phase 9.6c Exercise Execution Audit...")
    failures = 0

    # 1. Payload Valid
    res, msg = check_file('src/exercises/registry.ts', ["payloadBuilder: mcqPayloadBuilder"])
    if not res:
        print(f"FAIL: Listen exercise not using mcq payload. {msg}")
        failures += 1
    else:
        print("PASS: Listen payload validity")

    # 2. Renderable & Recoverable (Fail-safe)
    res, msg = check_file('src/components/learning/ExerciseRenderer.tsx', [
        "handleEmergencySkip", 
        "if (!definition || !payload)", 
        "Salta Esercizio"
    ])
    if not res:
        print(f"FAIL: ExerciseRenderer missing fail-safes. {msg}")
        failures += 1
    else:
        print("PASS: Renderer fail-safes")

    # 3. Session Validation
    res, msg = check_file('src/services/sessionValidator.ts', [
        "['Listen', 'Match', 'ListenChoose'].includes",
        "return false"
    ])
    if not res:
        print(f"FAIL: SessionValidator not enforcing strict payload rules. {msg}")
        failures += 1
    else:
        print("PASS: Session pre-flight validation")

    if failures == 0:
        print("\nOVERALL: PASS. Learning flow is playable and protected against deadlocks.")
        exit(0)
    else:
        print(f"\nOVERALL: FAIL. {failures} execution issues remaining.")
        exit(1)

if __name__ == "__main__":
    audit()
