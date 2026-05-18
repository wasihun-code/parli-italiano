import { describe, it, expect, beforeEach, vi } from 'vitest';
import { render, screen, fireEvent, waitFor, act } from '@testing-library/react';
import { MemoryRouter, Route, Routes } from 'react-router-dom';
import { ConversationScreen } from './ConversationScreen';
import { useConversationStore } from '@shared/store/conversationStore';
import { useProgressStore } from '@shared/store/progressStore';
import { generateResponse } from '../lib/llm';

// Mock all external dependencies
vi.mock('../lib/db', () => ({
  setupDatabase: vi.fn().mockResolvedValue(undefined),
  loadScenarioHeader: vi.fn().mockResolvedValue({
    id: 1,
    title: 'Cafe',
    description: 'Order a coffee',
    category: 'Travel',
  }),
  loadScenarioConversationVocabulary: vi.fn().mockResolvedValue([
    'ciao',
    'un caffe',
  ]),
}));

vi.mock('../lib/llm', () => ({
  initLlama: vi.fn().mockResolvedValue(undefined),
  unloadLlama: vi.fn().mockResolvedValue(undefined),
  generateResponse: vi.fn(),
}));

vi.mock('../lib/useSpeechRecognition', () => ({
  useSpeechRecognition: () => ({
    transcript: '',
    listening: false,
    error: null,
    start: vi.fn(),
    stop: vi.fn(),
  }),
}));

function renderConversation() {
  return render(
    <MemoryRouter initialEntries={['/scenarios/1/conversation']}>
      <Routes>
        <Route path="/scenarios/:scenarioId/conversation" element={<ConversationScreen />} />
      </Routes>
    </MemoryRouter>,
  );
}

