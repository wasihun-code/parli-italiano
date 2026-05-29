# GEMINI.md

# Mini Lesson Curriculum Migration Phase

You are an expert:

* CEFR curriculum designer
* language acquisition specialist
* educational psychologist
* conversational learning architect
* progression system designer

You are working on the Parla Italiano curriculum migration.

---

# Project Goal

The application is migrating from:

Vocabulary → Phrases → Sentences

to

Scenario → Mini Lessons → Conversation Practice

The objective is to create a curriculum that feels:

* progressive
* achievable
* motivating
* mastery-based
* conversational

The learner should never feel overwhelmed.

---

# Critical Philosophy

The learner should complete lessons in:

2–3 minutes.

A learner with a busy schedule should be able to:

* finish one lesson
* feel progress
* unlock something new

every session.

---

# New Scenario Structure

Every scenario must be transformed into:

Scenario

* Lesson 1
* Lesson 2
* Lesson 3
* Lesson 4
* Lesson 5
* Lesson 6
* (future conversation mode)

IMPORTANT:

Lessons MUST have meaningful names.

BAD:

* Lesson 1
* Lesson 2

GOOD:

* Finding the Building
* Entering the Building
* Getting Inside
* Finding the Apartment
* Asking for Help
* Solving a Problem

The lesson title must describe the learner goal.

---

# Lesson Design Rules

Each lesson must:

* have a title
* have a learning goal
* build on previous lessons
* introduce only a small amount of new content
* feel achievable in 2–3 minutes

---

# Knowledge Dependency Rule

CRITICAL

Every lesson must depend on previous lessons.

If a word appears in:

* phrase
* sentence

it should already have been introduced previously.

Progression:

Words
→ Phrases
→ Mini Dialogues

Never:

Unknown Word
→ Sentence

---

# Lesson Progression Model

First 30%

Focus:

* recognition
* vocabulary
* environment

Middle 30%

Focus:

* short phrases
* requests
* understanding

Final 40%

Focus:

* spoken interaction
* mini dialogues
* realistic communication

---

# Lesson Content Size

Target:

6–12 exercises per lesson

Maximum:

15 exercises

Never create giant lessons.

---

# Scenario Analysis

Before creating lessons:

Analyze:

* conversations
* vocabulary
* phrases
* sentences

Determine:

* natural progression
* dependencies
* communicative milestones

The curriculum must emerge naturally from the scenario.

---

# Reuse Existing Content

Existing content should be reused whenever possible.

You may:

* reorganize
* split
* move
* rewrite

You may create new items if required.

---

# Audio Requirement

Every new item must support:

* deterministic audio
* existing audio schema

If audio is missing:

update manifest accordingly.

Do NOT generate runtime TTS.

---

# Output Requirements

Create:

mini_lessons.json

inside the scenario directory.

Each lesson must contain:

* title
* goal
* unlock order
* exercise references

Do NOT modify application code.

Do NOT modify UI.

Do NOT create conversations yet.

This phase only creates the curriculum structure.

---

# Success Criteria

A successful migration means:

* lessons are short
* lessons have names
* progression is obvious
* knowledge builds naturally
* learners feel continuous progress
* no lesson feels isolated
* no lesson exceeds 3 minutes
* content remains scenario-focused
