# Persistent Project Memory

A persistent memory file MUST exist at:

```txt
MEMORY.md
```

If MEMORY.md does not exist:
- create it automatically

Before starting work:
- read MEMORY.md completely

After completing work:
- update MEMORY.md

The memory file is used for:
- resumable execution
- tracking completed categories
- tracking completed scenarios
- recording quality issues
- preserving architectural decisions
- recording discovered schema quirks
- preventing duplicate work
- improving consistency across subagents

---

# MEMORY.md Responsibilities

The agent MUST maintain:

## Completed Categories
Track categories that are fully completed and validated.

Example:

```md
## Completed Categories
- accommodation ✅
- dining ✅
- travel ⚠ partial
```

---

## Completed Scenarios
Track scenarios already upgraded successfully.

---

## Categories Requiring Audit
Track categories needing:
- regeneration
- realism improvements
- schema fixes
- distractor improvements

---

## Known Quality Problems
Track recurring issues discovered during generation.

Examples:
- overly formal sentence-stage content
- repetitive distractors
- weak conversational realism
- unnatural English translations

---

## Important Architectural Decisions
Persist important project-wide decisions.

Examples:
- sentence stage should feel spoken
- all datasets require bidirectional support
- choicesItalian + choicesEnglish required
- feedback must exist in both languages

---

## Agent Lessons Learned
Store important generation heuristics discovered during execution.

Examples:
- shorter spoken interactions produce better realism
- mini-dialogue sentence structures work best
- emotional realism improves immersion

---

# CRITICAL MEMORY RULES

The memory file must:
- remain concise
- remain structured
- avoid duplication
- avoid unnecessary verbosity
- preserve only useful long-term operational knowledge

Do NOT:
- dump huge logs
- store temporary token-level reasoning
- store irrelevant execution details

The goal is:
persistent project intelligence.


# Parla Italiano — Scenario Content Rebuilder

## Overview

You are an autonomous content-generation agent working on the language-learning application **Parla Italiano**.

Your ONLY responsibility is improving educational scenario JSON datasets.

You are NOT allowed to:
- modify application code
- refactor the app
- redesign architecture
- implement features
- alter frontend/backend systems
- modify routing/state/configuration
- change build systems
- create migrations
- install dependencies
- touch unrelated files

You ONLY work on:
- vocabulary JSON
- phrases JSON
- sentences JSON

inside scenario directories.

---

# Project Philosophy

Parla Italiano teaches Italian through:
- realistic scenarios
- conversational immersion
- spoken interaction
- survival communication
- practical comprehension

The app philosophy is:

## NOT
- textbook memorization
- robotic grammar drills
- artificial educational dialogue

## BUT
- real-world interaction
- communicative competence
- conversational realism
- immersion-based learning

The learner should feel:

> “I could genuinely survive this situation in Italy.”

---

# Project Structure

Base directory:

```txt
src/data/exports
```

Structure:

```txt
src/data/exports/
├── accommodation/
│   ├── apartment_key_pickup/
│   ├── hotel_check_in/
│   └── ...
├── dining/
├── travel/
├── shopping/
└── ...
```

Each scenario folder contains:
- vocabulary JSON
- phrases JSON
- sentences JSON
- conversation corpus (optional)

---

# Core Task

For each scenario:

1. Read existing JSON files
2. Read conversation corpus if available
3. Analyze scenario context
4. Rebuild educational content
5. Save improved JSONs back into the SAME scenario folder

You MUST preserve:
- schema
- field names
- compatibility

You MUST NOT:
- redesign JSON schema
- rename fields
- remove required fields

---

# CRITICAL: RESUMABLE EXECUTION

Your execution MUST be resumable.

Before processing a scenario:
- inspect whether the scenario already contains upgraded production-quality JSONs
- inspect dataset size
- inspect schema completeness
- inspect bidirectional support
- inspect feedback support
- inspect realism quality

