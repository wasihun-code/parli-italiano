import sys
import os
import re

def run_audit():
    print("Starting Exercise Registry Audit...")
    
    registry_path = "src/exercises/registry.ts"
    types_path = "src/types/learningPath.ts"
    
    if not os.path.exists(registry_path):
        print(f"❌ FAIL: Registry not found at {registry_path}")
        return False

    with open(registry_path, 'r') as f:
        registry_content = f.read()
        
    with open(types_path, 'r') as f:
        types_content = f.read()

    # Extract all types from the ExerciseType union specifically
    # Using re.DOTALL and re.MULTILINE for robustness
    exercise_type_block = re.search(r"export type ExerciseType =\s*(.*?);", types_content, re.DOTALL)
    if not exercise_type_block:
        print("❌ FAIL: Could not find ExerciseType definition in types.ts")
        return False
    
    type_matches = re.findall(r"'(\w+)'", exercise_type_block.group(1))
    
    # Extract only the top-level keys in ExerciseRegistry
    registry_block = re.search(r"export const ExerciseRegistry: Record<string, ExerciseDefinition> = \{(.*?)\};", registry_content, re.DOTALL)
    if not registry_block:
        print("❌ FAIL: Could not find ExerciseRegistry definition in registry.ts")
        return False
        
    inner_registry = registry_block.group(1)
    # Match keys that are followed by : { at the beginning of a line (with optional whitespace)
    registry_keys = re.findall(r"^\s{2}(\w+): \{", inner_registry, re.MULTILINE)
    
    print(f"Found {len(type_matches)} official types in types.ts: {type_matches}")
    print(f"Found {len(registry_keys)} registered entries in registry.ts: {registry_keys}")

    all_pass = True

    # Check 1: Every Type in types.ts is in Registry
    for t in type_matches:
        if t not in registry_keys:
            print(f"❌ FAIL: Type '{t}' is defined in types.ts but missing from ExerciseRegistry")
            all_pass = False
        else:
            print(f"✅ Type '{t}' is registered.")

    # Check 2: Registry entries have mandatory components
    mandatory_fields = ['metadata', 'payloadBuilder', 'validator', 'completionHandler']
    for t in registry_keys:
        # Find the block for this specific key
        # Simplest way: find from t: { to the next occurrence of   }, (two spaces, closing brace, comma)
        match = re.search(rf"^\s{{2}}{t}: \{{(.*?)\s{{2}}\}},", inner_registry, re.MULTILINE | re.DOTALL)
        if not match:
             # Try for the last item in the object
             match = re.search(rf"^\s{{2}}{t}: \{{(.*?)\s{{2}}\}}", inner_registry, re.MULTILINE | re.DOTALL)

        if match:
            content = match.group(1)
            for field in mandatory_fields:
                if field not in content:
                    print(f"❌ FAIL: Registry entry '{t}' is missing field '{field}'")
                    all_pass = False
        else:
            print(f"⚠️ Warning: Could not verify fields for '{t}' via regex.")

    if all_pass:
        print("✅ PASS: Exercise Registry is 100% compliant with the runtime contract.")
        return True
    else:
        print("❌ FAIL: Exercise Registry inconsistencies detected.")
        return False

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
