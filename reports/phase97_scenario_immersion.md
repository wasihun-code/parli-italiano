# Phase 9.7: Scenario Immersion Defect Resolution

## 1. Root Cause
The initial view of `LearningSystemV3PilotScreen` functioned like a generic vocabulary trainer ("Stai per iniziare una sessione..."). It lacked context, failing to connect the upcoming exercises to the actual goal of "Apartment Key Pickup".

## 2. Fix Implemented
Rebuilt the pilot entry screen to include:
- **Scenario Banner:** Emphasizing the scenario title and "Conversation Stage: Arrival".
- **Current Goal:** "Master the vocabulary and sentences needed to find the building entrance..."
- **Why This Matters:** Cultural context regarding Italian intercoms and courtyards.
- **Conversation Preview:** A simulated text-message style preview of the target dialogue ("Sono davanti al portone...").

## 3. Result
Learners are now emotionally and contextually primed for the specific scenario before the first exercise begins, enhancing immersion.
