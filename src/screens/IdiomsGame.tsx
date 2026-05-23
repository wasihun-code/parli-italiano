import React, { useState, useMemo, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import idiomsData from '@shared/data/idiomsGame.json';
import { useGameStore } from '@shared/store/gameStore';
import { PrimaryButton } from '../components/PrimaryButton';
import { shuffle } from '@shared/utils/trainingUi';
import { ProgressBar } from '../components/ProgressBar';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { ShortcutHelp } from '../components/ShortcutHelp';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';

export const IdiomsGame: React.FC = () => {
  const navigate = useNavigate();
  const { idiomsGame, unlockLevel, updateHighScore } = useGameStore();
  
  const [level, setLevel] = useState(1);
  const [gameState, setGameState] = useState<'lobby' | 'playing' | 'gameOver' | 'win'>('lobby');
  const [score, setScore] = useState(0);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<{ isCorrect: boolean, explanation?: string } | null>(null);

  const [hintsLeft, setHintsLeft] = useState(3);
  const [showHint, setShowHint] = useState(false);

  const itemsForLevel = useMemo(() => {
    const filtered = idiomsData.filter(s => s.difficulty === level);
    return shuffle([...filtered]).slice(0, 10);
  }, [level]);

  const currentItem = itemsForLevel[currentIndex];
  
  const options = useMemo(() => {
    if (!currentItem) return [];
    // pick 3 distractors from the same level
    const sameLevel = idiomsData.filter(s => s.difficulty === level && s.id !== currentItem.id);
    const distractors = shuffle([...sameLevel]).slice(0, 3).map(s => s.meaning);
    return shuffle([currentItem.meaning, ...distractors]);
  }, [currentItem, level]);

  const nextQuestion = useCallback(() => {
    setFeedback(null);
    setSelectedOption(null);
    setShowHint(false);
    if (currentIndex + 1 < itemsForLevel.length) {
      setCurrentIndex(i => i + 1);
    } else {
      setGameState('win');
      updateHighScore('idiomsGame', score);
      if (score >= 100 && level < 3) {
        unlockLevel('idiomsGame', level + 1);
      }
    }
  }, [currentIndex, itemsForLevel.length, score, level, updateHighScore, unlockLevel]);

  const handleCheck = useCallback(() => {
    if (feedback || !currentItem || !selectedOption) return;

    if (selectedOption === currentItem.meaning) {
      setScore(s => s + 15);
      setFeedback({ isCorrect: true });
      setTimeout(() => {
        nextQuestion();
      }, 800);
    } else {
      const explanation = getWrongAnswerExplanation({
        type: 'idioms',
        italian: currentItem.italian,
        correctAnswer: currentItem.meaning
      });
      setFeedback({ isCorrect: false, explanation });
    }
  }, [feedback, currentItem, selectedOption, nextQuestion]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (gameState !== 'playing') return;
      if (!feedback) {
        if (e.key === '1' && options[0]) setSelectedOption(options[0]);
        if (e.key === '2' && options[1]) setSelectedOption(options[1]);
        if (e.key === '3' && options[2]) setSelectedOption(options[2]);
        if (e.key === '4' && options[3]) setSelectedOption(options[3]);
      }
      if (e.key === 'Enter') {
        e.preventDefault();
        if (feedback && !feedback.isCorrect) {
          nextQuestion();
        } else if (!feedback && selectedOption) {
          handleCheck();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameState, feedback, options, selectedOption, handleCheck, nextQuestion]);

  if (gameState === 'lobby') {
    return (
      <Screen>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Espressioni</h1>
          <p style={{ color: colors.textSecondary }}>Guess the meaning of Italian idioms.</p>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {[1, 2, 3].map(l => {
            const isUnlocked = l <= idiomsGame.unlockedLevels;
            return (
              <button
                key={l}
                disabled={!isUnlocked}
                onClick={() => { 
                  setLevel(l); setGameState('playing'); setScore(0); setCurrentIndex(0); 
                  setSelectedOption(null); setFeedback(null); setHintsLeft(3); setShowHint(false); 
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
                    {l === 1 ? 'Common idioms' : l === 2 ? 'Intermediate expressions' : 'Advanced metaphors'}
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

  if (gameState === 'win') {
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <div className="card fade-in" style={{ padding: spacing.xl, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h1 style={{ fontSize: 48 }}>🎉 Vittoria!</h1>
          <p style={{ fontSize: 24, color: colors.textSecondary }}>Final Score: {score}</p>
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
            <div style={{ color: colors.accent, fontWeight: 900 }}>Score: {score}</div>
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
          padding: spacing.xl, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center'
        }}>
          <div style={{ fontSize: 28, fontWeight: 900, color: colors.primary }}>{currentItem?.italian}</div>
          {showHint && <div className="fade-in" style={{ fontSize: 16, color: colors.textSecondary, marginTop: spacing.sm }}>
            <strong>Literal:</strong> {currentItem?.literal}
          </div>}
        </div>

        {!feedback ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
              {options.map((opt, i) => {
                const isSelected = opt === selectedOption;
                return (
                  <button
                    key={opt + i}
                    onClick={() => setSelectedOption(opt)}
                    style={{
                      padding: spacing.md,
                      borderRadius: 12,
                      border: `2px solid ${isSelected ? colors.primary : colors.border}`,
                      background: isSelected ? 'rgba(33, 150, 243, 0.1)' : colors.surface,
                      color: isSelected ? colors.primary : colors.textSecondary,
                      fontSize: 16,
                      fontWeight: 'bold',
                      cursor: 'pointer',
                      transition: 'all 0.2s',
                      textAlign: 'left'
                    }}
                  >
                    {opt}
                  </button>
                );
              })}
            </div>
            <PrimaryButton label="Check" onPress={handleCheck} disabled={!selectedOption} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, fontWeight: 800 }}>
              Tip: Press 1-4 to select, Enter to submit
            </p>
          </div>
        ) : (
          <div className="fade-in" style={{ textAlign: 'center', marginTop: spacing.md }}>
            <FeedbackMessage 
              type={feedback.isCorrect ? 'correct' : 'incorrect'} 
              message={
                feedback.isCorrect 
                  ? 'Correct!' 
                  : (
                    <>
                      <div>Incorrect</div>
                      <div style={{ marginTop: spacing.sm, fontSize: 14, fontWeight: 'normal', color: colors.textSecondary }}>
                        {feedback.explanation}
                      </div>
                      <div style={{ marginTop: spacing.sm, fontSize: 16, fontWeight: 'bold' }}>
                        Meaning: {currentItem?.meaning} ({currentItem?.literal})
                      </div>
                    </>
                  )
              }
            />
            {!feedback.isCorrect && <PrimaryButton label="Next" onPress={nextQuestion} />}
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, marginTop: 8, fontWeight: 800 }}>
              Tip: Press Enter to continue
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
