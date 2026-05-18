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
    expect(screen.getByText('Nothing to review right now - come back later!')).toBeInTheDocument();
  });

  it('shows stats even when empty', () => {
    renderWithRouter(<ReviewScreen />);
    expect(screen.getByText('0 learned / 0 total')).toBeInTheDocument();
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
        i1: { ...state.items['i1'], dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    // Italian side shown first
    expect(screen.getByText('grazie')).toBeInTheDocument();
    expect(screen.getByText('Italian')).toBeInTheDocument();
  });

  it('flips the card to show English on click', () => {
    useSrsStore.getState().registerItem({
      id: 'i1',
      type: 'vocabulary',
      italian: 'grazie',
      english: 'thank you',
    });
    useSrsStore.setState(state => ({
      items: {
        ...state.items,
        i1: { ...state.items['i1'], dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    // Click the card to flip
    fireEvent.click(screen.getByText('grazie'));
    expect(screen.getByText('thank you')).toBeInTheDocument();
    expect(screen.getByText('Translation')).toBeInTheDocument();
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
        i1: { ...state.items['i1'], dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    fireEvent.click(screen.getByText('grazie'));
    fireEvent.click(screen.getByText('REMEMBERED'));

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
        i1: { ...state.items['i1'], dueAt: new Date(Date.now() - 10_000).toISOString() },
      },
    }));

    renderWithRouter(<ReviewScreen />);
    fireEvent.click(screen.getByText('grazie'));
    fireEvent.click(screen.getByText('FORGOT'));

    expect(useSrsStore.getState().items['i1'].correctStreak).toBe(0);
  });
});
