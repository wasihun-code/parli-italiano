import os
import json
import asyncio
import edge_tts
import random
import time
import sys
import subprocess

MANIFEST_PATH = "public/audio_manifest.json"
AUDIO_OUTPUT_DIR = "public/audio"
CONCURRENCY_LIMIT = 3
DELAY_RANGE = (0.3, 1.0) # GEMINI.md recommends 300ms-1000ms
MAX_RETRIES = 5 # GEMINI.md recommends 3-5

async def synthesize_text(text, voice_id, voice_name, info, manifest_registry, lock):
    """Synthesize a single text item with retries and delays."""
    filename = info["filename"]
    output_path = os.path.join(AUDIO_OUTPUT_DIR, filename)
    temp_mp3 = output_path + ".mp3"
    
    if os.path.exists(output_path):
        async with lock:
            info["status"] = "completed"
        return True

    for attempt in range(MAX_RETRIES):
        try:
            # Randomized delay to be conservative
            await asyncio.sleep(random.uniform(*DELAY_RANGE))
            
            communicate = edge_tts.Communicate(text, voice_name)
            await communicate.save(temp_mp3)
            
            # Convert to Opus with normalization
            subprocess.run([
                "ffmpeg", "-y", "-i", temp_mp3,
                "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                "-c:a", "libopus", "-b:a", "32k", "-application", "voip",
                output_path
            ], check=True, capture_output=True)
            
            # Cleanup temp file
            if os.path.exists(temp_mp3):
                os.remove(temp_mp3)
                
            async with lock:
                info["status"] = "completed"
            return True
            
        except Exception as e:
            if os.path.exists(temp_mp3):
                os.remove(temp_mp3)
            print(f"Error synthesizing '{text[:30]}...' with {voice_id} (attempt {attempt+1}): {e}")
            if attempt < MAX_RETRIES - 1:
                # Exponential backoff for retries
                await asyncio.sleep(random.uniform(1.0, 2.0) * (2 ** attempt))
            else:
                async with lock:
                    info["status"] = f"failed: {str(e)}"
    
    return False

async def main(category=None, limit=None):
    if not os.path.exists(AUDIO_OUTPUT_DIR):
        os.makedirs(AUDIO_OUTPUT_DIR)
        
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    registry = manifest["registry"]
    voice_map = manifest["metadata"]["voice_map"]
    
    pending_tasks = []
    
    for text, voices in registry.items():
        for voice_id, info in voices.items():
            if info["status"] == "pending":
                if category and category not in info.get("categories", []):
                    continue
                
                voice_name = voice_map.get(voice_id)
                if not voice_name:
                    continue
                    
                pending_tasks.append((text, voice_id, voice_name, info))

    if limit:
        pending_tasks = pending_tasks[:limit]
        
    if category:
        print(f"Targeting category: {category}")
    print(f"Processing {len(pending_tasks)} items.")

    if not pending_tasks:
        print("No pending items to process.")
        return

    lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    
    async def sem_task(text, voice_id, voice_name, info):
        async with semaphore:
            return await synthesize_text(text, voice_id, voice_name, info, registry, lock)
    
    results = []
    chunk_size = 50
    for i in range(0, len(pending_tasks), chunk_size):
        chunk = pending_tasks[i:i + chunk_size]
        tasks = [sem_task(*item) for item in chunk]
        chunk_results = await asyncio.gather(*tasks)
        results.extend(chunk_results)
        
        # Periodic save
        with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        print(f"Progress: {i + len(chunk)}/{len(pending_tasks)} items processed...")
    
    success_count = sum(1 for r in results if r)
    print(f"Batch completed. Success: {success_count}/{len(pending_tasks)}")

if __name__ == "__main__":
    target_category = None
    target_limit = None
    
    # Usage: python synthesize_audio.py [category] [limit]
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            target_limit = int(sys.argv[1])
        else:
            target_category = sys.argv[1]
            if len(sys.argv) > 2 and sys.argv[2].isdigit():
                target_limit = int(sys.argv[2])
                
    asyncio.run(main(target_category, target_limit))
