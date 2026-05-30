import json

def count_missing():
    with open('public/audio_manifest.json', 'r', encoding='utf-8') as f:
        manifest = json.load(f)
        
    pending_count = 0
    completed_count = 0
    
    for text, voices in manifest['registry'].items():
        for voice_id, info in voices.items():
            if info['status'] == 'pending':
                pending_count += 1
            else:
                completed_count += 1
                
    print(f"Total Completed: {completed_count}")
    print(f"Total Pending: {pending_count}")

if __name__ == "__main__":
    count_missing()
