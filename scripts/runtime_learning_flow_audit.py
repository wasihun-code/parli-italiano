import os
import sys

def run_learning_flow_audit():
    print("\n--- RUNTIME LEARNING FLOW AUDIT (STATIC) ---")
    
    conv_file = "src/screens/ScriptedConversationScreen.tsx"
    with open(conv_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Rule: Host audio autoplay
    # Check for Tts.speak in useEffect for initialization and handleContinue
    has_host_autoplay_init = "void Tts.speak(firstMsg.text)" in content
    has_host_autoplay_advance = "void Tts.speak(nextMsg.text)" in content
    
    # Rule: User audio manual only
    # Check that Tts.speak is NOT in handleChoice
    has_user_autoplay_choice = "void Tts.speak(choice.text)" in content
    
    # Check for speaker icon in user history
    has_user_manual_trigger = 'msg.role === \'user\'' in content and '🔊' in content
    
    print(f"Host autoplay implemented: {'YES' if (has_host_autoplay_init and has_host_autoplay_advance) else 'NO'}")
    print(f"User autoplay present: {'YES' if has_user_autoplay_choice else 'NO'}")
    print(f"User manual speaker icon present: {'YES' if has_user_manual_trigger else 'NO'}")
    
    success = has_host_autoplay_init and has_host_autoplay_advance and not has_user_autoplay_choice and has_user_manual_trigger
    
    if success:
        print("CONVERSATION FLOW AUDIT: PASS")
        return True
    else:
        print("CONVERSATION FLOW AUDIT: FAIL")
        return False

if __name__ == "__main__":
    success = run_learning_flow_audit()
    sys.exit(0 if success else 1)
