# Knowledge Graph Simulation

## Architecture Shift Analysis

This report simulates the impact of moving from isolated scenario IDs to a unified Knowledge Graph architecture for vocabulary.

### Current Architecture: Scenario Mastery
- IDs are isolated per scenario (e.g., `s22-v15`, `s58-v115`).
- **Current Item Count (Total Extracted Vocab):** 28629

### Future Architecture: Global Knowledge Graph
- IDs are normalized and shared globally (e.g., `word_grazie`).
- **Potential Global Concepts:** 5293

### Impact
- **Compression %:** 81.51%

Moving to a Global Knowledge Graph would eliminate the need to track 23336 redundant learning events. The system would shrink the vocabulary spaced repetition database significantly while providing a highly accurate measure of a user's true language acquisition.
