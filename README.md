# Parla Italiano 🇮🇹
### Offline Italian conversation practice with a friendly AI tutor.

Parla Italiano is a web-based language learning application designed to bridge the gap between basic vocabulary and real-world conversation. It features immersive scenarios, comprehensive grammar lessons, a suite of interactive games, and a specialized AI tutor named **Antonio**, powered by **llama3.1:8b** running locally through Ollama.

---

## ✨ Features

- **116 Validated Scenarios**: From ordering a coffee in Rome to navigating a job interview in Milan. Each scenario includes Vocabulary, Phrases, and Sentence training.
- **7 Interactive Mini-Games**: 
  - **Gender (Maschile o Femminile?)**: Fast-paced noun classification.
  - **Translation**: Sentence-level translation drills.
  - **Prepositions**: Contextual preposition mastery.
  - **Expressions (Idioms)**: Learn common Italian sayings and their meanings.
  - **Opposites**: Typed-answer antonym challenge.
  - **Numbers**: Practice digits ↔ Italian word conversion (1-1000).
  - **Stories (Storie) 📖**: Immersive book-style reader with parallel translations and comprehension quizzes.
- **Comprehensive Grammar (A1-A2)**: 12 detailed topics with explanations, practical examples, and interactive quizzes.
- **Phased Learning Path**: Master the essential Italian building blocks through Foundations, Scenarios, and Games.
- **AI Conversation**: Open-ended role-play with **Antonio**, your personal AI tutor, powered by local inference.
- **Explanatory Feedback**: Dynamic, rule-based explanations for incorrect answers to help you understand *why* a mistake was made.
- **Offline-First**: Powered by **Ollama** and **llama3.1:8b** for secure, local inference.
- **SRS Review**: Spaced Repetition System (Spaced Cards) to ensure long-term retention of new words.
- **Placement Test**: Start at the right level based on your current proficiency.
- **Keyboard Shortcuts**: Power-user features (1-4 for options, Enter to submit) for a faster learning flow.

---

## 🛠 Tech Stack

- **Frontend**: React 19, TypeScript, Vite
- **State Management**: Zustand (Persisted)
- **Local Database**: Dexie.js (IndexedDB)
- **AI Engine**: Ollama (`llama3.1:8b` by default)
- **Voice**: Web Speech API / Spark-TTS

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v18+)
- **npm** or **yarn**
- **Ollama**: [Download here](https://ollama.com/)
- **RAM**: 8GB minimum (16GB recommended for smooth inference)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/parli-italiano.git
   cd parli-italiano
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Configure Ollama**
   - Ensure the Ollama server is running.
   - Ensure the `llama3.1:8b` model is available:
     ```bash
     ollama pull llama3.1:8b
     ```

4. **Environment Variables**
   Create a `.env` file in the root:
   ```env
   VITE_OLLAMA_URL=http://localhost:11434
   VITE_OLLAMA_MODEL=llama3.1:8b
   ```

5. **Run the Development Server**
   ```bash
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## 📂 Project Structure

- `src/`: Main source code.
  - `ai/`: Prompt templates and AI logic.
  - `components/`: Reusable UI components.
  - `data/`: Scenario definitions, lesson content, games, and stories.
  - `lib/`: Utilities (LLM, TTS, DB, etc.).
  - `screens/`: App screens (Home, Training, Conversation, Games).
  - `store/`: Zustand state stores for auth, progress, and game state.
- `scripts/`: Generation and validation scripts for curriculum and data.
- `public/`: Static assets and PWA icons.
- `e2e/`: Playwright end-to-end tests.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- **Ollama**: For providing the engine for local LLM inference.
- **Spark-TTS**: For high-quality Italian speech synthesis.
