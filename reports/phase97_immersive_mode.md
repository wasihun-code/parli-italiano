# Phase 9.7: Immersive Mode Defect Resolution

## 1. Root Cause
The `FooterNav` and application shell chrome were not configured to hide during the V3 pilot routes (`/train`). This caused the dashboard navigation to persist during learning sessions, breaking immersion.

## 2. Fix Implemented
Updated `src/components/FooterNav.tsx` to include `'/train'` in the `hideOn` array.

## 3. Result
The learning experience now occupies the entire viewport, functioning similarly to dedicated language apps like Duolingo or Babbel.
