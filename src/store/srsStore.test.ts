import { useSrsStore } from './srsStore';

describe('srsStore', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
  });

  it('registers a new item', () => {
    useSrsStore.getState().registerItem({
      id: 'item1',
      type: 'vocabulary',
      italian: 'ciao',
      english: 'hello',
    });

    const items = useSrsStore.getState().items;
    expect(items['item1']).toBeDefined();
    expect(items['item1']!.learned).toBe(false);
    expect(items['item1']!.correctStreak).toBe(0);
  });

  it('updates correct streak and learned status on correct answers', () => {
    useSrsStore.getState().registerItem({
      id: 'item1',
      type: 'vocabulary',
      italian: 'ciao',
      english: 'hello',
    });

    useSrsStore.getState().recordAnswer('item1', true);
    useSrsStore.getState().recordAnswer('item1', true);
    useSrsStore.getState().recordAnswer('item1', true);

    const items = useSrsStore.getState().items;
    expect(items['item1']!.correctStreak).toBe(3);
    expect(items['item1']!.learned).toBe(true);
  });

  it('resets streak on incorrect answer', () => {
    useSrsStore.getState().registerItem({
      id: 'item1',
      type: 'vocabulary',
      italian: 'ciao',
      english: 'hello',
    });

    useSrsStore.getState().recordAnswer('item1', true);
    useSrsStore.getState().recordAnswer('item1', false);

    const items = useSrsStore.getState().items;
    expect(items['item1']!.correctStreak).toBe(0);
    expect(items['item1']!.learned).toBe(false);
  });
});
