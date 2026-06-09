## Audit Inventory

| # | Audit Name | Purpose |
|---|---|---|
| A01 | **Dependency Audit** | Ensures every entity in the lesson only depends on entities that are already introduced (within earlier micro‑lessons or earlier in the same lesson). Detects forward references and missing prerequisites. |
| A02 | **Coverage Audit** | Verifies that all dependencies declared by the lesson’s entities exist in the global registries (words, phrases, sentences). No unresolved references. |
| A03 | **Duplicate Introduction Audit** | Guarantees every word, phrase, sentence, and turn has exactly one introduction point across the entire curriculum. Re‑introductions (excluding reviews) are illegal. |
| A04 | **Lesson Flow Audit** | Checks that the lesson’s internal ordering respects the Word → Phrase → Sentence → Turn hierarchy. No phrase appears before its words, no sentence before its phrases, etc. |
| A05 | **State Machine Audit** | Validates that the current learner state permits the introduction of each new entity. Dependent words/phrases must be at least PRACTICED before the lesson can introduce higher‑level items. |
| A06 | **Conversation Readiness Audit** | Ensures every conversation turn in the lesson is fully reachable: all its prerequisite sentences exist and are in a state that allows turn practice, and the turn pair (host+user) can be completed without dead‑ends. |
| A07 | **Exercise Eligibility Audit** | Run immediately before generating a specific exercise. Verifies that the target entity is in a state that allows that exercise type, and that all required prerequisites are satisfied. |

---

## Audit Definitions and Validation Rules

Each audit is described with:
- **Inputs**
- **Validation logic**
- **Pass conditions**
- **Failure conditions**

---

### A01 – Dependency Audit

**Goal**  
Prevent “untaught content” – an entity cannot be introduced before all its direct dependencies are known.

**Inputs**  
- The micro‑lesson definition: list of new words, new phrases, new sentences, new turns.
- The global dependency graph (Dependency Graph from Phase 2): `depends_on_words`, `depends_on_phrases` for each phrase; `depends_on_words`, `depends_on_phrases` for each sentence; `depends_on_sentences` for each turn.
- The cumulative set of entities already introduced in all previous micro‑lessons, plus entities introduced earlier in the current micro‑lesson.

**Validation Logic**  
For every new entity `E` being introduced in the current lesson (ordered by the lesson’s own sequence of introduction):
1. Determine all direct dependencies:
   - if `E` is a word → no dependencies (words are atomic).
   - if `E` is a phrase → `depends_on_words` (list of word IDs).
   - if `E` is a sentence → `depends_on_words` ∪ `depends_on_phrases`.
   - if `E` is a turn → the sentence ID it instantiates (`depends_on_sentences`).
2. For each dependency `D`, verify that `D` is **already introduced** – i.e., it belongs to the set of entities that have been introduced before `E` in the curriculum timeline (this includes all entities from previous micro‑lessons, and all entities introduced in the current micro‑lesson whose introduction order is before `E`).
3. The verification respects the order of introduction within the micro‑lesson as defined by the lesson plan (the curriculum defines which item is introduced first, second, etc.).

**Pass Condition**  
All dependencies of every new entity are satisfied by previously introduced entities. No forward references.

**Failure Condition**  
Any dependency of a new entity is not yet introduced. Example:
- The lesson attempts to introduce phrase `p_000004` (hai il codice) before the word `w_000012` (codice) has been introduced (even if in the same lesson, if the phrase is introduced before the word, it fails).
- The lesson introduces a turn whose sentence has not been introduced yet.

---

### A02 – Coverage Audit

**Goal**  
Ensure that every dependency ID referenced by a lesson’s entities actually exists in the global registries. This catches typos, missing records, or broken references from the Knowledge Graph.

**Inputs**  
- All new entities of the micro‑lesson.
- Global Word Registry (all known word IDs).
- Global Phrase Registry.
- Global Sentence Registry.
- The dependency fields of each entity.

**Validation Logic**  
For each new entity, resolve every dependency ID against the appropriate global registry:
- For a phrase’s `depends_on_words`, check each word ID exists in the global Word Registry.
- For a sentence’s `depends_on_words` and `depends_on_phrases`, check existence.
- For a turn’s `depends_on_sentences`, check the sentence ID exists.

**Pass Condition**  
All referenced dependency IDs are found in the corresponding global registries. No dangling references.

**Failure Condition**  
Any dependency ID is not present in the global registry. Example:
- A sentence `s_099` (not defined) is listed as a dependency of a turn.
- A word ID `w_99999` is referenced by a phrase but does not exist.

