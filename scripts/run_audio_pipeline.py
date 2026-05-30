import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from audio_manager import extract_corpus_data, generate_manifest, inject_audio_paths
import json

def run_audio_pipeline():
    print("Extracting corpus data...")
    text_to_categories = extract_corpus_data("src/data/exports")
    
    print("Generating manifest...")
    manifest = generate_manifest(text_to_categories, "public/audio_manifest.json")
    
    print("Injecting audio paths...")
    inject_audio_paths("src/data/exports", manifest)
    
if __name__ == "__main__":
    run_audio_pipeline()
