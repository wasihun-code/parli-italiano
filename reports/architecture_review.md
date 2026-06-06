# Architecture Review — Phase 7.2

## 1. Compliance with ARCHITECTURE.md
The plan to move to a Global Dictionary adheres to the "Source of Truth Hierarchy" by deriving all lexical units from the existing `conversations.json` files. It correctly identifies the need for a relational mapping to preserve scenario context.

## 2. Compliance with HYBRID_MASTERY.md
The proposed Hybrid Mastery model (Global Vocab / Local Phrases) is correctly captured. However, the use of `concept_` IDs for homonyms must be more robust than the simple index-based approach used in the prototype (`concept_0_word`).

## 3. Compliance with DATABASE_RULES.md
**Critical Violation Found:** The proposed migration plan in `reports/hybrid_mastery_migration_plan.md` mentions "Remove scenario_vocabulary," which violates the "Never delete tables during migration" rule. Legacy tables must be retained but ignored.

## 4. Identified Architectural Risks
- **Migration Strategy Conflict:** There is a conflict between "Strategy A" (maintaining a mapping file and preserving existing scenario-bound IDs for backward compatibility) and "Strategy B" (direct ID rewriting in existing curriculum files). 
- **ID Instability:** Programmatic IDs based on indices (`concept_0_...`) are unstable. If the extraction order changes, IDs will shift, breaking user progress tracking.
- **Recommendation:** Adopt Strategy A (Relational Mapping) to ensure 100% backward compatibility with Scenario Mastery V1. Use semantic Concept IDs (e.g., `concept_english_context_normalized_word`) to ensure stability.

## 5. Implementation Plan Approval
Approved with the following conditions:
- Do not delete `scenario_vocabulary`.
- Ensure Global IDs are deterministic and immutable.
- Prioritize mapping over rewriting.
