# Certification Storage Audit

## 1. Authoritative Source of Truth
The investigation confirms that **`reports/global_certification.json`** is the absolute authoritative source of truth for the certification status of all 116 scenarios.

- **File Path:** `reports/global_certification.json`
- **Scenarios Found:** 116
- **Status:** 100% Pass Rate (116/116)
- **Last Run Timestamp:** 2026-06-05T15:49:45

## 2. Per-Scenario Certification Files
Per-scenario certification files (`reports/*_certification.md`) are transient artifacts generated during individual scenario builds or partial audit runs. They are NOT guaranteed to exist for all 116 scenarios simultaneously in the `reports/` directory, as the global certification pipeline may prioritize a consolidated report or cleanup individual files to reduce clutter.

## 3. Discovered Redundancy
There are 14 individual `*_certification.md` files currently residing in `reports/`. These represent a partial state and should not be used as the primary metric for release readiness.

## 4. Requirement for Audit Fix
The `release_readiness_audit.py` script must be updated to parse the `global_certification.json` file rather than counting individual markdown files.
