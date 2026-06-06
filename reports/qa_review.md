# QA Review (Adversarial) — Phase 7.2

## 1. Systemic Data Loss: Tokenization Failures
The current `linguistic_extractor.py` uses a `len > 2` constraint.
- **Critical Risk:** This discards the most essential Italian words: `è`, `ho`, `il`, `la`, `un`, `io`, `di`, `in`, `su`, `ma`. These items MUST be tracked globally for a true proficiency model.
- **Fix:** Remove the length constraint.

## 2. Apostrophe & Elision Destruction
Tokenization splits elided forms (e.g., `l'ascensore` -> `ascensore`).
- **Critical Risk:** This loses article and gender context. Fragments like `dell'`, `nell'` are added as standalone words, creating grammatical noise.
- **Fix:** Update tokenization to treat elided articles as part of the noun or preserve the article state.

## 3. Collision & ID Hallucination
- **ASCII-only IDs:** Stripping non-ASCII characters causes collisions (e.g., `più` and `pi` both become `word_pi`).
- **Semantic Collisions:** Deterministic IDs fail to distinguish `visto` (seen) from `visto` (visa).
- **Mapping Hallucinations:** The corpus contains misaligned translations (e.g., `dieci` = "from the").
- **Fix:** IDs must support UTF-8 or use robust hashing. Mass cleanup of hallucinated translations is required.

## 4. Inefficient Phrase Strategy
Keeping all phrases scenario-bound causes massive redundancy for core units like `Per favore`, `Prego`, `Va bene`.
- **Recommendation:** Elevate the top ~100 core conversational phrases to the Global Dictionary.

## 5. Adversarial Conclusion
The Global Dictionary foundation is currently "leaky." Proceeding with the current tokenization logic will result in a dictionary missing 30% of the most frequent communicative units.
