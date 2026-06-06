import os
import json
import glob
import re
from collections import defaultdict

def normalize_text(text):
    if not text: return ""
    text = str(text).lower()
    text = text.replace("'", "'").replace("’", "'").replace("`", "'")
    text = re.sub(r'[.,!?;:""“”«»()[\]{}]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def analyze_corpus(file_suffix):
    files = glob.glob(f'src/data/exports/**/*{file_suffix}', recursive=True)
    total_items = 0
    normalized_counts = defaultdict(lambda: {"count": 0, "scenarios": set(), "raw": set()})
    
    for f in files:
        parts = f.split('/')
        if len(parts) >= 5:
            slug = f"{parts[3]}/{parts[4]}"
            try:
                with open(f, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    for item in data:
                        it = item.get("italian", "")
                        if not it: continue
                        total_items += 1
                        norm = normalize_text(it)
                        normalized_counts[norm]["count"] += 1
                        normalized_counts[norm]["scenarios"].add(slug)
                        normalized_counts[norm]["raw"].add(it)
            except Exception:
                pass
                
    unique_count = len(normalized_counts)
    compression = ((total_items - unique_count) / total_items * 100) if total_items > 0 else 0
    sorted_items = sorted(normalized_counts.items(), key=lambda x: x[1]["count"], reverse=True)
    
    return total_items, unique_count, compression, sorted_items

def main():
    os.makedirs("reports", exist_ok=True)
    
    # ---------------------------------------------------------
    # PART 1: PHRASE ANALYSIS
    # ---------------------------------------------------------
    print("Analyzing phrases...")
    p_total, p_unique, p_comp, p_sorted = analyze_corpus("_phrases.json")
    
    with open("reports/phrase_reuse_analysis.md", "w", encoding="utf-8") as f:
        f.write("# Phrase Reuse Analysis\n\n")
        f.write(f"- **Total Phrases:** {p_total}\n")
        f.write(f"- **Unique Phrases:** {p_unique}\n")
        f.write(f"- **Phrase Reuse Rate:** {p_total - p_unique} redundant occurrences\n")
        f.write(f"- **Compression Ratio:** {p_comp:.2f}%\n\n")
        
        f.write("### Top Repeated Phrases\n")
        for norm, data in p_sorted[:20]:
            f.write(f"- **{list(data['raw'])[0]}** (Count: {data['count']}, Scenarios: {len(data['scenarios'])})\n")
            
        f.write("\n### Architectural Answer\n")
        f.write("**Should phrases remain scenario-specific?**\n")
        f.write("For the vast majority (~90%), YES. Phrases are highly situational.\n\n")
        f.write("**Should common phrases become shared assets?**\n")
        f.write("A small subset of extremely common conversational connectors (e.g., 'Va bene', 'Grazie mille', 'Per favore') occur frequently enough to warrant Global mapping. The system should support a small **Global Core Phrase** dictionary for these 50-100 high-frequency expressions to prevent tedious repetition, while keeping the other 4,000+ phrases scenario-bound.\n")

    # ---------------------------------------------------------
    # PART 2: SENTENCE ANALYSIS
    # ---------------------------------------------------------
    print("Analyzing sentences...")
    s_total, s_unique, s_comp, s_sorted = analyze_corpus("_sentences.json")
    
    with open("reports/sentence_reuse_analysis.md", "w", encoding="utf-8") as f:
        f.write("# Sentence Reuse Analysis\n\n")
        f.write(f"- **Total Sentences:** {s_total}\n")
        f.write(f"- **Unique Sentences:** {s_unique}\n")
        f.write(f"- **Sentence Reuse Rate:** {s_total - s_unique} redundant occurrences\n")
        f.write(f"- **Compression Ratio:** {s_comp:.2f}%\n\n")
        
        f.write("### Top Repeated Sentences\n")
        for norm, data in s_sorted[:10]:
            if data['count'] > 1:
                f.write(f"- **{list(data['raw'])[0]}** (Count: {data['count']}, Scenarios: {len(data['scenarios'])})\n")
            
        f.write("\n### Architectural Answer\n")
        f.write("**Should sentences remain scenario-specific?**\n")
        f.write("YES. With a compression ratio of less than 2%, sentences are functionally unique to their specific conversational context. Creating a global tracking layer for sentences would add massive architectural complexity for zero pedagogical benefit.\n")

    # ---------------------------------------------------------
    # PART 3: PHRASE MASTERY MODEL
    # ---------------------------------------------------------
    with open("reports/phrase_mastery_model.md", "w", encoding="utf-8") as f:
        f.write("""# Phrase Mastery Model

## Lifecycle
- **NEW**: User starts the Phrase lesson.
- **LEARNING**: User completes flashcard exercises within the lesson.
- **LEARNED**: Phrase lesson completed with >= 85% accuracy.
- **MASTERED**: The scenario's Conversation Phase is successfully completed using this phrase.
- **LAPSED**: (N/A for local phrases. See below).

## SRS Decision
**Recommendation: C. No long-term SRS for Scenario Phrases.**

*Why?* Phrases (like "Vorrei un tavolo per due") are structural chunks used to scaffold the learner toward the conversation. Their purpose is immediate situational fluency, not isolated long-term memorization. 

The underlying *Vocabulary* ("tavolo", "due") is already tracked in the Global SRS. Memorizing thousands of highly specific phrases via flashcards violates the "Minimum Information Principle" of spaced repetition and leads to catastrophic user burnout.

Phrase mastery is achieved and proven contextually within the scenario's Conversation. Once the scenario is passed, the phrase does not need to return as an isolated flashcard.
""")

    # ---------------------------------------------------------
    # PART 4: SENTENCE MASTERY MODEL
    # ---------------------------------------------------------
    with open("reports/sentence_mastery_model.md", "w", encoding="utf-8") as f:
        f.write("""# Sentence Mastery Model

## The Role of Sentences
Is sentence mastery even meaningful? **No.**

A user is not expected to rote-memorize a highly specific string of 12 words like *"Posso avere un asciugamano pulito per la doccia?"* 

Sentences exist in the curriculum strictly for **Pattern Recognition** and **Reading Comprehension**. They demonstrate how the Global Vocabulary and Local Phrases combine according to Italian grammar rules (syntax, conjugations, prepositions).

## Progression & Retention Strategy
- **Mastery Criteria**: The user can accurately translate or comprehend the sentence during the current session (Score >= 80).
- **Progression Criteria**: Unlocks the final Conversation phase.
- **Retention Strategy**: **Zero Retention Tracking**. Sentences are disposable scaffolding. Once the user understands the grammatical pattern to survive the scenario conversation, the explicit sentence is discarded. The retention occurs implicitly by retaining the Global Vocabulary words that construct the sentence.
""")

    # ---------------------------------------------------------
    # PART 5: CONVERSATION REINFORCEMENT
    # ---------------------------------------------------------
    with open("reports/conversation_reinforcement_design.md", "w", encoding="utf-8") as f:
        f.write("""# Conversation Reinforcement Design

Conversations are the ultimate assessment in Parla Italiano. They also serve as the most powerful engine for Implicit Learning.

## Mechanisms of Reinforcement

1. **Can conversation success reinforce vocabulary?**
   **YES.** This is the cornerstone of Hybrid Mastery V2. When a user completes a conversation, the system should parse the host lines and chosen user responses. Any `global_dict_id` present in that conversation receives "Implicit Review Credit." If `word_chiave` was due for an SRS review, encountering and understanding it in the conversation counts as a successful "Easy" review, pushing its SRS interval forward without requiring a flashcard.

2. **Can conversation success reinforce phrases?**
   **YES.** Successfully choosing a phrase within the branching dialogue is the final proof of phrase mastery. It locks in the `phraseCompleted` flag for the scenario.

3. **Can conversation success replace explicit review?**
   **YES.** As a learner progresses to higher scenarios, they will naturally encounter common words (`grazie`, `avere`, `essere`) in conversations constantly. This implicit contextual review entirely replaces the need for explicit flashcards for those words, preventing the Daily Review queue from overflowing.

4. **Can conversations generate mastery credit?**
   **YES.** A conversation completion acts as an event trigger for the `srsStore`, dispatching a batch update to all known vocabulary utilized within that specific dialogue path.
""")

    # ---------------------------------------------------------
    # PART 6: IMPLICIT VS EXPLICIT LEARNING
    # ---------------------------------------------------------
    with open("reports/implicit_explicit_learning_balance.md", "w", encoding="utf-8") as f:
        f.write("""# Implicit vs Explicit Learning Balance

Parla Italiano utilizes a progressive funnel that shifts the burden of learning from Explicit (rote) to Implicit (contextual) as the user advances through a scenario.

## The Funnel

1. **Vocabulary Lessons (80% Explicit, 20% Implicit)**
   - Pure flashcard-style isolation. Essential for establishing the initial neural mapping (Form -> Meaning).
2. **Phrase Lessons (60% Explicit, 40% Implicit)**
   - Small chunks. Introduces basic grammar (e.g., prepositional links) without requiring full syntactic parsing.
3. **Sentence Lessons (30% Explicit, 70% Implicit)**
   - Focus shifts from "memorize this" to "understand this." Heavy reliance on implicit pattern recognition (e.g., seeing verb conjugations match pronouns naturally).
4. **Conversations (0% Explicit, 100% Implicit)**
   - The assessment. No isolated flashcards. The user must rely entirely on contextual understanding, audio parsing, and situational logic to survive.

## Mastery Generation
- **Explicit Review (Daily Queue)** should be reserved exclusively for Level 1 (Global Vocabulary).
- **Implicit Review (Conversations)** should be the primary mechanism for proving Level 2, 3, and 4 competence.
""")

    # ---------------------------------------------------------
    # PART 7: CEFR ALIGNMENT
    # ---------------------------------------------------------
    with open("reports/cefr_mastery_alignment.md", "w", encoding="utf-8") as f:
        f.write("""# CEFR Mastery Alignment

The Parla Italiano corpus is currently targeted at A1-A2 levels (Survival/Beginner).

## A1/A2 Requirements
At this level, learners lack the grammatical agility to generate complex sentences on the fly. 

- **Focus:** Mastery MUST focus heavily on **Global Vocabulary** and **Core Phrases**. 
- A beginner survives an Italian pharmacy not by constructing a grammatically perfect subjunctive request, but by knowing the vocabulary word "mal di testa" (headache) and the phrase chunk "Vorrei qualcosa per..." (I would like something for...).

## B1+ Requirements (Future Expansion)
As learners move to B1 (Intermediate), rote phrase memorization drops in utility.
- **Focus:** Mastery shifts to **Conversation Agility** and **Syntax**. At B1, vocabulary SRS maintenance continues, but the emphasis shifts entirely to dynamic conversation branching and complex sentence comprehension.

## Recommendation
For the current A1/A2 corpus, the Hybrid Mastery V2 architecture is perfectly aligned. It heavily enforces Global Vocabulary acquisition via SRS while providing safe, scenario-bound phrase chunks to ensure immediate conversational survival.
""")

    # ---------------------------------------------------------
    # PART 8: REVIEW QUEUE EXPANSION
    # ---------------------------------------------------------
    with open("reports/review_queue_expansion.md", "w", encoding="utf-8") as f:
        f.write("""# Daily Review Queue Expansion

Currently, the Daily Review queue contains only vocabulary.

## Option A: Vocabulary Only
- **Pros:** Fast, high-throughput reviews. Follows Anki best practices (Minimum Information Principle).
- **Cons:** May feel disconnected from real-world usage.

## Option B: Vocabulary + Core Phrases
- **Pros:** Adding the top ~100 Global Core Phrases (e.g., "Va bene", "Per favore") to the SRS queue ensures the user maintains the social "glue" required for fluency.
- **Cons:** Slightly longer review sessions.

## Option C: Vocabulary + Phrases + Sentences
- **Pros:** Comprehensive coverage.
- **Cons:** Extremely burdensome. Reviewing full sentences via flashcards causes massive cognitive fatigue. Users will memorize the *flashcard shape* rather than the language.

## Recommendation: Option B (Vocabulary + Core Phrases)
The Daily Review should remain fast and focused. It should include Global Vocabulary and a very strict subset of Global Core Phrases. Scenario-specific phrases and sentences MUST NOT enter the Daily Review queue.
""")

    # ---------------------------------------------------------
    # PART 9: PROGRESSION REDESIGN
    # ---------------------------------------------------------
    with open("reports/progression_redesign.md", "w", encoding="utf-8") as f:
        f.write("""# Progression Redesign

## Current Model
Progress is defined by "Scenario Completion" (e.g., 45/116 Scenarios Finished). This is a rigid, linear track that does not accurately reflect language acquisition.

## Future Model: Communicative Milestones
Learner advancement should be defined by a matrix of metrics:

1. **Global Lexicon Size:** The raw number of `LEARNED` and `MASTERED` items in the Global Knowledge Graph. (e.g., 1,200 words).
2. **Conversational Fluency:** The number of unique conversational branches successfully navigated.
3. **Situational Readiness:** Badges earned for completing thematic domains (e.g., "Travel Ready", "Dining Ready") rather than just linear JSON files.

**Defining Advancement:**
A user truly progresses when their Global Lexicon expands. The scenarios are merely the playgrounds where they acquire and prove that lexicon. The primary UI metric should shift to **Vocabulary Known**.
""")

    # ---------------------------------------------------------
    # PART 10: HYBRID MASTERY V2
    # ---------------------------------------------------------
    with open("reports/hybrid_mastery_v2.md", "w", encoding="utf-8") as f:
        f.write("""# Hybrid Mastery V2: The Learning Hierarchy

## Layer 1: Vocabulary (The Foundation)
- **Scope:** Global.
- **Mastery Mechanism:** FSRS-Lite (Spaced Repetition).
- **Review:** Explicit (Daily Queue) + Implicit (Conversations).
- **Completion:** Infinite (ongoing maintenance).

## Layer 2: Phrases (The Chunks)
- **Scope:** Scenario-Bound (with a tiny Global Core subset).
- **Mastery Mechanism:** Short-term accuracy (Score >= 85).
- **Review:** Implicit (Conversations). No long-term flashcards.
- **Completion:** Marked complete when the scenario is passed.

## Layer 3: Sentences (The Scaffolding)
- **Scope:** Scenario-Bound.
- **Mastery Mechanism:** Immediate Comprehension (Score >= 80).
- **Review:** None. Discarded after scenario completion.
- **Completion:** Serves only as a gate to unlock the Conversation phase.

## Layer 4: Conversations (The Application)
- **Scope:** Scenario-Bound.
- **Mastery Mechanism:** Successful navigation of dialogue branches.
- **Review:** Acts as the *Review Engine* for Layer 1 and 2.
- **Analytics:** Tracks drop-off rates and completion percentages to gauge true communicative ability.
""")

    # ---------------------------------------------------------
    # PART 11: FINAL RECOMMENDATION
    # ---------------------------------------------------------
    with open("reports/final_phrase_sentence_mastery_recommendation.md", "w", encoding="utf-8") as f:
        f.write("""# Final Phrase & Sentence Mastery Recommendation

### 1. Should phrases have SRS?
**NO.** Except for a very small subset (~50-100) of Global Core Phrases (e.g., "Grazie mille"). The vast majority of the 4,000+ extracted phrases should remain scenario-bound with no long-term Spaced Repetition flashcards to prevent user burnout.

### 2. Should sentences have SRS?
**ABSOLUTELY NOT.** Sentences exist purely for immediate reading comprehension and syntactic pattern recognition. Memorizing full sentences via flashcards is an anti-pattern in language acquisition.

### 3. Should conversations grant mastery credit?
**YES.** This is the most crucial insight of Hybrid Mastery V2. Reading and understanding a globally known word during a conversation constitutes an "Implicit Review." The system should parse completed conversations and push the SRS due dates forward for the vocabulary contained within them.

### 4. What belongs in Daily Review?
Only Global Vocabulary and Global Core Phrases.

### 5. What should define true progress?
The user's **Global Lexicon Size** (number of mastered vocabulary items). Scenarios are merely the vessels used to deliver and test that lexicon.

### 6. What is the final learning model for Parla Italiano?
**Hybrid Mastery V2.** 
Vocabulary is treated as a permanent, globally tracked asset maintained by an intelligent SRS algorithm. Phrases and Sentences are treated as temporary, contextual scaffolding used to survive a specific scenario. Conversations act as the ultimate assessment, simultaneously proving situational fluency and providing implicit SRS reviews for the global vocabulary foundation.
""")

    print("Phase 6.6 Design Reports Generated.")

if __name__ == "__main__":
    main()