---

### A03 – Duplicate Introduction Audit

**Goal**  
Each entity (word, phrase, sentence, turn) must be introduced exactly once. This audit prevents re‑introductions that would confuse the learning state machine and waste exercise generation.

**Inputs**  
- The entity (word, phrase, sentence, turn) proposed for introduction.
- The full set of all previously introduced entities across the entire curriculum (recorded in the system’s “introduced” log).

**Validation Logic**  
For each new entity in the lesson, query the curriculum history:
- If the entity ID already has a recorded introduction timestamp (i.e., it has been introduced before), the lesson fails.
- **Reviews are not introductions.** The check only applies when an entity is flagged as “new” in the micro‑lesson. Review exercises are not subject to this audit.

**Pass Condition**  
Every new entity in the lesson is unique and has never been introduced before.

**Failure Condition**  
Any entity ID that already appears in the introduced set. Example:
- The word `w_000001` (ciao) is already introduced in micro‑lesson 1, but the current lesson again lists it as a “new word”.

---

### A04 – Lesson Flow Audit

**Goal**  
Verify that the micro‑lesson’s internal structure respects the hierarchical progression: all words must be introduced before the phrases that use them (within the lesson), all phrases before sentences, all sentences before turns.

**Inputs**  
- The micro‑lesson’s internal teaching sequence: ordered list of introduction events (word X, phrase Y, sentence Z, turn T) with explicit ordering.
- Dependency relationships as per global graph (which words a phrase needs, etc.).

**Validation Logic**  
1. Partition the micro‑lesson’s introduction events by type and order.
2. For each phrase being introduced in the lesson, ensure that **all** its dependent words appear earlier in the same lesson’s introduction order, OR have been introduced in previous lessons (covered by A01). But the flow audit specifically checks the within‑lesson ordering: a phrase must not be introduced before any of its dependent words that are also part of the current lesson.
3. Similarly for sentences: all dependent phrases that are new in this lesson must be introduced earlier in the lesson sequence.
4. For turns: the corresponding sentence must be introduced earlier in the lesson (or already known).

**Pass Condition**  
The sequence respects word‑before‑phrase, phrase‑before‑sentence, sentence‑before‑turn for all new dependencies within the same lesson.

**Failure Condition**  
A phrase appears in the lesson flow before one of its dependent words (also new in this lesson). Example:
- The lesson introduces the phrase `p_000001` (piacere di conoscerti) at step 2, but the word `w_000002` (piacere) is introduced at step 5 – out of order.

---

### A05 – State Machine Audit

**Goal**  
Ensure that the learner’s current state allows the introduction of each new entity. Dependent entities must be at least in the PRACTICED state before the lesson can introduce a higher‑level entity that depends on them.

**Inputs**  
- Learner’s state model: for each entity the system knows, its current state (UNSEEN, INTRODUCED, PRACTICED, MASTERED, FORGOTTEN) and mastery score.
- The micro‑lesson’s list of new entities and their dependencies.
- The dependency graph.

**Validation Logic**  
For each new entity `E` to be introduced:
1. Identify all its prerequisites (as per dependency graph).
2. For each prerequisite, check that its state is at least **PRACTICED** (mastery ≥ 0.70) and that it is **not FORGOTTEN**.
3. If any prerequisite is UNSEEN, INTRODUCED (but not yet PRACTICED), or FORGOTTEN, the lesson fails.
4. Exception: words have no prerequisites, so always pass.

**Pass Condition**  
All prerequisites of every new entity are in PRACTICED or MASTERED state (and not FORGOTTEN).

**Failure Condition**  
A prerequisite is not sufficiently learned. Example:
- The lesson tries to introduce a phrase that requires the word `w_000012` (codice), but the learner’s `w_000012` is still INTRODUCED (not yet practiced). The audit blocks the phrase introduction.

---

### A06 – Conversation Readiness Audit

**Goal**  
Verify that every conversation turn in the lesson can be fully practiced: the turn’s sentence is reachable, the complementary turn exists (for the pair), and no dead‑end blocks scenario completion.

**Inputs**  
- The micro‑lesson’s conversation turns (host and user).
- The global turn registry (pairs are defined by consecutive turns in a scenario).
- State of the underlying sentences (must be at least PRACTICED to allow turn practice – this is partly covered by A05, but also needs to check the pairing for Conversation exercise readiness).

