# V3 Runtime Contract

This document defines the data flow between the Learning System V3 components.

## Data Flow Diagram

```text
[Scenario JSON] + [Global Mastery Map]
          |
          v
[LearningPathGenerator]
          |
          v
[Ordered LearningSteps]
          |
          v
[Exercise Resolver] <--- [Exercise Registry]
          |
          v
[ExerciseDefinition] + [Dynamic Payload]
          |
          v
[Future UI Renderer]
```

## Layer Responsibilities

### 1. LearningPathGenerator
- **Role:** Strategist.
- **Input:** Raw scenario data and user progress.
- **Responsibility:** Determine WHAT items are taught and in WHAT sequence. It emits abstract `LearningStep` objects.

### 2. Exercise Resolver
- **Role:** Broker.
- **Input:** A single `LearningStep`.
- **Responsibility:** Map the step's `exerciseType` to a formal `ExerciseDefinition` and generate the `ExercisePayload` by combining the step with the specific item data.

### 3. Exercise Registry
- **Role:** Source of Truth for Types.
- **Responsibility:** Define the metadata, builders, and validators for all exercise types.

### 4. UI Renderer (Phase 9.4+)
- **Role:** Presenter.
- **Input:** `ExerciseDefinition` + `ExercisePayload`.
- **Responsibility:** Display the exercise to the user and capture input. It does NOT contain learning logic.
