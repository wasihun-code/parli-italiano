import os
import subprocess
import glob
import concurrent.futures

AUDIO_DIR = "public/audio"
TEMP_DIR = "public/audio_temp"

def fix_file(file_path):
    filename = os.path.basename(file_path)
    temp_path = os.path.join(TEMP_DIR, filename)
    
    # Check if it's already Opus
    res = subprocess.run(["file", file_path], capture_output=True, text=True)
    if "Ogg data, Opus audio" in res.stdout:
        return f"Skipped {filename} (already Opus)"
        
    try:
        # Convert to Opus with normalization
        # -af loudnorm: loudness normalization
        # -c:a libopus: opus codec
        # -b:a 32k: bitrate (good for speech)
        # -application voip: optimized for speech
        subprocess.run([
            "ffmpeg", "-y", "-i", file_path,
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-c:a", "libopus", "-b:a", "32k", "-application", "voip",
            temp_path
        ], check=True, capture_output=True)
        
        # Replace original
        os.replace(temp_path, file_path)
        return f"Fixed {filename}"
    except Exception as e:
        return f"Error fixing {filename}: {e}"

def main():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
        
    files = glob.glob(os.path.join(AUDIO_DIR, "*.opus"))
    print(f"Auditing and fixing {len(files)} files...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(fix_file, files))
        
    for res in results[:20]:
        print(res)
    if len(results) > 20:
        print(f"... processed {len(results)} files total.")

if __name__ == "__main__":
    main()
