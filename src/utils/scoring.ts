export function percentageScore(correct: number, total: number): number {
  if (total <= 0) {
    return 0;
  }

  return Math.round((correct / total) * 100);
}

export function hasPassedFoundation(score: number): boolean {
  return score >= 90;
}

export function hasPassedPhraseTraining(score: number): boolean {
  return score >= 85;
}

export function hasPassedSentenceTraining(score: number): boolean {
  return score >= 80;
}
