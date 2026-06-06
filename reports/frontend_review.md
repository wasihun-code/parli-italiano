# Frontend Review: Phase 7.8 — Daily Review System

## 1. Overview
This report outlines the design and implementation specifications for the new `DailyReviewScreen.tsx`, the `HomeScreen` integration, and Admin Dashboard enhancements for tracking student progress through Spaced Repetition (SRS).

## 2. DailyReviewScreen.tsx Design

### 2.1 Screen State Machine
The screen will manage three primary states:
1. **Intro**: Displays a summary of reviews due today.
2. **Reviewing**: The active flashcard session.
3. **Outro**: Success screen with performance metrics.

### 2.2 UI Specifications

#### Intro State (Entry Screen)
- **Header**: "Ripasso Giornaliero" (Daily Review).
- **Metric Cards**:
    - **Vocabulary**: 12 items.
    - **Phrases**: 6 items.
- **Action**: Large "Inizia Sessione" (Start Session) button.

#### Reviewing State (Flashcards)
- **Progress Bar**: Thin bar at the top showing completion percentage.
- **Flashcard**:
    - Centered card with `colors.cardBg` and 16px border-radius.
    - Large typography for Italian (e.g., `fontSize: 36`).
    - Subtitle indicating category (e.g., "Vocabolario").
    - **Interaction**: Tap card to reveal English translation with a "flip" animation.
- **Feedback Buttons (Post-Reveal)**:
    - A row of 4 buttons at the bottom:
        1. **Again** (`colors.error`): Failed to remember.
        2. **Hard** (`colors.warning`): Remembered with significant effort.
        3. **Good** (`colors.primary`): Remembered with standard effort.
        4. **Easy** (`colors.success`): Remembered instantly.

#### Outro State (Summary)
- **Visual**: Celebration icon (e.g., 🏆 or 🎉).
- **Summary**: "18 elementi ripassati!"
- **Stats**: Streak update, XP earned.
- **Action**: "Torna alla Home" button.

### 2.3 SRS Mapping Logic
To support granular feedback, the `srsStore` should be updated to accept `SrsFeedback`.
- **Again**: Interval reset to minimum (5 mins).
- **Hard**: Interval * 1.2.
- **Good**: Interval * 2.5.
- **Easy**: Interval * 4.0.

## 3. Home Screen Integration

### 3.1 Daily Review Banner
A new component `DailyReviewBanner.tsx` will be placed above the "Main Action Card" on the `HomeScreen`.

- **Style**:
    - Background: `colors.chipBg`.
    - Border: `2px solid ${colors.accent}`.
    - Icon: 🧠 (Brain).
    - Text: "**18 Ripassi in scadenza** - Mantieni viva la memoria!"
- **Action**: Clicking the banner navigates to `/daily-review`.

## 4. Admin Dashboard Enhancements

### 4.1 Analytics Updates (`AnalyticsDashboard.tsx`)
- **Metric Card: Average Daily Reviews**:
    - Tracks how many SRS items users are completing per day on average.
- **Table: "Le Più Dimenticate" (Most Forgotten Items)**:
    - Lists Vocabulary/Phrases with the highest "Again" feedback ratio.
    - Columns: ID, Italian, English, Fail Rate (%).

### 4.2 User Detail View Updates
- **SRS Heatmap**: A calendar view showing daily review activity for the specific user.
- **Knowledge Retention Rate**: Percentage of items currently in "Good" or "Easy" status vs. "Again" or "Hard".

## 5. Technical Implementation Notes
- Use `framer-motion` for the flashcard flip animation if available, otherwise CSS transitions.
- Ensure `useSrsStore` is reactive so the banner count updates immediately after a session.
- Add `KeyboardEvents` support (1, 2, 3, 4 keys) for fast desktop reviewing.
