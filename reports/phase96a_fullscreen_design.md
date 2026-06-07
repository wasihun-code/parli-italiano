# Phase 9.6a: Fullscreen Design

## 1. Requirement
Transform the learning environment into a distraction-free, immersive experience.

## 2. Design Strategy
- **Remove Chrome:** All site navigation (Sidebar, Bottom Nav) is hidden during the session.
- **Centering:** The exercise is vertically and horizontally centered on the screen.
- **Responsive Sizing:** Max width of 600px ensures readability on tablets and desktops while being thumb-friendly on mobile.

## 3. Implementation
The `LearningSystemV3PilotScreen` uses a `flex: 1` container that expands to fill the entire viewport, effectively creating a dedicated "Learning Mode".

## 4. Conclusion
The learner is no longer distracted by the broader app interface, allowing for deeper focus on the Italian content.