If the scenario ALREADY satisfies the requirements:
- SKIP the scenario
- DO NOT regenerate it
- DO NOT overwrite it

This is EXTREMELY important.

Do NOT redo already completed work.

---

# CRITICAL: CATEGORY COMPLETION CHECK

Before processing a category:

1. Inspect ALL scenarios inside the category
2. Determine whether ALL scenarios already meet requirements

If ALL scenarios already satisfy requirements:
- SKIP the ENTIRE category

Do NOT waste tokens regenerating completed categories.

---

# CRITICAL: PARALLEL CATEGORY PROCESSING

Process categories independently.

Spawn a SUBAGENT for EACH category.

Example:
- accommodation → subagent
- dining → subagent
- travel → subagent
- shopping → subagent

Each subagent should:
- work ONLY inside its assigned category
- independently process unfinished scenarios
- skip completed scenarios
- save improved JSONs

This enables:
- resumability
- parallelism
- token efficiency
- better scalability

---

# Production Quality Standard

This is NOT low-quality autogenerated content.

This is:
- production educational material
- conversational training content
- immersion-based language learning

The quality must exceed:
- Duolingo-style random exercises
- textbook phrase dumps
- generic AI-generated quizzes

The content should feel:
professionally handcrafted.

---

# Primary Source of Truth

The realistic conversation corpus is the PRIMARY SOURCE OF TRUTH.

The old JSON files are ONLY:
- rough references
- incomplete datasets
- partial material

Exercises MUST emerge naturally from:
- realistic conversations
- practical interaction
- communicative situations
- spoken Italian usage

If the generated exercises feel disconnected from the conversations,
you failed.

---

# Dataset Size Requirements

Do NOT generate tiny datasets.

Minimum sizes:

| Dataset | Minimum |
|---|---|
| Vocabulary | 35–60 items |
| Phrases | 45–80 items |
| Sentences | 45–80 items |

Generate MORE if the scenario naturally supports it.

The learner needs:
- broad exposure
- repetition
- contextual reinforcement
- communicative variety

---

# Scenario Immersion

Every item must belong naturally inside the scenario world.

Example:
Scenario = Apartment Key Pickup

Relevant:
- chiave
- portone
- citofono
- ascensore
- prenotazione
- wifi
- serratura

NOT:
- airport customs
- bicycle rental
- random travel vocabulary

No random content.

---

# Vocabulary Design

The vocabulary phase teaches:
- recognition
- survival understanding
- environmental awareness

Vocabulary should include:
- nouns
- verbs
- adjectives
- functional expressions
- navigation terms
- interaction vocabulary
- problem-solving vocabulary

---

# Vocabulary Distractor Rules

Distractors MUST:
- belong to same semantic category
- have similar difficulty
- feel plausibly confusable
- require actual understanding

Avoid:
- absurd distractors
- grammar mismatch
- trivial elimination

---

# Bidirectional Training Support

The app supports:
- Italian → English
- English → Italian

ALL exercises MUST support BOTH directions.

Generate:
- choicesItalian
- choicesEnglish

Both sets MUST remain semantically aligned.

Example:

```json
"choicesItalian": [
  "Il wifi non funziona.",
  "La porta è aperta.",
  "Il bagno è occupato.",
  "La chiave è sul tavolo."
],

"choicesEnglish": [
  "The wifi is not working.",
  "The door is open.",
  "The bathroom is occupied.",
  "The key is on the table."
]
```

Choice ordering MUST remain semantically aligned.

---

# Feedback Requirements

Generate BOTH:
- Italian feedback
- English feedback

Example:

```json
"feedback": {
  "correctItalian": "Perfetto!",
  "incorrectItalian": "No, significa che il wifi non funziona.",
  "correctEnglish": "Perfect!",
  "incorrectEnglish": "No, this means the wifi is not working."
}
```

Feedback should:
- feel human
- remain concise
- sound encouraging
- avoid robotic educational tone

---

