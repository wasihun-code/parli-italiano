# Distractor Generation Rules

## Core Goal
Distractors must force the learner to actually read and understand the Italian options. They cannot be easily guessed by length, formatting, or obvious irrelevance.

## Rules
1.  **Count:** Every choice array MUST contain 3 to 4 items (1 correct, 2-3 distractors).
2.  **No Placeholders:** Never use words like "Distractor 1", "Placeholder", or empty strings.
3.  **No Duplicates:** The array of choices must contain only unique strings (case-insensitive).
4.  **Length Matching:** Distractors must be of similar length to the correct answer. A good rule of thumb is +/- 40% character length.
    *   *BAD:* Correct: "Sì." | Distractors: "Vorrei prenotare un tavolo per due persone."
    *   *GOOD:* Correct: "Sì, grazie." | Distractors: "No, grazie.", "Per favore.", "Scusi."
5.  **Domain Consistency:** Distractors MUST belong to the same topic/scenario. Do not mix airport vocabulary into an apartment scenario.
6.  **Grammatical Consistency:** If the correct answer is a verb, distractors should be verbs. If it's a noun, distractors should be nouns.
7.  **Plausibility:** Distractors should be linguistically plausible but contextually wrong.

## Example (Apartment Scenario)
**Host:** "Sei davanti al palazzo?"
**Correct Answer:** "Sì, sono davanti al portone."
**Valid Distractors:** "No, sono al secondo piano.", "Sì, ho le chiavi.", "Dov'è il portone?"
**Invalid Distractors:** "Il caffè è caldo." (Off-domain), "Sì." (Too short), "Distractor 1" (Placeholder).
