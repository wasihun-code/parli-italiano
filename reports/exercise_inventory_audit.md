# Parla Italiano: Exercise Inventory Audit

## 1. Vocabulary Exercise Catalog

| Exercise Name | Mode | Screen | Trigger | Objective |
| :--- | :--- | :--- | :--- | :--- |
| **Flashcard** | Recognition | Vocab Screen | Attempt 0 | Primary introduction of IT/EN pair. |
| **Listening** | Recognition | Vocab Screen | Attempt 1 | Map spoken Italian to English text. |
| **Spelling** | Production | Vocab Screen | Attempt 2 | Produce Italian spelling from English/Audio. |
| **Multiple Choice**| Recognition | Vocab Screen | Attempt 3+ | Final recognition check (EN -> IT). |

## 2. Phrase Exercise Catalog

| Exercise Name | Mode | Screen | Trigger | Objective |
| :--- | :--- | :--- | :--- | :--- |
| **Multiple Choice**| Recognition | Phrase Screen | Attempt 0 | Identify phrase from English prompt. |
| **Assembly** | Recall | Phrase Screen | Attempt 1 | Order scrambled words to build phrase. |
| **Fill in the Blank**| Recall | Phrase Screen | Attempt 2 | Identify missing word in Italian context. |
| **Dictation** | Production | Phrase Screen | Attempt 3 | Transcribe audio of the full phrase. |
| **Speaking** | Production | Phrase Screen | Attempt 4 | Voice-to-text pronunciation check. |

## 3. Sentence Exercise Catalog

| Exercise Name | Mode | Screen | Trigger | Objective |
| :--- | :--- | :--- | :--- | :--- |
| **Dictation** | Production | Sentence Screen| Index % 3 == 0| Transcribe complex audio. |
| **Translation** | Production | Sentence Screen| Index % 3 == 1| Write Italian sentence from English. |
| **Completion** | Recall | Sentence Screen| Index % 3 == 2| Fill in complex syntactic gaps. |

## 4. Mini Lesson (Global) Inventory

| Exercise Name | Mode | Screen | Trigger | Objective |
| :--- | :--- | :--- | :--- | :--- |
| **Rapid Recognition**| Recognition | MiniLesson Screen| Constant | Match Italian text to English (Multiple Choice). |

**Note:** The `MiniLessonTrainingScreen` currently only utilizes Multiple Choice (Recognition) for all items (Vocab, Phrase, and Sentence), ignoring the specialized modes of the individual screens.

## 5. Summary Typology

| Category | Percentage (Approx) | Dominant Screen |
| :--- | :--- | :--- |
| **Recognition** | **85%** | Mini Lessons, Vocab Phase 1/2 |
| **Recall** | **10%** | Assembly, Fill-Blank |
| **Production** | **5%** | Spelling, Dictation, Speaking |

## 6. Audit Finding: The "Production Cliff"

The system follows a "Production Cliff" design:
1.  Learners spend **90% of their time** in the Recognition/Recall phase during Mini Lessons.
2.  The **Production** phase (Writing/Speaking) is sequestered in specialized screens that are often bypassed or reached only after high friction.
3.  The **Conversation** is entirely recognition-based (Multiple Choice), meaning a learner can "Master" the entire 116-scenario course without ever being required to type a single unique Italian sentence from scratch.