describe('ConversationScreen (LLaMA 3.1 Alpaca)', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    
    // Reset stores
    useConversationStore.setState({
      messages: [],
      speed: 'normale',
      activeScenarioId: undefined,
      userErrors: [],
      unknownWords: [],
    });
    
    useProgressStore.setState({
      scenarioProgress: {
        1: {
          vocabularyCompleted: true,
          phraseScore: 100,
          phraseCompleted: true,
          sentenceScore: 100,
          sentenceCompleted: true,
          conversationUnlocked: true,
        },
      },
    });

    // Default mock implementation
    vi.mocked(generateResponse).mockResolvedValue('Buongiorno! Come posso aiutarti?');
  });

  it('starts conversation automatically and displays assistant greeting', async () => {
    vi.mocked(generateResponse).mockResolvedValueOnce('Benvenuti al Cafe!');
    
    await act(async () => {
      renderConversation();
    });

    await waitFor(() => {
      expect(generateResponse).toHaveBeenCalled();
      expect(screen.getByText('Benvenuti al Cafe!')).toBeInTheDocument();
    });

    const calls = vi.mocked(generateResponse).mock.calls;
    const firstCallMessages = calls[0][0] as any[];
    
    expect(firstCallMessages[0].content).toContain('Parla SOLO in italiano');
    expect(firstCallMessages[0].content).toContain('Scenario: Cafe');
    expect(firstCallMessages[1].content).toContain('Inizia la conversazione.');
  });

  it('sends user message and displays assistant response', async () => {
    vi.mocked(generateResponse)
      .mockResolvedValueOnce('Ciao! Cosa desideri?') // Greeting
      .mockResolvedValueOnce('Certamente, un caffè per te.'); // User reply

    await act(async () => {
      renderConversation();
    });

    await screen.findByText('Ciao! Cosa desideri?');

    const textInputToggle = screen.getByRole('button', { name: 'Type instead' }); 
    fireEvent.click(textInputToggle);

    const input = screen.getByPlaceholderText('Scrivi in italiano...');
    fireEvent.change(input, { target: { value: 'Vorrei un caffè.' } });
    
    const sendButton = screen.getByRole('button', { name: 'Send message' });
    await act(async () => {
      fireEvent.click(sendButton);
    });

    await waitFor(() => {
      expect(generateResponse).toHaveBeenCalledTimes(2);
      expect(screen.getByText('Vorrei un caffè.')).toBeInTheDocument();
      expect(screen.getByText('Certamente, un caffè per te.')).toBeInTheDocument();
    });
  });

  it('displays multiple assistant messages in order', async () => {
    vi.mocked(generateResponse)
      .mockResolvedValueOnce('Messaggio 1') // Greeting
      .mockResolvedValueOnce('Risposta 1')  // After user msg 1
      .mockResolvedValueOnce('Risposta 2'); // After user msg 2

    await act(async () => {
      renderConversation();
    });

    await screen.findByText('Messaggio 1');

    const textInputToggle = screen.getByRole('button', { name: 'Type instead' }); 
    fireEvent.click(textInputToggle);
    const input = screen.getByPlaceholderText('Scrivi in italiano...');
    const sendButton = screen.getByRole('button', { name: 'Send message' });

    // Send first message
    fireEvent.change(input, { target: { value: 'User 1' } });
    await act(async () => {
      fireEvent.click(sendButton);
    });
    await screen.findByText('Risposta 1');

    // Send second message
    fireEvent.change(input, { target: { value: 'User 2' } });
    await act(async () => {
      fireEvent.click(sendButton);
    });
    await screen.findByText('Risposta 2');

    const assistantBubbles = screen.getAllByText(/Messaggio 1|Risposta 1|Risposta 2/);
    expect(assistantBubbles).toHaveLength(3);
    expect(assistantBubbles[0]).toHaveTextContent('Messaggio 1');
    expect(assistantBubbles[1]).toHaveTextContent('Risposta 1');
    expect(assistantBubbles[2]).toHaveTextContent('Risposta 2');
  });

  it('handles translation on-demand with correct prompt and UI update', async () => {
    vi.mocked(generateResponse).mockResolvedValueOnce('Buongiorno!');
    
    await act(async () => {
      renderConversation();
    });
    await screen.findByText('Buongiorno!');

    // Click Translate button
    const translateBtn = await screen.findByText('Traduci');
    
    vi.mocked(generateResponse).mockResolvedValueOnce('Good morning!');
    
    await act(async () => {
      fireEvent.click(translateBtn);
    });

    await waitFor(() => {
      expect(screen.getByText('Good morning!')).toBeInTheDocument();
      expect(screen.getByText('Mostra Italiano')).toBeInTheDocument();
    });

    const translationCall = vi.mocked(generateResponse).mock.calls.find(c => 
      (c[0] as any[])[0].content.includes('Translate the following Italian text to English')
    );
    expect(translationCall).toBeDefined();
    expect(translationCall![0][0].content).toContain('### Input:\nBuongiorno!');
  });

  it('sends grammar mini-lesson after 6 user messages and displays it separately', async () => {
    // 1 greeting + 6 replies + 1 mini-lesson = 8 calls
    for (let i = 1; i <= 7; i++) {
      vi.mocked(generateResponse).mockResolvedValueOnce(`Risposta ${i}`);
    }
    vi.mocked(generateResponse).mockResolvedValueOnce('CONSIGLIO GRAMMATICALE: ...');

    await act(async () => {
      renderConversation();
    });
    await screen.findByText('Risposta 1'); // The greeting

    const textInputToggle = screen.getByRole('button', { name: 'Type instead' }); 
    fireEvent.click(textInputToggle);
    const input = screen.getByPlaceholderText('Scrivi in italiano...');
    const sendButton = screen.getByRole('button', { name: 'Send message' });

    // Send 6 messages
    for (let i = 1; i <= 6; i++) {
      fireEvent.change(input, { target: { value: `User ${i}` } });
      await act(async () => {
        fireEvent.click(sendButton);
      });
      await screen.findByText(`Risposta ${i+1}`);
    }

    await waitFor(() => {
      expect(generateResponse).toHaveBeenCalledTimes(8);
      expect(screen.getByText('Risposta 7')).toBeInTheDocument();
      expect(screen.getByText('CONSIGLIO GRAMMATICALE: ...')).toBeInTheDocument();
    }, { timeout: 10000 });

    const bubbles = screen.getAllByText(/Risposta 7|CONSIGLIO GRAMMATICALE/);
    expect(bubbles[0]).toHaveTextContent('Risposta 7');
    expect(bubbles[1]).toHaveTextContent('CONSIGLIO GRAMMATICALE: ...');
  });

  it('shows error bubble when generateResponse fails', async () => {
    vi.mocked(generateResponse)
      .mockResolvedValueOnce('Greeting')
      .mockRejectedValueOnce(new Error('Network error'));
    
    await act(async () => {
      renderConversation();
    });
    await screen.findByText('Greeting');

    const textInputToggle = screen.getByRole('button', { name: 'Type instead' }); 
    fireEvent.click(textInputToggle);
    const input = screen.getByPlaceholderText('Scrivi in italiano...');
    fireEvent.change(input, { target: { value: 'Ciao' } });
    const sendButton = screen.getByRole('button', { name: 'Send message' });
    
    await act(async () => {
      fireEvent.click(sendButton);
    });

    await waitFor(() => {
      const errorElements = screen.getAllByText('Network error');
      expect(errorElements.length).toBeGreaterThan(0);
    });
  });

  it('displays raw Italian response exactly as returned (no parsing)', async () => {
    const rawOutput = 'ITALIAN: label is ignored because we dont parse anymore.';
    vi.mocked(generateResponse).mockResolvedValueOnce(rawOutput);

    await act(async () => {
      renderConversation();
    });

    await waitFor(() => {
      expect(screen.getByText(rawOutput)).toBeInTheDocument();
    });
  });

  it('renders locked state when conversation is not unlocked', async () => {
    useProgressStore.setState({
      scenarioProgress: {
        1: {
          conversationUnlocked: false,
          vocabularyCompleted: false,
          phraseScore: 0,
          phraseCompleted: false,
          sentenceScore: 0,
          sentenceCompleted: false,
        },
      },
    });

    await act(async () => {
      renderConversation();
    });

    expect(await screen.findByText('Conversazione Bloccata')).toBeInTheDocument();
  });
});
