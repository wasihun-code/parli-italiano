# Exercise Registry Specification

The Exercise Registry is the central source of truth for all exercise types in Learning System V3. It decouples the learning logic (Generator) from the user interface (Renderer).

## Registry Architecture

The registry is implemented in `src/exercises/registry.ts` and maps `ExerciseType` strings to their formal `ExerciseDefinition`.

```typescript
interface ExerciseDefinition {
  metadata: ExerciseMetadata;
  payloadBuilder: ExerciseFactory;
  validator: ExerciseValidator;
  completionHandler: CompletionHandler;
}
```

## Supported Exercise Types

1.  **Listen**: Audio playback verification.
2.  **ListenChoose**: Auditory recognition (MCQ).
3.  **Match**: Visual recognition (MCQ).
4.  **BuildSentence**: Syntax assembly for phrases.
5.  **Recall**: Gap fill / Cloze.
6.  **Dictation**: Audio transcription.
7.  **Speaking**: Verbal production.
8.  **Reading**: Passive comprehension.
9.  **Conversation**: Situational branching choices.
10. **Review**: SRS maintenance flow.
11. **Assembly**: Scrambled word construction for sentences.
12. **Spelling**: Explicit typing without audio assistance.

## Payload Contracts

Every exercise must define a `payloadBuilder`. This factory takes raw scenario item data and returns a structured `ExercisePayload`.

**Contract Requirement:** Payload builders must be deterministic. The same item data must always produce the same payload (e.g., same distractor options if provided in JSON).

## Validation Contracts

The `validator` function is a pure logic block:
`(payload: ExercisePayload, userInput: any) => ValidationResult`

It returns an `isValid` boolean and a `score` (0.0 to 1.0). This allows for future "Partial Success" mechanics.

## Completion Contracts

When a user submits their answer and the validation is processed, the `completionHandler` is invoked. It is responsible for:
- Logging the performance.
- Calculating final mastery impact.
- Determining if the user should repeat the exercise (Retry).
