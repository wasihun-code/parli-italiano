# Parla Italiano 🇮🇹
### Offline Italian conversation practice with a friendly AI tutor.

Parla Italiano is a web-based language learning application designed to bridge the gap between basic vocabulary and real-world conversation. It features immersive scenarios and a specialized AI tutor named **Antonio**, powered by **llama3.1:8b** running locally through Ollama.

---

## ✨ Features

- **110 Real-World Scenarios**: From ordering a coffee in Rome to navigating a job interview in Milan.
- **Phased Learning Path**: 
  - **Foundations**: Master the essential Italian building blocks.
  - **Scenario Training**: Progressive drills covering Vocabulary, Phrases, and Sentences.
  - **Conversation**: Open-ended role-play with Antonio.
- **Offline-First AI**: Powered by **Ollama** and **llama3.1:8b** for secure, local inference.
- **Natural Italian Voice**: Integrated with high-quality TTS for authentic listening practice.
- **SRS Review**: Spaced Repetition System to ensure long-term retention of new words.
- **Placement Test**: Start at the right level based on your current proficiency.
- **Progress Tracking**: Detailed stats on your journey to Italian fluency.

---

## 🛠 Tech Stack

- **Frontend**: React, TypeScript, Vite
- **State Management**: Zustand
- **Local Database**: Dexie.js (IndexedDB)
- **AI Engine**: Ollama (`llama3.1:8b` by default)
- **Voice**: Spark-TTS (Optional for high-quality voice)

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
  - `data/`: Scenario definitions and lesson content.
  - `lib/`: Utilities (LLM, TTS, DB, etc.).
  - `screens/`: App screens (Home, Training, Conversation).
  - `store/`: Zustand state stores.
- `public/`: Static assets.
- `e2e/`: Playwright end-to-end tests.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- **Ollama**: For providing the engine for local LLM inference.
- **Spark-TTS**: For the natural Italian speech synthesis.
