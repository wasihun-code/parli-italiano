import type {SrsItem} from '@app/store/srsStore';
import {useSrsStore} from '@app/store/srsStore';
import {calculateReviewStats, getNextReviewIndex} from './review';

function makeItem(id: string, dueAt: string, learned = false): SrsItem {
  return {
    id,
    type: 'vocabulary',
    italian: id,
    english: id,
    attempts: 0,
    correctAttempts: 0,
    correctStreak: learned ? 3 : 0,
    dueAt,
    learned,
  };
}

describe('review logic', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
  });

  it('calculates due and learned review stats', () => {
    const due = makeItem('ciao', new Date(0).toISOString(), true);
    const later = makeItem('grazie', new Date(9999999999999).toISOString());
    const stats = calculateReviewStats({ciao: due, grazie: later}, [due]);

    expect(stats).toEqual({
      totalItems: 2,
      dueItems: 1,
      learnedItems: 1,
    });
  });

  it('advances through due cards safely', () => {
    expect(getNextReviewIndex(0, 3)).toBe(1);
    expect(getNextReviewIndex(2, 3)).toBe(0);
    expect(getNextReviewIndex(0, 1)).toBe(0);
  });

  it('moves reviewed items out of the immediate due queue after answering', () => {
    useSrsStore.getState().registerItem({
      id: 'biglietto',
      type: 'vocabulary',
      italian: 'biglietto',
      english: 'ticket',
    });

    expect(useSrsStore.getState().getDueItems(new Date())).toHaveLength(1);
    useSrsStore.getState().recordAnswer('biglietto', true);
    expect(useSrsStore.getState().getDueItems(new Date())).toHaveLength(0);
  });
});
