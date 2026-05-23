import React from 'react';
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { ReviewScreen } from './ReviewScreen';
import { useSrsStore } from '@shared/store/srsStore';

vi.mock('../lib/tts', () => ({
  Tts: { speak: vi.fn() },
}));

const renderWithRouter = (ui: React.ReactElement) =>
  render(<BrowserRouter>{ui}</BrowserRouter>);

describe('ReviewScreen', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
  });

  it('shows the empty state when no items are due', () => {
    renderWithRouter(<ReviewScreen />);
    expect(screen.getByText('Ripasso completato')).toBeInTheDocument();
  });

  it('shows stats even when empty', () => {
    renderWithRouter(<ReviewScreen />);
    expect(screen.getByText('0 imparati / 0 totali')).toBeInTheDocument();
  });

  it('displays a due item on the flashcard', () => {
    useSrsStore.getState().registerItem({
      id: 'i1',
      type: 'vocabulary',
      italian: 'grazie',
      english: 'thank you',
    });
    // Force it to be due now
    useSrsStore.setState(state => ({
      items: {
        ...state.items,
        i1: { ...state.items['i1'], learned: true, dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    // English side shown first by default (Task 7 reverse order)
    expect(screen.getByText('thank you')).toBeInTheDocument();
    expect(screen.getByText('Inglese')).toBeInTheDocument();
  });

  it('flips the card to show Italian on click', () => {
    useSrsStore.getState().registerItem({
      id: 'i1',
      type: 'vocabulary',
      italian: 'grazie',
      english: 'thank you',
    });
    useSrsStore.setState(state => ({
      items: {
        ...state.items,
        i1: { ...state.items['i1'], learned: true, dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    // Click the card to flip
    fireEvent.click(screen.getByText('thank you'));
    expect(screen.getByText('grazie')).toBeInTheDocument();
    expect(screen.getByText('Italiano')).toBeInTheDocument();
  });

  it('records a correct answer and updates streak', () => {
    useSrsStore.getState().registerItem({
      id: 'i1',
      type: 'vocabulary',
      italian: 'grazie',
      english: 'thank you',
    });
    useSrsStore.setState(state => ({
      items: {
        ...state.items,
        i1: { ...state.items['i1'], learned: true, dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    fireEvent.click(screen.getByText('thank you'));
    fireEvent.click(screen.getByText('RICORDATO'));

    expect(useSrsStore.getState().items['i1'].correctStreak).toBe(1);
    expect(useSrsStore.getState().items['i1'].attempts).toBe(1);
  });

  it('records an incorrect answer and resets streak', () => {
    useSrsStore.getState().registerItem({
      id: 'i1',
      type: 'vocabulary',
      italian: 'grazie',
      english: 'thank you',
    });
    // Give it a streak first
    useSrsStore.getState().recordAnswer('i1', true);
    useSrsStore.setState(state => ({
      items: {
        ...state.items,
        i1: { ...state.items['i1'], learned: true, dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    fireEvent.click(screen.getByText('thank you'));
    fireEvent.click(screen.getByText('DIMENTICATO'));

    expect(useSrsStore.getState().items['i1'].correctStreak).toBe(0);
  });
});
