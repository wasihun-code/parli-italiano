import React, { useState, useMemo, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { genderWords } from '@shared/data/genderWords';
import { useGameStore } from '@shared/store/gameStore';
import { PrimaryButton } from '../components/PrimaryButton';
import { shuffle } from '@shared/utils/trainingUi';
import { ProgressBar } from '../components/ProgressBar';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { ShortcutHelp } from '../components/ShortcutHelp';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';
import { useSubscriptionStore } from '@shared/store/subscriptionStore';

export const GenderGame: React.FC = () => {
  const navigate = useNavigate();
  const { genderGame, unlockLevel, updateHighScore } = useGameStore();
  const { plan, isValid } = useSubscriptionStore();
  const isPremium = plan !== 'free' && isValid;
  
  const [level, setLevel] = useState(1);
  const [gameState, setGameState] = useState<'lobby' | 'playing' | 'gameOver' | 'win'>('lobby');
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [feedback, setFeedback] = useState<{ isCorrect: boolean, message: string, explanation?: string } | null>(null);
  
  const [selectedGender, setSelectedGender] = useState<'m' | 'f' | null>(null);
  const [hintsLeft, setHintsLeft] = useState(3);
  const [showHint, setShowHint] = useState(false);

  const wordsForLevel = useMemo(() => {
    const filtered = genderWords.filter(w => w.difficulty === level);
    return shuffle([...filtered]).slice(0, 20); // 20 words per round
  }, [level]);

  const currentWord = wordsForLevel[currentIndex];

  const nextWord = useCallback(() => {
    setFeedback(null);
    setSelectedGender(null);
    setShowHint(false);
    if (currentIndex + 1 < wordsForLevel.length) {
      setCurrentIndex(i => i + 1);
    } else {
      setGameState('win');
      updateHighScore('genderGame', score + 10);
      if (score + 10 >= 100 && level < 3) {
        unlockLevel('genderGame', level + 1);
      }
    }
  }, [currentIndex, wordsForLevel.length, score, level, updateHighScore, unlockLevel]);

  const handleCheck = useCallback(() => {
    if (feedback || !currentWord || !selectedGender) return;

    if (currentWord.gender === selectedGender) {
      setScore(s => s + 10);
      setFeedback({ isCorrect: true, message: 'Ottimo!' });
      setTimeout(() => {
        nextWord();
      }, 800);
    } else {
      setLives(l => l - 1);
      const explanation = getWrongAnswerExplanation({
        type: 'gender',
        italian: currentWord.italian,
        correctAnswer: currentWord.gender
      });
      setFeedback({ 
        isCorrect: false, 
        message: `Sbagliato. "${currentWord.italian}" è ${currentWord.gender === 'm' ? 'Maschile' : 'Femminile'}.`,
        explanation 
      });
    }
  }, [feedback, currentWord, selectedGender, nextWord]);

  useEffect(() => {
    if (lives <= 0) {
      setGameState('gameOver');
      updateHighScore('genderGame', score);
    }
  }, [lives, score, updateHighScore]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (gameState !== 'playing') return;
      if (e.key === '1') setSelectedGender('m');
      if (e.key === '2') setSelectedGender('f');
      if (e.key === 'Enter') {
        e.preventDefault();
        if (feedback && !feedback.isCorrect) {
          nextWord();
        } else if (!feedback && selectedGender) {
          handleCheck();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameState, feedback, selectedGender, handleCheck, nextWord]);

  if (gameState === 'lobby') {
    return (
      <Screen>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Maschile o Femminile?</h1>
          <p style={{ color: colors.textSecondary }}>Guess the gender of the nouns.</p>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {[1, 2, 3].map(l => {
            const isPremiumLocked = l > 1 && !isPremium;
            const isUnlocked = l <= genderGame.unlockedLevels && !isPremiumLocked;
            
            const handleClick = () => {
              if (isPremiumLocked) {
                navigate('/premium');
              } else if (isUnlocked) {
                setLevel(l); 
                setGameState('playing'); 
                setScore(0); 
                setLives(3); 
                setCurrentIndex(0); 
                setHintsLeft(3); 
                setShowHint(false); 
                setSelectedGender(null); 
                setFeedback(null);
              }
            };

            return (
              <button
                key={l}
                disabled={!isUnlocked && !isPremiumLocked}
                onClick={handleClick}
                className="card"
                style={{
                  padding: spacing.lg,
                  textAlign: 'left',
                  cursor: (isUnlocked || isPremiumLocked) ? 'pointer' : 'default',
                  opacity: (isUnlocked || isPremiumLocked) ? 1 : 0.5,
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  border: `2px solid ${colors.border}`,
                  background: colors.surface,
                  width: '100%'
                }}
              >
                <div>
                  <h3 style={{ margin: 0, color: colors.primary }}>Level {l}</h3>
                  <p style={{ margin: 4, fontSize: 14, color: colors.textSecondary }}>
                    {l === 1 ? 'Common nouns (o/a)' : l === 2 ? 'Nouns ending in -e' : 'Tricky exceptions'}
                  </p>
                </div>
                {isPremiumLocked && <span style={{ fontSize: 24 }}>👑</span>}
                {!isPremiumLocked && !isUnlocked && <span>🔒</span>}
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
          <h1 style={{ fontSize: 48 }}>{gameState === 'win' ? '🎉 Bravissimo!' : '😢 Game Over'}</h1>
          <p style={{ fontSize: 24, color: colors.textSecondary }}>Final Score: {score}</p>
          <PrimaryButton label="Play Again" onPress={() => setGameState('lobby')} />
          <PrimaryButton label="Exit" onPress={() => navigate('/games')} variant="secondary" />
        </div>
      </Screen>
    );
  }

  const progressPercent = ((currentIndex) / 20) * 100;

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm, marginBottom: spacing.xl }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ fontSize: 18, fontWeight: 900, color: colors.primary, display: 'flex', alignItems: 'center' }}>
            Level {level}
            <ShortcutHelp />
          </div>
          <div style={{ display: 'flex', gap: spacing.md }}>
            <div style={{ color: colors.accent, fontWeight: 900 }}>Score: {score}</div>
            <div style={{ color: colors.error }}>{'❤️'.repeat(lives)}</div>
          </div>
        </div>
        <ProgressBar progress={progressPercent} />
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl, alignItems: 'center', justifyContent: 'center', paddingBottom: 100 }}>
        
        <div style={{ width: '100%', maxWidth: 400, display: 'flex', justifyContent: 'flex-end', marginBottom: -spacing.md }}>
          <button 
            onClick={() => { if (hintsLeft > 0) { setShowHint(true); setHintsLeft(h => h - 1); } }}
            disabled={hintsLeft === 0 || showHint || !!feedback}
            style={{
              padding: '8px 16px', borderRadius: 20, border: 'none', background: hintsLeft > 0 ? colors.accent : colors.border,
              color: colors.onPrimary, fontWeight: 'bold', cursor: hintsLeft > 0 ? 'pointer' : 'default', opacity: hintsLeft > 0 ? 1 : 0.5
            }}
          >
            Translate ({hintsLeft} left)
          </button>
        </div>

        <div className="card" style={{ 
          width: '100%', maxWidth: 400, height: 200, display: 'flex', flexDirection: 'column', alignItems: 'center', 
          justifyContent: 'center', color: colors.primary 
        }}>
          <div style={{ fontSize: 42, fontWeight: 900 }}>{currentWord?.italian}</div>
          {showHint && <div className="fade-in" style={{ fontSize: 18, color: colors.textSecondary, marginTop: spacing.sm }}>{currentWord?.english}</div>}
        </div>

        {feedback && !feedback.isCorrect && (
          <div className="fade-in" style={{ width: '100%', maxWidth: 400 }}>
            <FeedbackMessage 
              type="incorrect" 
              message={
                <>
                  <div>{feedback.message}</div>
                  <div style={{ marginTop: spacing.sm, fontSize: 14, fontWeight: 'normal', color: colors.textSecondary }}>
                    {feedback.explanation}
                  </div>
                </>
              } 
            />
            <PrimaryButton label="Next" onPress={nextWord} />
          </div>
        )}
        
        {feedback && feedback.isCorrect && (
          <div className="fade-in" style={{ width: '100%', maxWidth: 400 }}>
            <FeedbackMessage type="correct" message={feedback.message} />
          </div>
        )}

        {!feedback && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md, width: '100%', maxWidth: 400 }}>
            <div style={{ display: 'flex', gap: spacing.md }}>
              <button 
                onClick={() => setSelectedGender('m')}
                style={{ 
                  flex: 1, padding: spacing.xl, borderRadius: 20, border: `3px solid ${selectedGender === 'm' ? colors.primary : colors.border}`, 
                  background: selectedGender === 'm' ? 'rgba(33, 150, 243, 0.1)' : colors.surface, 
                  color: selectedGender === 'm' ? colors.primary : colors.textSecondary, 
                  fontWeight: '900', cursor: 'pointer', fontSize: 18, transition: 'all 0.2s'
                }}
              >
                MASCULINE
              </button>
              <button 
                onClick={() => setSelectedGender('f')}
                style={{ 
                  flex: 1, padding: spacing.xl, borderRadius: 20, border: `3px solid ${selectedGender === 'f' ? colors.accent : colors.border}`, 
                  background: selectedGender === 'f' ? 'rgba(233, 30, 99, 0.1)' : colors.surface, 
                  color: selectedGender === 'f' ? colors.accent : colors.textSecondary, 
                  fontWeight: '900', cursor: 'pointer', fontSize: 18, transition: 'all 0.2s'
                }}
              >
                FEMININE
              </button>
            </div>
            <PrimaryButton label="Check" onPress={handleCheck} disabled={!selectedGender} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, fontWeight: 800 }}>
              Tip: Press 1-2 to select, Enter to submit
            </p>
          </div>
        )}
      </div>

      <div style={{ marginTop: 'auto' }}>
        <PrimaryButton label="Quit" onPress={() => setGameState('lobby')} variant="secondary" />
      </div>
    </Screen>
  );
};
