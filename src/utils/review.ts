import type {SrsItem} from '@app/store/srsStore';

export type ReviewStats = {
  totalItems: number;
  dueItems: number;
  learnedItems: number;
};

export function calculateReviewStats(
  items: Record<string, SrsItem>,
  dueItems: SrsItem[],
): ReviewStats {
  const allItems = Object.values(items);
  return {
    totalItems: allItems.length,
    dueItems: dueItems.length,
    learnedItems: allItems.filter(item => item.learned).length,
  };
}

export function getNextReviewIndex(
  currentIndex: number,
  dueItemCount: number,
): number {
  if (dueItemCount <= 1) {
    return 0;
  }

  return currentIndex >= dueItemCount - 1 ? 0 : currentIndex + 1;
}