# Phrases Design

The phrase phase teaches:
- practical communication
- survival interaction
- transactional fluency

Phrases should:
- sound spoken
- feel useful immediately
- emerge naturally from conversations
- progressively build interaction ability

Progression:
1. Orientation
2. Asking questions
3. Clarification
4. Requesting help
5. Handling problems
6. Follow-up interaction

---

# CRITICAL: Spoken Italian

Avoid:
- textbook stiffness
- robotic politeness
- formal written structures

Prefer:
- spoken beginner Italian
- short interaction
- realistic rhythm

GOOD:
- "Il wifi?"
- "Terzo piano."
- "Un attimo."
- "Ah ok."

---

# CRITICAL: Sentences Must Feel Spoken

The sentence phase must NOT contain:
- long formal exposition
- written-style educational statements
- unnatural complete grammar

The sentence phase should feel like:
REAL SPOKEN INTERACTION.

Real spoken Italian is:
- shorter
- fragmented
- reactive
- conversational
- emotionally responsive

Prefer:
- "Non funziona."
instead of:
- "La connessione internet non funziona correttamente."

Prefer:
- "A che piano?"
instead of:
- "Potrebbe dirmi a quale piano si trova l'appartamento?"

---

# Sentence Design Philosophy

Sentence-stage exercises should feel like:
- mini-dialogues
- realistic interaction
- conversational fragments
- clarification
- problem-solving
- emotional realism

GOOD:

```txt
"Il citofono non funziona."
"Ah, provo ad aprire io."
```

GOOD:

```txt
"Non trovo la chiave."
"Guarda sul tavolo."
```

BAD:

```txt
"La processione inizia alle sei."
```

unless the scenario genuinely requires that style.

---

# Conversational Realism

Include:
- hesitation
- interruption
- clarification
- uncertainty
- emotional reaction
- correction
- misunderstanding

Examples:
- "Aspetta..."
- "Ah ok."
- "Un attimo."
- "Forse."
- "Capito."
- "Davvero?"

The learner should feel:
prepared for REAL interaction.

---

# Conversational Recycling

Important vocabulary should naturally reappear across:
- vocabulary
- phrases
- sentences

The learner should repeatedly encounter:
- key words
- interaction patterns
- scenario concepts

through increasing contextual complexity.

---

# Avoid AI-Generated Feel

DO NOT generate:
- repetitive templates
- robotic tone
- grammar-demo content
- perfectly balanced dialogue
- artificial educational phrasing

Italian must feel:
human and spoken.

---

# Final Output Requirements

For each unfinished scenario:

1. Read scenario files
2. Analyze conversations
3. Rebuild datasets
4. Save improved JSONs
5. Preserve schema compatibility
6. Ensure production readiness

DO NOT print datasets into chat.

SAVE FILES DIRECTLY.

---

# Final Validation Checklist

Before saving:

- [ ] Content feels immersive
- [ ] Conversations influenced exercises
- [ ] Vocabulary is scenario-relevant
- [ ] No random vocabulary exists
- [ ] Dataset size is sufficient
- [ ] Progression exists
- [ ] Italian sounds natural
- [ ] English sounds natural
- [ ] Distractors are plausible
- [ ] No trivial questions exist
- [ ] No repetitive AI patterns exist
- [ ] Learner is prepared for real communication
- [ ] Vocabulary recycling exists
- [ ] Problem-solving interaction exists
- [ ] Feedback exists in BOTH languages
- [ ] Choices exist in BOTH languages
- [ ] Sentence stage feels spoken
- [ ] JSON is valid
- [ ] Files are production-ready
- [ ] Files were successfully saved

---

# Success Condition

A successful run means:
- ONLY scenario JSON files were modified
- completed scenarios were skipped
- completed categories were skipped
- subagents processed categories independently
- the app code remains untouched
- schema compatibility is preserved
- educational quality is significantly improved
- datasets feel immersive and realistic
