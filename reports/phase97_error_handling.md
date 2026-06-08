# Phase 9.7: Wrong Answer Handling Defect Resolution

## 1. Root Cause
The `FeedbackOverlay.tsx` error state was visually indistinct and lacked empathetic or clear instructional text beyond a simple "Sbagliato".

## 2. Fix Implemented
- Improved visual hierarchy for errors using a highlighted, semi-transparent background box.
- Clearly labeled the correct answer with "Risposta Corretta" and increased font size (`28px`, `font-weight: 900`).
- Added supportive, constructive copy on failure: "Non preoccuparti. Lo rivedremo presto per aiutarti a memorizzarlo."

## 3. Result
Wrong answers are immediately obvious, educational (displaying the correct answer prominently), and emotionally supportive.
