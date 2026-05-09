/**
 * Unit tests for the SRS store (shared logic from src/store/srsStore.ts)
 */
import { describe, it, expect, beforeEach } from 'vitest';
import { useSrsStore } from '@shared/store/srsStore';

describe('useSrsStore', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
  });

  it('starts with an empty items record', () => {
    expect(Object.keys(useSrsStore.getState().items)).toHaveLength(0);
  });

  it('registers a new item with default values', () => {
    useSrsStore.getState().registerItem({
      id: 'v1',
      type: 'vocabulary',
      italian: 'ciao',
      english: 'hello',
    });

    const item = useSrsStore.getState().items['v1'];
    expect(item).toBeDefined();
    expect(item.italian).toBe('ciao');
    expect(item.english).toBe('hello');
    expect(item.learned).toBe(false);
    expect(item.correctStreak).toBe(0);
    expect(item.attempts).toBe(0);
  });

  it('ignores duplicate registrations', () => {
    const input = { id: 'v1', type: 'vocabulary' as const, italian: 'ciao', english: 'hello' };
    useSrsStore.getState().registerItem(input);
    useSrsStore.getState().recordAnswer('v1', true);
    useSrsStore.getState().registerItem(input); // second call
    // Streak should still be 1, not reset
    expect(useSrsStore.getState().items['v1'].correctStreak).toBe(1);
  });

  it('increments correctStreak on correct answer', () => {
    useSrsStore.getState().registerItem({ id: 'v1', type: 'vocabulary', italian: 'ciao', english: 'hello' });
    useSrsStore.getState().recordAnswer('v1', true);
    useSrsStore.getState().recordAnswer('v1', true);

    expect(useSrsStore.getState().items['v1'].correctStreak).toBe(2);
    expect(useSrsStore.getState().items['v1'].attempts).toBe(2);
    expect(useSrsStore.getState().items['v1'].correctAttempts).toBe(2);
  });

  it('marks item as learned after 3 consecutive correct answers', () => {
    useSrsStore.getState().registerItem({ id: 'v1', type: 'vocabulary', italian: 'ciao', english: 'hello' });
    useSrsStore.getState().recordAnswer('v1', true);
    useSrsStore.getState().recordAnswer('v1', true);
    expect(useSrsStore.getState().items['v1'].learned).toBe(false);
    useSrsStore.getState().recordAnswer('v1', true);
    expect(useSrsStore.getState().items['v1'].learned).toBe(true);
  });

  it('resets correctStreak on incorrect answer', () => {
    useSrsStore.getState().registerItem({ id: 'v1', type: 'vocabulary', italian: 'ciao', english: 'hello' });
    useSrsStore.getState().recordAnswer('v1', true);
    useSrsStore.getState().recordAnswer('v1', true);
    useSrsStore.getState().recordAnswer('v1', false);

    expect(useSrsStore.getState().items['v1'].correctStreak).toBe(0);
    expect(useSrsStore.getState().items['v1'].learned).toBe(false);
  });

  it('isLearned returns false for unknown items', () => {
    expect(useSrsStore.getState().isLearned('nonexistent')).toBe(false);
  });

  it('schedules correctly answered items further in the future', () => {
    useSrsStore.getState().registerItem({ id: 'v1', type: 'vocabulary', italian: 'ciao', english: 'hello' });
    const before = new Date(useSrsStore.getState().items['v1'].dueAt);
    useSrsStore.getState().recordAnswer('v1', true);
    const after = new Date(useSrsStore.getState().items['v1'].dueAt);
    expect(after.getTime()).toBeGreaterThan(before.getTime());
  });

  it('reset clears all items', () => {
    useSrsStore.getState().registerItem({ id: 'v1', type: 'vocabulary', italian: 'ciao', english: 'hello' });
    useSrsStore.getState().reset();
    expect(Object.keys(useSrsStore.getState().items)).toHaveLength(0);
  });
});
