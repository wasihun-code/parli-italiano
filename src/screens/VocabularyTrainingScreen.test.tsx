import { describe, it, expect, beforeEach, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { MemoryRouter, Route, Routes } from 'react-router-dom';
import { VocabularyTrainingScreen } from './VocabularyTrainingScreen';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';

// Mock DB and TTS so async loads complete instantly
vi.mock('../lib/db', () => ({
  setupDatabase: vi.fn().mockResolvedValue(undefined),
  loadScenarioHeader: vi.fn().mockResolvedValue({ id: 1, title: 'Test Scenario' }),
  loadScenarioVocabulary: vi.fn().mockResolvedValue([
    { id: 'v1', italian: 'ciao', english: 'hello' },
    { id: 'v2', italian: 'grazie', english: 'thank you' },
    { id: 'v3', italian: 'prego', english: 'you are welcome' },
  ]),
}));

vi.mock('../lib/tts', () => ({
  Tts: { speak: vi.fn() },
}));

const renderScreen = () =>
  render(
    <MemoryRouter initialEntries={['/scenarios/1/vocabulary']}>
      <Routes>
        <Route path="/scenarios/:scenarioId/vocabulary" element={<VocabularyTrainingScreen />} />
      </Routes>
    </MemoryRouter>,
  );

describe('VocabularyTrainingScreen', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
    useProgressStore.setState({ scenarioProgress: {}, foundationScores: {} });
  });

  it('renders loading state initially then shows content', async () => {
    renderScreen();
    expect(screen.getByText(/Loading vocabulary/)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText('Test Scenario')).toBeInTheDocument());
  });

  it('shows the SKIP button after loading', async () => {
    renderScreen();
    await waitFor(() => expect(screen.getByText('SKIP')).toBeInTheDocument());
  });

  it('entering skip test shows multiple choice option buttons', async () => {
    renderScreen();
    await waitFor(() => expect(screen.getByText('SKIP')).toBeInTheDocument());

    fireEvent.click(screen.getByText('SKIP'));

    // Skip test uses multiple-choice: at least 2 buttons with numbered options should appear
    // The numbered option buttons have a span inside with the number
    await waitFor(() => {
      // Look for "1." number label text characteristic of multiple choice options
      expect(screen.getByText('1')).toBeInTheDocument();
    });
  });

  it('clicking a multiple-choice option shows feedback', async () => {
    renderScreen();
    await waitFor(() => expect(screen.getByText('SKIP')).toBeInTheDocument());

    fireEvent.click(screen.getByText('SKIP'));

    // Wait for numbered options to appear
    await waitFor(() => expect(screen.getByText('1')).toBeInTheDocument());

    // Find the option buttons (they contain a numbered span + text).
    // Get all buttons, find those that have a '1.' span sibling (the option buttons)
    const allButtons = screen.getAllByRole('button');
    const optionButton = allButtons.find(b =>
      ['ciao', 'grazie', 'prego'].some(text => b.textContent?.includes(text)),
    );
    expect(optionButton).toBeDefined();

    fireEvent.click(optionButton!);

    // After answering, either feedback shows or the next question loads
    // Either Continue button appears or the exercise advances
    await waitFor(() => {
      const continueBtn = screen.queryByRole('button', { name: /Continue/i });
      const playAudio = screen.queryByRole('button', { name: /Play Audio/i });
      // At least one of these should be visible after answering
      expect(continueBtn || playAudio).toBeTruthy();
    }, { timeout: 2000 });
  });

  it('completes the skip test with success and updates stores', async () => {
    renderScreen();
    await waitFor(() => expect(screen.getByText('SKIP')).toBeInTheDocument());

    fireEvent.click(screen.getByText('SKIP'));

    const vocabulary = [
      { id: 'v1', italian: 'ciao', english: 'hello' },
      { id: 'v2', italian: 'grazie', english: 'thank you' },
      { id: 'v3', italian: 'prego', english: 'you are welcome' },
    ];

    for (let i = 0; i < 3; i++) {
      await waitFor(() => expect(screen.getByText('1')).toBeInTheDocument());
      const prompt = screen.getByRole('heading', { level: 1 }).textContent;
      const term = vocabulary.find(v => v.english === prompt);
      if (!term) throw new Error(`Could not find term for prompt: ${prompt}`);
      
      fireEvent.click(screen.getByText(term.italian));
      
      const continueBtn = await screen.findByRole('button', { name: /Continue/i });
      fireEvent.click(continueBtn);
    }

    // Results screen should appear
    await waitFor(() => expect(screen.getByText('Test Results')).toBeInTheDocument());
    
    // Verify stores are updated
    const srsState = useSrsStore.getState();
    expect(srsState.items['v1']?.learned).toBe(true);
    expect(srsState.items['v2']?.learned).toBe(true);
    expect(srsState.items['v3']?.learned).toBe(true);
    
    const progressState = useProgressStore.getState();
    expect(progressState.scenarioProgress[1]?.vocabularyCompleted).toBe(true);
    expect(progressState.scenarioProgress[1]?.phraseScore).toBe(100);
  });
});
