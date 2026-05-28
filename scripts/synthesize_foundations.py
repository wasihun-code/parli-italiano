import os
import json
import asyncio
import edge_tts
import random
import time
import hashlib
import re

MANIFEST_PATH = "public/audio_manifest.json"
AUDIO_OUTPUT_DIR = "public/audio"
VOICE_ID = "elsa"
VOICE_NAME = "it-IT-ElsaNeural"
CONCURRENCY_LIMIT = 3
DELAY_RANGE = (0.3, 1.0)
MAX_RETRIES = 5

def get_audio_hash(text, voice_id=VOICE_ID):
    key = f"{text.strip()}|{voice_id}"
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]

def extract_foundations():
    foundation_file = "src/data/foundations.ts"
    with open(foundation_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple regex to find italian: '...'
    matches = re.findall(r"italian: '(.*?)'", content)
    return sorted(list(set(matches)))

async def synthesize_text(text, manifest, lock):
    h = get_audio_hash(text)
    filename = f"{h}.opus"
    output_path = os.path.join(AUDIO_OUTPUT_DIR, filename)
    
    if os.path.exists(output_path):
        if text not in manifest["registry"]:
            manifest["registry"][text] = {}
        if VOICE_ID not in manifest["registry"][text]:
            manifest["registry"][text][VOICE_ID] = {
                "hash": h,
                "filename": filename,
                "path": f"/audio/{filename}",
                "status": "completed",
                "categories": ["foundations"]
            }
        return True

    for attempt in range(MAX_RETRIES):
        try:
            await asyncio.sleep(random.uniform(*DELAY_RANGE))
            communicate = edge_tts.Communicate(text, VOICE_NAME)
            # Edge TTS doesn't normalize, but we'll do it later if needed.
            # For now, just save.
            await communicate.save(output_path)
            
            async with lock:
                if text not in manifest["registry"]:
                    manifest["registry"][text] = {}
                manifest["registry"][text][VOICE_ID] = {
                    "hash": h,
                    "filename": filename,
                    "path": f"/audio/{filename}",
                    "status": "completed",
                    "categories": ["foundations"]
                }
            return True
            
        except Exception as e:
            print(f"Error '{text}': {e}")
            await asyncio.sleep(2 ** attempt)
    
    return False

async def main():
    if not os.path.exists(AUDIO_OUTPUT_DIR):
        os.makedirs(AUDIO_OUTPUT_DIR)
        
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    texts = extract_foundations()
    print(f"Found {len(texts)} unique foundation texts.")
    
    lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    
    async def sem_task(text):
        async with semaphore:
            return await synthesize_text(text, manifest, lock)
    
    tasks = [sem_task(text) for text in texts]
    results = await asyncio.gather(*tasks)
    
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"Done! Synthesized: {sum(1 for r in results if r)}/{len(texts)}")

if __name__ == "__main__":
    asyncio.run(main())
