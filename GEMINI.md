# Parla Italiano — Corpus & Audio Infrastructure Specification

# Overview

Parla Italiano is a production-grade immersive Italian learning platform focused on:
- survival communication
- realistic spoken interaction
- conversational immersion
- practical Italian
- offline-first learning

The platform uses:
- deterministic educational corpora
- reusable audio assets
- resumable infrastructure
- stabilization-oriented workflows
- production-grade validation systems

The learner should feel:
“I could genuinely survive this interaction in Italy.”

---

# Core Philosophy

The app must feel like:
REAL PEOPLE SPEAKING REAL ITALIAN.

NOT:
- robotic educational content
- textbook grammar exposition
- disconnected phrase dumps
- unnatural AI dialogue
- grammar-demo sentences

BUT:
- spoken mini-dialogues
- interruptions
- emotional realism
- uncertainty
- reactive communication
- practical survival interaction

The corpus is now considered:
PRODUCTION-STABILIZED.

Avoid:
- uncontrolled rewrites
- mass regeneration
- destabilizing modifications

Prefer:
- deterministic upgrades
- surgical fixes
- validation-first workflows
- infrastructure stabilization

---

# Repository Scope Restrictions

You MAY modify:
- corpus JSON files
- audio manifests
- audio infrastructure tooling
- validation tooling
- MEMORY.md
- synthesis scripts

You MAY NOT:
- redesign frontend
- refactor backend
- alter routing
- modify application architecture
- redesign state management
- rewrite unrelated source files
- perform destructive repo-wide rewrites

---

# Corpus Architecture

Base corpus directory:

```txt
src/data/exports
```

Each scenario may contain:
- vocabulary JSON
- phrases JSON
- sentences JSON
- conversations.txt
- future audio metadata

---

# Corpus Lifecycle

Each category progresses through:

1. Audit
2. Generation
3. Validation
4. Repair
5. Stabilization
6. Locked/Completed

Never mark categories completed before:
- JSON validation
- schema validation
- realism validation
- consistency validation
- audio validation (when applicable)

---

# Conversational Standards

Italian must feel:
- spoken
- compressed
- reactive
- emotionally believable
- conversational

Avoid:
- textbook stiffness
- overly formal written rhythm
- narration-heavy structures
- exposition-heavy dialogue

Sentence-stage content should resemble:
- mini-dialogues
- clarification
- interruptions
- uncertainty
- emotional realism
- practical interaction

---

# Bidirectional Training Requirements

All production datasets must support:
- Italian → English
- English → Italian

Every exercise should support:
- choicesItalian
- choicesEnglish

Choices must remain semantically aligned.

---

# Feedback Requirements

Production schema:

```json
"feedback": {
  "correctItalian": "...",
  "incorrectItalian": "...",
  "correctEnglish": "...",
  "incorrectEnglish": "..."
}
```

Feedback should:
- sound human
- remain concise
- encourage immersion
- avoid robotic educational tone

---

# ID Requirements

All corpus entries must contain:
- deterministic IDs
- unique IDs within datasets

Preferred structure:

```txt
travel_airport_arrival_s042
```

Avoid:
- unstable numbering
- duplicate identifiers
- random IDs

IDs are critical for:
- SRS
- analytics
- progress tracking
- audio mapping
- migrations

---

# Audio Infrastructure

The platform supports:
- deterministic reusable audio generation
- offline-first delivery
- resumable synthesis workflows
- future persona systems
- future premium voice packs
- future local TTS engines

---

# CRITICAL AUDIO RULE

Generate audio:
PER UNIQUE ITALIAN TEXT + VOICE COMBINATION,
NOT per exercise.

If the same Italian text appears:
- across categories
- across games
- across review systems

the SAME audio asset should be reused IF:
- the voice is identical

Different voices MUST generate different assets.

---

# Future-Safe Audio Hashing

Audio hashing must support:
- persona systems
- premium voices
- regeneration workflows
- voice replacement

Preferred strategy:

```txt
sha1(normalized_text + voice_id)
```

Example:
- "Un attimo." + Elsa
- "Un attimo." + Diego

must generate DIFFERENT audio assets.

Avoid:
- text-only hashing for future systems.

Current default voice:
- it-IT-ElsaNeural

---

# Audio Format

Preferred production format:
- .opus

Reasons:
- excellent speech compression
- ideal for PWAs
- smaller offline footprint
- excellent streaming behavior

Avoid:
- wav in production
- duplicate mp3 storage

---

# Audio Storage

Store audio inside:

```txt
public/audio/
```

Use:
- flat hash-based structure

GOOD:

```txt
public/audio/7cc91a.opus
```

BAD:

```txt
public/audio/travel/airport/file.mp3
```

---

# Audio Schema

Exercises should support:

```json
"audio": {
  "italian": "/audio/7cc91a.opus"
}
```

Preserve compatibility across:
- vocabulary
- phrases
- sentences

---

# Audio Manifest System

The pipeline must support:
- manifest generation
- resumable synthesis
- regeneration workflows
- missing-audio detection
- validation tooling

Manifest responsibilities:
- extract unique Italian text
- deduplicate globally
- map text + voice → deterministic hash
- track generation state

---

# Manifest Scalability

Large-scale manifests should eventually support:
- sharded manifests
- category manifests
- incremental updates
- resumable synchronization

Avoid:
- repeatedly rewriting extremely large monolithic manifests

Preferred future structure:

```txt
public/audio/manifests/
```

