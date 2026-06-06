import os
import json
import glob
import re
from collections import defaultdict

def normalize_text(text):
    if not text:
        return ""
    # lowercase
    text = text.lower()
    # normalize apostrophes
    text = text.replace("'", "'").replace("’", "'").replace("`", "'")
    # normalize punctuation (remove basic punctuation for exact matching, or just strip it)
    # The prompt says "normalize punctuation", let's replace common punctuation with space to separate words, 
    # but for phrases/sentences maybe we want to strip trailing punctuation? 
    # Actually, removing punctuation like .,!?;: helps find exact duplicates
    text = re.sub(r'[.,!?;:""“”«»()[\]{}]', '', text)
    # remove duplicate spaces
    text = re.sub(r'\s+', ' ', text)
    # trim whitespace
    return text.strip()

def analyze_type(file_suffix, report_path, title, limit=None):
    files = glob.glob(f'src/data/exports/**/*{file_suffix}', recursive=True)
    
    total_items = 0
    normalized_counts = defaultdict(lambda: {"count": 0, "scenarios": set(), "english_translations": set()})
    
    for f in files:
        # e.g., src/data/exports/travel/airport_arrival/travel_airport_arrival_vocabulary.json
        parts = f.split('/')
        if len(parts) >= 5:
            category = parts[3]
            scenario = parts[4]
            slug = f"{category}/{scenario}"
            
            try:
                with open(f, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    for item in data:
                        italian = item.get("italian", "")
                        english = item.get("english", "")
                        if not italian:
                            continue
                        
                        total_items += 1
                        norm = normalize_text(italian)
                        
                        normalized_counts[norm]["count"] += 1
                        normalized_counts[norm]["scenarios"].add(slug)
                        if english:
                            normalized_counts[norm]["english_translations"].add(english)
            except Exception as e:
                pass
                
    unique_count = len(normalized_counts)
    compression_ratio = ((total_items - unique_count) / total_items * 100) if total_items > 0 else 0
    
    # Sort by frequency
    sorted_items = sorted(normalized_counts.items(), key=lambda x: x[1]["count"], reverse=True)
    
    with open(report_path, 'w', encoding='utf-8') as out:
        out.write(f"# {title}\n\n")
        out.write(f"- **Total items:** {total_items}\n")
        out.write(f"- **Unique normalized items:** {unique_count}\n")
        out.write(f"- **Compression ratio:** {compression_ratio:.2f}%\n\n")
        
        display_limit = limit if limit else 100
        out.write(f"## Top {display_limit} Repeated Items\n\n")
        
        for i, (norm, data) in enumerate(sorted_items[:display_limit]):
            out.write(f"### {i+1}. {norm}\n")
            out.write(f"- **Occurrences:** {data['count']}\n")
            out.write(f"- **Translations:** {', '.join(list(data['english_translations'])[:3])}\n")
            # Limit scenarios list length to avoid massive files
            scens = list(data['scenarios'])
            if len(scens) > 10:
                scens_str = ", ".join(scens[:10]) + f" ...and {len(scens) - 10} more"
            else:
                scens_str = ", ".join(scens)
            out.write(f"- **Scenarios:** [{scens_str}]\n\n")

    return sorted_items, total_items, unique_count

def generate_dictionary_prototype(vocab_items):
    report_path = "reports/global_dictionary_prototype.md"
    with open(report_path, "w", encoding="utf-8") as out:
        out.write("# Global Dictionary Prototype\n\n")
        out.write("Prototype structure for the top 200 vocabulary words.\n\n")
        
        for norm, data in vocab_items[:200]:
            eng = list(data["english_translations"])[0] if data["english_translations"] else "UNKNOWN"
            out.write(f"**Word:**\n\n{norm}\n\n")
            out.write(f"**English:**\n\n{eng}\n\n")
            
            out.write("**Occurrences:**\n\n")
            for s in list(data["scenarios"])[:5]:
                out.write(f"- {s}\n")
            if len(data["scenarios"]) > 5:
                out.write(f"- ...\n")
            out.write("\n")
            
            out.write(f"**Frequency:**\n\n{data['count']}\n\n")
            
            # Simple global ID mapping rule (replace spaces with underscore, ascii only approximation)
            safe_id = re.sub(r'[^a-z0-9]', '', norm.replace(' ', '_'))
            out.write(f"**Potential Global ID:**\n\nword_{safe_id}\n\n")
            out.write("---\n\n")

def generate_simulation(total_vocab, unique_vocab):
    report_path = "reports/knowledge_graph_simulation.md"
    compression = ((total_vocab - unique_vocab) / total_vocab * 100) if total_vocab > 0 else 0
    
    content = f"""# Knowledge Graph Simulation

## Architecture Shift Analysis

This report simulates the impact of moving from isolated scenario IDs to a unified Knowledge Graph architecture for vocabulary.

### Current Architecture: Scenario Mastery
- IDs are isolated per scenario (e.g., `s22-v15`, `s58-v115`).
- **Current Item Count (Total Extracted Vocab):** {total_vocab}

### Future Architecture: Global Knowledge Graph
- IDs are normalized and shared globally (e.g., `word_grazie`).
- **Potential Global Concepts:** {unique_vocab}

### Impact
- **Compression %:** {compression:.2f}%

Moving to a Global Knowledge Graph would eliminate the need to track {total_vocab - unique_vocab} redundant learning events. The system would shrink the vocabulary spaced repetition database significantly while providing a highly accurate measure of a user's true language acquisition.
"""
    with open(report_path, "w", encoding="utf-8") as out:
        out.write(content)

def generate_recommendations():
    report_path = "reports/global_mastery_recommendation.md"
    content = """# Global Mastery Recommendation

## Pedagogical Analysis

When a learner masters a common word like **"grazie"**, the system must decide how to handle future occurrences.

### Options:
**A. Never show again**
- *Result:* The word disappears from all future lessons and conversations. 
- *Flaw:* Unnatural. Conversations become Swiss cheese, missing crucial connecting words.

**B. Hide from vocabulary lessons, Still show in conversations**
- *Result:* The user skips the flashcard in the "Vocabulary" mini-lesson, but sees it in context during the Conversation exercise.
- *Benefit:* Reduces flashcard fatigue while maintaining contextual reading practice.

**C. Spaced repetition review**
- *Result:* The word appears in global SRS reviews, but is entirely decoupled from scenario progression.
- *Benefit:* Optimal for long-term memory.

**D. Hybrid model**
- *Result:* Vocabulary is tracked globally. If a user opens a new scenario containing "grazie", the vocabulary mini-lesson dynamically excludes it (or marks it pre-mastered). However, the word still appears in Phrases, Sentences, and Conversations to reinforce context.

### Recommended Approach: Hybrid Mastery

The **Hybrid Mastery** model is the pedagogically superior choice. 
- **Vocabulary** should be tracked via a Global Knowledge Graph. This provides accurate "Known Words" metrics and prevents flashcard fatigue.
- **Phrases, Sentences, and Conversations** should remain Scenario-Specific. Language is contextual. Mastering "piano" (floor) in a hotel scenario does not mean the user understands "piano" (slowly) in a clarification scenario. Phrases and sentences provide the necessary contextual scaffolding.

## Migration Impact Estimation

| System | Migration Risk | Impact Description |
| :--- | :--- | :--- |
| `linguistic_extractor.py` | **HIGH** | Must normalize strings, generate deterministic global IDs (`word_grazie`), and resolve homonyms/context clashes. |
| `curriculum_designer.py` | **HIGH** | Must map global IDs to scenarios and potentially adjust lesson chunking logic if globally known words are filtered out. |
| `srsStore.ts` | **MEDIUM** | Needs to transition from `scenario_id-vocab_id` composite keys to tracking global `word_id` states. |
| `progressStore.ts` | **MEDIUM** | Scenario unlocking logic must become dynamic (e.g., "unlock if all scenario-specific phrases are done AND all associated global vocab is known"). |
| `training screens` | **HIGH** | UI needs to fetch global SRS state to dynamically filter out known vocabulary before rendering a lesson. |
| `conversation engine` | **LOW** | Conversations remain static text. Tracking choices would just reference global IDs instead of local ones. |
| `Dexie schema` | **HIGH** | Requires a new `global_dictionary` table and a many-to-many relationship mapping scenarios to global dictionary IDs. |
| `certification pipeline` | **HIGH** | Audits must verify bidirectional coverage against the new global dictionary mapping, vastly increasing audit complexity. |

## Final Recommendation

Parla Italiano should migrate to a **Hybrid Mastery** architecture. 

**Why?**
The current Scenario Mastery model forces learners to redundantly master the same 2,000 common words across 116 scenarios, leading to massive pedagogical friction. However, moving *everything* (phrases and sentences) to a global model destroys situational context.

The Hybrid approach solves both:
1. **Global Vocabulary:** Build a `global_dictionary.json` and track single words globally.
2. **Contextual Application:** Keep phrases and sentences scenario-bound to test the application of that global vocabulary in real-world contexts.

This approach offers the most rewarding user experience (unlocking known words automatically) while preserving the high-quality, contextual immersion that Parla Italiano is built upon.
"""
    with open(report_path, "w", encoding="utf-8") as out:
        out.write(content)

def main():
    os.makedirs("reports", exist_ok=True)
    
    print("Analyzing Vocabulary...")
    vocab_items, total_vocab, unique_vocab = analyze_type("_vocabulary.json", "reports/global_vocabulary_analysis.md", "Global Vocabulary Analysis", limit=500)
    
    print("Analyzing Phrases...")
    analyze_type("_phrases.json", "reports/global_phrase_analysis.md", "Global Phrase Analysis", limit=100)
    
    print("Analyzing Sentences...")
    analyze_type("_sentences.json", "reports/global_sentence_analysis.md", "Global Sentence Analysis", limit=100)
    
    print("Generating Dictionary Prototype...")
    generate_dictionary_prototype(vocab_items)
    
    print("Generating Simulation...")
    generate_simulation(total_vocab, unique_vocab)
    
    print("Generating Recommendations...")
    generate_recommendations()
    
    print("Done.")

if __name__ == "__main__":
    main()