**Validation Logic**  
1. For each turn in the lesson, confirm that its corresponding sentence is already introduced and PRACTICED (already validated by A05).  
2. Check that the complementary turn (the other half of the exchange) is either already introduced (from previous lessons) or is also present in the current lesson and will be introduced before the Conversation exercise is attempted.  
3. Verify that there is a valid scenario plan such that all turns in the lesson belong to a sequence that can be completed (no isolated turn without a partner).  
4. Ensure no turn requires a sentence that is missing or in a lower state (redundant with A05, but double‑checked).  
5. (Optional) Check that the conversation flow graph for the scenario is fully connected – no dead‑ends where the learner cannot progress because a turn is not defined.

**Pass Condition**  
Every turn has its complementary turn defined and reachable, the underlying sentences are PRACTICED, and the scenario segment can be completed.

**Failure Condition**  
A host turn is introduced but the corresponding user turn is missing from the curriculum (or vice‑versa), making the pair unpracticeable. Or a turn’s sentence is not PRACTICED. Example:  
- Micro‑lesson adds only turn `t_000003` (host) but does not include the user response `t_000004` anywhere (even from prior lessons) – Conversation exercise would be impossible.

---

### A07 – Exercise Eligibility Audit

**Goal**  
Immediately before generating an exercise for a specific entity, verify that:
- The target entity is in a state that permits that type of exercise.
- Any prerequisites for that exercise type are met (e.g., to generate a Recall exercise for a phrase, the phrase must have been introduced and certain earlier exercises completed).

**Inputs**  
- Target entity ID and type (word/phrase/sentence/turn).
- Requested exercise type (Listen, ListenChoose, Match, Recall, Spelling, Assembly, BuildSentence, Dictation, Speaking, Conversation, etc.).
- Learner’s state for that entity (state, which exercises have been completed, mastery score).
- The defined learning flow for that entity type (what exercises can be generated at each stage).

**Validation Logic**  
Using the Learning Flow Design (Phase 3.5) as reference, the system maps the entity state to allowed exercises:

