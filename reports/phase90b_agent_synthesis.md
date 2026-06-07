# Phase 9.0B: Agent Synthesis Report

This report synthesizes findings from specialized sub-agents regarding the specification hardening of Learning System V3.

## Architecture Agent Findings
- **Determinism is the core requirement.** The path generation logic must be a pure function to avoid "state drift" between the local IndexedDB and the UI representation.
- **Service Isolation:** The `PathGenerator` should be a standalone utility class that does not have side effects. It should only return the data structure needed for the UI.
- **Risk:** Calculating large paths (300+ items) on the fly may cause UI jank. Recommendation: Chunk the generation or memoize the result.

## Learning Science Agent Findings
- **The "Recognition to Production" curve is pedagogically superior to the current alphabetical system.**
- **Interleaving:** The generator should interleave vocabulary and phrases to ensure learners see how words work in context before reaching the final conversation.
- **Scaffolding:** The 80% vocabulary mastery gate for conversations is necessary to prevent learner frustration in branching scenarios.

## Curriculum Agent Findings
- **Conversation Chronology vs. Alphabetical Sorting:** Re-sorting content based on when it appears in the dialogue is the most significant improvement for learner context.
- **Semantic Continuity:** V3 should group items by their "Turn Cluster" in the conversation JSON.

## Audit Agent Findings
- **Verification is the only path to safety.** The implementation phase must run the `learning_path_determinism_audit.py` on every major code change.
- **Content Immutability:** Any logic that attempts to `WRITE` to a scenario JSON or the `mini_lessons` table must be caught by CI and blocked.

## QA Agent Findings
- **Failure Recovery:** The "Recovery Review" mechanism (triggered by 3 mistakes in a conversation) is a critical UX safeguard. It ensures the user doesn't get stuck in a "failure loop" during dialogue.
- **Production Balance:** We must monitor that the path doesn't become 100% production too early, which would spike the dropout rate.

## Implementation Risks
1.  **Complexity Sprawl:** Building a "Pure Function" path generator that handles 11 exercise types and 4 item categories is a high-logic task.
2.  **Performance:** Generating the sequence on client-side React components.
3.  **Data Consistency:** Ensuring the IDs generated in the path match the IDs in the legacy IndexedDB tables.
