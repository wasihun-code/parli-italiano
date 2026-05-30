import os
import sys

def main():
    print("\n--- Keyboard Accessibility Audit (STATIC) ---")
    
    files_to_check = [
        "src/screens/ScriptedConversationScreen.tsx",
        "src/screens/MiniLessonTrainingScreen.tsx"
    ]
    
    required_keys = [
        "e.key === 'Escape'",
        "e.key === 'Enter'",
        "e.key === ' '", # Space
    ]
    
    # Check for '1-4' mapping logic, which varies slightly.
    # We look for parseInt(e.key) or e.key >= '1'
    choice_logic = ["parseInt(e.key", "e.key >= '1'"]
    
    errors = []
    
    for fpath in files_to_check:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            errors.append(f"Failed to read {fpath}: {e}")
            continue
            
        for req in required_keys:
            if req not in content:
                errors.append(f"{fpath} missing handler for {req}")
                
        if not any(c in content for c in choice_logic):
            errors.append(f"{fpath} missing choice selection logic (1-4)")
            
        # Scripted conversation also needs 't' for translation
        if "Conversation" in fpath:
            if "e.key.toLowerCase() === 't'" not in content and "e.key === 't'" not in content:
                errors.append(f"{fpath} missing translation toggle ('t')")

    if errors:
        for e in errors: print(f"  - {e}")
        print("Keyboard Audit: FAIL")
        return False
    else:
        print("Keyboard Audit: PASS")
        return True

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
