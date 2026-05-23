import React, { useState, useMemo, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '../theme/colors';
import { spacing } from '../theme/spacing';
import pluralData from '../data/pluralWords.json';
import { useGameStore } from '../store/gameStore';
import { useAudioStore } from '../store/audioStore';
import { audioService } from '../lib/audioService';
import { PrimaryButton } from '../components/PrimaryButton';
import { shuffle } from '../utils/trainingUi';
import { normalizeString, levenshteinDistance } from '../utils/string';
import { ProgressBar } from '../components/ProgressBar';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { ShortcutHelp } from '../components/ShortcutHelp';
import { getWrongAnswerExplanation } from '../utils/feedbackExplanations';

export const PluralGame: React.FC = () => {
  const navigate = useNavigate();
  const { pluralGame, unlockLevel, updateHighScore } = useGameStore();
  const { soundEnabled } = useAudioStore();
  
  const [level, setLevel] = useState(1);
  const [gameState, setGameState] = useState<'lobby' | 'playing' | 'gameOver' | 'win'>('lobby');
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [typedAnswer, setTypedAnswer] = useState('');
  const [feedback, setFeedback] = useState<{ isCorrect: boolean, isNearly: boolean, correctAnswer: string, explanation?: string } | null>(null);

  const [hintsLeft, setHintsLeft] = useState(3);
  const [showHint, setShowHint] = useState(false);

  const itemsForLevel = useMemo(() => {
    const filtered = pluralData.filter(s => s.difficulty === level);
    return shuffle([...filtered]).slice(0, 15);
  }, [level]);

  const currentItem = itemsForLevel[currentIndex];

  const handleCheck = useCallback(() => {
    if (feedback || !currentItem || !typedAnswer.trim()) return;

    const normSubmitted = normalizeString(typedAnswer);
    const normExpected = normalizeString(currentItem.plural);
    
    const isCorrect = normSubmitted === normExpected;
    const isNearly = !isCorrect && normExpected.length >= 4 && levenshteinDistance(normSubmitted, normExpected) <= 1;

    if (isCorrect || isNearly) {
      if (soundEnabled) audioService.playCorrect();
      setScore(s => s + 10);
      setFeedback({ isCorrect: true, isNearly, correctAnswer: currentItem.plural });
      setTimeout(() => {
        nextQuestion();
      }, 800);
    } else {
      if (soundEnabled) audioService.playIncorrect();
      setLives(l => l - 1);
      const explanation = getWrongAnswerExplanation({
        type: 'plural',
        italian: currentItem.italian,
        correctAnswer: currentItem.plural
      });
      setFeedback({ isCorrect: false, isNearly: false, correctAnswer: currentItem.plural, explanation });
    }
  }, [feedback, currentItem, typedAnswer, soundEnabled]);

  const nextQuestion = useCallback(() => {
    setFeedback(null);
    setTypedAnswer('');
    setShowHint(false);
    if (currentIndex + 1 < itemsForLevel.length) {
      setCurrentIndex(i => i + 1);
    } else {
      if (soundEnabled) audioService.playComplete();
      setGameState('win');
      updateHighScore('pluralGame', score);
      if (score >= 100 && level < 3) {
        if (soundEnabled) audioService.playLevelUp();
        unlockLevel('pluralGame', level + 1);
      }
    }
  }, [currentIndex, itemsForLevel.length, score, updateHighScore, soundEnabled, level, unlockLevel]);

  useEffect(() => {
    if (lives <= 0) {
      setGameState('gameOver');
      updateHighScore('pluralGame', score);
    }
  }, [lives, score, updateHighScore]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (gameState !== 'playing') return;
      if (e.key === 'Enter') {
        e.preventDefault();
        if (feedback && !feedback.isCorrect) {
          nextQuestion();
        } else if (!feedback && typedAnswer.trim()) {
          handleCheck();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameState, feedback, typedAnswer, handleCheck, nextQuestion]);


  if (gameState === 'lobby') {
    return (
      <Screen>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Plural Game</h1>
          <p style={{ color: colors.textSecondary }}>Type the plural form of the Italian word.</p>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {[1, 2, 3].map(l => {
            const isUnlocked = l <= pluralGame.unlockedLevels;
            return (
              <button
                key={l}
                disabled={!isUnlocked}
                onClick={() => { 
                    if (soundEnabled) audioService.playClick();
                    setLevel(l); setGameState('playing'); setScore(0); setLives(3); setCurrentIndex(0); setTypedAnswer(''); setFeedback(null); setHintsLeft(3); setShowHint(false); 
                }}
                className="card"
                style={{
                  padding: spacing.lg,
                  textAlign: 'left',
                  cursor: isUnlocked ? 'pointer' : 'default',
                  opacity: isUnlocked ? 1 : 0.5,
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  border: `2px solid ${colors.border}`,
                  background: colors.surface
                }}
              >
                <div>
                  <h3 style={{ margin: 0, color: colors.primary }}>Level {l}</h3>
                  <p style={{ margin: 4, fontSize: 14, color: colors.textSecondary }}>
                    {l === 1 ? 'Regular plurals (-o, -a)' : l === 2 ? 'Ending in -e' : 'Irregulars & Loanwords'}
                  </p>
                </div>
                {!isUnlocked && <span>🔒</span>}
              </button>
            );
          })}
          <PrimaryButton label="Back to Games" onPress={() => navigate('/games')} variant="secondary" />
        </div>
      </Screen>
    );
  }

  if (gameState === 'gameOver' || gameState === 'win') {
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <div className="card fade-in" style={{ padding: spacing.xl, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h1 style={{ fontSize: 48 }}>{gameState === 'win' ? '🎉 Vittoria!' : '😢 Game Over'}</h1>
          <p style={{ fontSize: 24, color: colors.textSecondary }}>Final Score: {score} / 100</p>
          <PrimaryButton label="Play Again" onPress={() => setGameState('lobby')} />
          <PrimaryButton label="Exit" onPress={() => navigate('/games')} variant="secondary" />
        </div>
      </Screen>
    );
  }

  const progressPercent = Math.min(100, (score / 100) * 100);

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm, marginBottom: spacing.xl }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ fontSize: 18, fontWeight: 900, color: colors.primary, display: 'flex', alignItems: 'center' }}>
            Level {level}
            <ShortcutHelp />
          </div>
          <div style={{ display: 'flex', gap: spacing.md }}>
            <div style={{ color: colors.accent, fontWeight: 900 }}>Score: {score} / 100</div>
            <div style={{ color: colors.error }}>{'❤️'.repeat(lives)}</div>
          </div>
        </div>
        <ProgressBar progress={progressPercent} />
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
        
        <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: -spacing.md }}>
          <button 
            onClick={() => { if (hintsLeft > 0) { setShowHint(true); setHintsLeft(h => h - 1); } }}
            disabled={hintsLeft === 0 || showHint || !!feedback}
            style={{
              padding: '8px 16px', borderRadius: 20, border: 'none', background: hintsLeft > 0 ? colors.accent : colors.border,
              color: colors.onPrimary, fontWeight: 'bold', cursor: hintsLeft > 0 ? 'pointer' : 'default', opacity: hintsLeft > 0 ? 1 : 0.5
            }}
          >
            Hint ({hintsLeft} left)
          </button>
        </div>

        <div className="card" style={{ 
          padding: spacing.xl, fontSize: 36, fontWeight: 900, color: colors.primary, textAlign: 'center'
        }}>
          {currentItem?.italian}
          <div style={{ fontSize: 16, color: colors.textSecondary, marginTop: 4 }}>
            ({currentItem?.english})
          </div>
          {showHint && <div className="fade-in" style={{ fontSize: 16, color: colors.textSecondary, marginTop: spacing.sm }}>
            <strong>Hint:</strong> Starts with "{currentItem?.plural.charAt(0).toUpperCase()}..."
          </div>}
        </div>

        {!feedback ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <input
              autoFocus
              type="text"
              value={typedAnswer}
              onChange={e => setTypedAnswer(e.target.value)}
              placeholder="Type the plural form..."
              style={{
                padding: spacing.lg,
                borderRadius: 16,
                border: `2px solid ${colors.border}`,
                fontSize: 18,
                backgroundColor: colors.bg,
                outline: 'none',
                textAlign: 'center'
              }}
            />
            <PrimaryButton label="Check" onPress={handleCheck} disabled={!typedAnswer.trim()} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, fontWeight: 800 }}>
              Tip: Press Enter to submit
            </p>
          </div>
        ) : (
          <div className="fade-in" style={{ textAlign: 'center' }}>
            <FeedbackMessage 
              type={feedback.isCorrect ? 'correct' : 'incorrect'} 
              message={
                <>
                  <div>{feedback.isCorrect ? (feedback.isNearly ? 'Quasi corretto!' : 'Perfetto!') : 'Non corretto'}</div>
                  {!feedback.isCorrect && feedback.explanation && (
                    <div style={{ marginTop: spacing.sm, fontSize: 14, fontWeight: 'normal', color: colors.textSecondary }}>
                      {feedback.explanation}
                    </div>
                  )}
                </>
              }
            />
            {!feedback.isCorrect && (
              <div className="card" style={{ marginBottom: spacing.md, padding: spacing.md }}>
                <p style={{ margin: 0, fontSize: 14, color: colors.textSecondary }}>Correct plural:</p>
                <p style={{ margin: '4px 0 0 0', fontWeight: 'bold', fontSize: 18 }}>{currentItem?.plural} ({currentItem?.english})</p>
              </div>
            )}
            {!feedback.isCorrect && <PrimaryButton label="Next" onPress={nextQuestion} />}
            {!feedback.isCorrect && (
              <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, marginTop: 8, fontWeight: 800 }}>
                Tip: Press Enter to continue
              </p>
            )}
          </div>
        )}
      </div>

      <div style={{ marginTop: 'auto' }}>
        <PrimaryButton label="Quit" onPress={() => { if (soundEnabled) audioService.playClick(); setGameState('lobby'); }} variant="secondary" />
      </div>
    </Screen>
  );
};