Examples:
- travel_manifest.json
- dining_manifest.json
- shard_001.json

Current single-manifest architecture is acceptable during stabilization.

---

# Audio Workflow

Preferred workflow:

JSON corpus
→ extract text
→ deduplicate
→ generate manifests
→ synthesize audio
→ validate audio
→ inject paths
→ validate corpus

Avoid:
- manual scenario-by-scenario synthesis
- duplicate generation
- uncontrolled regeneration

---

# Current Audio Engine

Current engine:
- Edge-TTS

Current preferred voice:
- it-IT-ElsaNeural

Architecture must remain flexible enough to support:
- premium voices
- local engines
- persona systems
- downloadable packs
- slow-speed variants

without destabilizing corpus structure.

---

# Edge-TTS Safety Rules

Edge-TTS uses remote Microsoft speech services.

Therefore the pipeline MUST behave conservatively.

Prioritize:
- reliability
- resumability
- stability

over:
- maximum throughput

---

# Audio Generation Constraints

The synthesis pipeline MUST include:
- randomized delays
- retry logic
- resumable execution
- skip-existing behavior
- failure logging
- controlled concurrency

---

# Concurrency Limits

Recommended:
- 2–4 concurrent workers

Avoid:
- aggressive parallelism
- uncontrolled bursts

---

# Delay Strategy

Use randomized delays:

Recommended:
- 300ms–1000ms

Example:

```python
await asyncio.sleep(random.uniform(0.3, 1.0))
```

This reduces:
- throttling
- temporary blocking
- instability

---

# Retry Strategy

The pipeline must:
- retry failures
- use exponential backoff
- log failures persistently

Recommended:
- 3–5 retries

---

# Resumable Generation

Audio generation MUST:
- skip existing files
- preserve completed assets
- survive interruptions
- resume safely

Treat synthesis as:
a resumable build pipeline.

---

# Audio Normalization Requirements

Audio consistency is critical for immersion.

The synthesis pipeline should eventually support:
- loudness normalization
- silence trimming
- consistent bitrate
- playback consistency
- conversational pacing consistency

Future normalization may include:
- ffmpeg loudnorm
- silence removal
- opus optimization

Avoid:
- inconsistent loudness
- long silence
- abrupt clipping
- inconsistent pacing

Audio UX consistency is more important than:
- maximum synthesis speed.

---

# Validation Requirements

Validation must include:
- JSON integrity
- schema consistency
- missing audio
- broken paths
- invalid manifests
- invalid filenames
- duplicate IDs
- missing IDs
- bidirectional alignment

---

# Conversational Audio QA

Audio validation must include:
- pronunciation realism
- pacing comfort
- listening fatigue evaluation
- emotional realism
- conversational flow
- speaker consistency

Validation is NOT limited to:
- file existence
- synthesis completion
- manifest integrity

Immersion quality is a primary production concern.

---

# Conversational Persona Audio System

The platform supports:
- role-aware immersion
- controlled multi-speaker synthesis
- conversational speaker consistency

This exists ONLY to improve:
- realism
- immersion
- listening quality
- scenario authenticity

NOT:
- random novelty
- chaotic speaker switching
- uncontrolled variation

---

# CRITICAL PERSONA RULE

Voices must be assigned:
BY ROLE,
NOT randomly.

GOOD:
- waiter → consistent waiter voice
- receptionist → consistent receptionist voice
- traveler → consistent traveler voice

BAD:
- arbitrary voice changes
- inconsistent role identity
- random gender switching

---

# Persona Usage Guidelines

## Vocabulary Stage
Use:
- single consistent voice

Reason:
- pronunciation consistency
- learner familiarity
- lower cognitive load

Avoid:
- multi-speaker vocabulary synthesis

---

# Phrase Stage

Prefer:
- mostly single voice

Avoid:
- excessive switching

---

# Sentence Stage

Sentence-stage mini-dialogues MAY support:
- role-based personas
- conversational differentiation
- immersive dialogue synthesis

This is the PRIMARY layer where personas provide educational value.

---

# Current Recommended Voice Strategy

| Layer | Voice Strategy |
|---|---|
| Vocabulary | single voice |
| Phrases | mostly single voice |
| Sentences | role-based personas |
| AI Tutor | dedicated unique voice |

---

# Dialogue Synthesis

Future dialogue systems may support:
- concatenated synthesis
- pause timing
- conversational rhythm
- role-aware playback

However:
- speaker mappings must remain stable
- dialogue synthesis must remain deterministic
- persona consistency must be preserved

---

# Persona Stability Rule

Do NOT inject persona metadata corpus-wide until:
- stable role taxonomy exists
- stable voice mappings exist
- deterministic assignment rules exist

Prototype carefully before large-scale rollout.

---

# Category-Based Audio Rollout

Do NOT synthesize the entire corpus at once.

Prefer:
- category-by-category rollout
- validation checkpoints
- incremental QA
- progressive deployment

Recommended rollout order:
1. travel
2. accommodation
3. dining
4. social
5. health

These categories provide the highest immersion value.

---

# Audio UX Philosophy

Audio immersion quality is now more important than:
- raw synthesis volume
- maximum throughput
- maximum voice variety

Prioritize:
- listening comfort
- realism
- pacing
- immersion
- consistency
- comprehension

---

# Final Success Condition

A successful task means:
- corpus integrity preserved
- schema consistency preserved
- deterministic infrastructure preserved
- resumability preserved
- realism preserved
- immersion preserved
- validation passed
- audio UX quality maintained