| Entity State | Allowed Exercises (progressive) |
|--------------|----------------------------------|
| UNSEEN       | Listen (first exposure) only. |
| INTRODUCED   | ListenChoose, Match, (and the next in sequence according to flow) – but only if the prerequisites in the flow are met (e.g., can't generate Recall before ListenChoose is completed). |
| PRACTICED    | Recall, Assembly (phrase), BuildSentence (sentence), Dictation (sentence), Speaking, etc. depending on flow. Also Conversation for turns. |
| MASTERED     | Review exercises only (Match, ListenChoose, Recall). No introductory exercises. |
| FORGOTTEN    | Re‑introduction exercise (Listen then Recall) only. |

Additionally, specific exercise‑type prerequisites:
- **Phrase: BuildSentence** is not allowed; BuildSentence is for sentences. The exercise type must be compatible with entity type.
- **Word: Speaking** may be allowed but only after Recall and Spelling are completed.
- **Turn: Conversation** requires both turns of the pair to be at least INTRODUCED and the sentences PRACTICED.

The audit checks:
1. Entity state → is the requested exercise in the allowed set for that state?
2. Entity type → exercise type compatibility (e.g., Dictation is only valid for sentences; Assembly only for phrases; BuildSentence only for sentences; Speaking for any but with prerequisites).
3. Exercise sequence integrity: has the learner completed all earlier exercises in the flow for that entity? For example, if requesting Recall for a word, the system checks that the word has passed ListenChoose and Match (or that the previous steps are marked complete).

**Pass Condition**  
All checks pass: entity state allows the exercise, type compatibility holds, all sequential prerequisites satisfied.

**Failure Condition**  
Any check fails. Example:
- Requesting a Recall exercise for a word that is still UNSEEN → blocked.
- Requesting Dictation for a phrase (invalid type).
- Requesting BuildSentence for a sentence whose phrase prerequisites are not yet PRACTICED (state machine) – this would be caught by A05, but if the sentence is allowed but the earlier exercises in the sentence learning flow aren't done, it fails.
- Requesting a Conversation exercise for a turn whose paired turn is not yet introduced.

---

## Failure Examples (Concrete)

### Dependency Audit Failure
- Micro‑lesson 5 introduces phrase `p_000007` (premi il tasto chiave) at step 1, but the word `w_000018` (tasto) is scheduled for introduction at step 3. The audit detects forward reference → **Blocked**.

### Coverage Audit Failure
- The lesson defines a turn that depends on sentence `s_099`, but that ID does not exist in the sentence registry. → **Error: missing sentence reference**.

### Duplicate Introduction Failure
- The curriculum attempted to reintroduce word `w_000001` (ciao) as a “new word” in lesson 10, even though it was already introduced in lesson 1. → **Duplicate blocked**.

### Lesson Flow Failure
- In a single micro‑lesson, the plan teaches sentence `s_000003` (host message) before introducing its dependent phrase `p_000003` (il portone è chiuso) – the flow is inverted. → **Audit fails**.

### State Machine Failure
- Learner has not yet practiced word `w_000025` (porta) – it is still INTRODUCED. The lesson wants to introduce phrase `p_000020` (vedi la porta B) which depends on that word. The state machine audit blocks because the prerequisite is not PRACTICED. → **Generation blocked until the word is practiced**.

### Conversation Readiness Failure
- The lesson includes host turn `t_000025` but the corresponding user turn `t_000026` is not scheduled anywhere in the curriculum, leaving the host turn without a reply. Conversation practice cannot be built. → **Audit fails**.

### Exercise Eligibility Failure
- Request: generate a **Speaking** exercise for word `w_000012` (codice), but the word is only in INTRODUCED state (has not yet completed Recall/Spelling). Speaking requires at least PRACTICED state. → **Blocked**.

---

## Pass Examples (Concrete)

### Dependency Audit Pass
- All new entities in the lesson only reference dependencies that were introduced in earlier micro‑lessons or are placed earlier in the current lesson’s sequence. No forward references.

### Coverage Audit Pass
- Every dependency ID in the lesson points to a valid entry in the global word, phrase, or sentence registry.

### Duplicate Introduction Pass
- All words, phrases, sentences, and turns in the lesson are being introduced for the first time in the entire curriculum.

### Lesson Flow Pass
- The lesson introduces words first, then the phrases built from those words, then sentences, then turns, exactly matching the dependency order.

### State Machine Pass
- For every phrase introduced, all its required words are PRACTICED. For every sentence, all required words and phrases are PRACTICED. The learner’s state matches this before the lesson is certified.

### Conversation Readiness Pass
- Every turn in the lesson has its complementary turn already introduced or present in the same lesson, and all underlying sentences are PRACTICED.

### Exercise Eligibility Pass
- Request: **Recall** exercise for phrase `p_000001` (piacere di conoscerti) when the phrase is in PRACTICED state and all earlier exercises (Listen, ListenChoose, Match, Assembly) are completed → allowed.

---

## Certification Pipeline (Deterministic)

The pipeline runs **before any exercise generation** for a given micro‑lesson. If all stages pass, the lesson is certified, and exercise generation may proceed. Otherwise, the entire lesson is blocked until errors are fixed.

**Order of execution (strict):**

1. **Coverage Audit** – quickest; catches broken references.
2. **Duplicate Introduction Audit** – catches re‑introduction mistakes.
3. **Dependency Audit** – verifies prerequisite ordering across the curriculum.
4. **Lesson Flow Audit** – verifies within‑lesson ordering.
5. **State Machine Audit** – learner‑state dependent; must be last of structural checks.
6. **Conversation Readiness Audit** – depends on state of sentences/turns.

Only after these six audits all return **PASS**, the lesson is marked “structurally valid and learner‑ready.” At that point, the system may begin generating exercises.

**Exercise generation phase:**
For each exercise request that follows, the system runs:
7. **Exercise Eligibility Audit** – per‑entity, per‑exercise. If it fails, that specific exercise is not generated (and may be queued for later when prerequisites are met). A failure here does **not** invalidate the whole lesson; it only defers the exercise.

Thus, the final “Generation Allowed” is a two‑stage gate:
- Lesson‑level verification (steps 1‑6) must all pass.
- Individual exercise requests must pass step 7.

---

## Final Release Criteria

For the entire verification system to be deployed into production, the following must hold:

- All audits are implemented as deterministic, stateless functions (except A05/A06 which read learner state).
- The global registries (words, phrases, sentences, turns) are locked and versioned – no changes allowed without re‑certification of all lessons.
- Every micro‑lesson in the curriculum has passed audits 1‑6 with the exact registry version in use.
- A monitoring dashboard shows audit results for each lesson; any regression (e.g., due to registry update) automatically blocks exercise generation until corrected.
- The exercise eligibility audit (A07) is integrated into the exercise generation API as a pre‑check. No exercise can be generated without a PASS.
- All failure reasons are logged with clear messages for content authors to fix.
- The system must never allow an exercise to be generated for a lesson that failed any of A01‑A06.

---

**End of Verification System Design**
