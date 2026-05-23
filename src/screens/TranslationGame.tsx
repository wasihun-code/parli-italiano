import React, { useState, useMemo, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { translationSentences } from '@shared/data/translationSentences';
import { useGameStore } from '@shared/store/gameStore';
import { PrimaryButton } from '../components/PrimaryButton';
import { shuffle } from '@shared/utils/trainingUi';
import { normalizeString, levenshteinDistance } from '@shared/utils/string';
import { ProgressBar } from '../components/ProgressBar';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { ShortcutHelp } from '../components/ShortcutHelp';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { audioService } from '../lib/audioService';

export const TranslationGame: React.FC = () => {
  const navigate = useNavigate();
  const { translationGame, unlockLevel, updateHighScore } = useGameStore();
  const { feedbackLanguage, soundEnabled } = useUserSettingsStore();
  const isIt = feedbackLanguage === 'it';
  
  const [level, setLevel] = useState(1);
  const [gameState, setGameState] = useState<'lobby' | 'playing' | 'gameOver' | 'win'>('lobby');
  const [score, setScore] = useState(0);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [typedAnswer, setTypedAnswer] = useState('');
  const [feedback, setFeedback] = useState<{ isCorrect: boolean, isNearly: boolean, correctAnswer: string, explanation?: string } | null>(null);

  const sentencesForLevel = useMemo(() => {
    const filtered = translationSentences.filter(s => s.difficulty === level);
    return shuffle([...filtered]).slice(0, 15);
  }, [level]);

  const currentItem = sentencesForLevel[currentIndex];

  const handleCheck = useCallback(() => {
    if (feedback || !currentItem || !typedAnswer.trim()) return;

    const normSubmitted = normalizeString(typedAnswer);
    const normExpected = normalizeString(currentItem.english);
    
    const isCorrect = normSubmitted === normExpected;
    const isNearly = !isCorrect && normExpected.length >= 4 && levenshteinDistance(normSubmitted, normExpected) <= 1;

    if (isCorrect || isNearly) {
      if (soundEnabled) audioService.playCorrect();
      setScore(s => s + 20);
      setFeedback({ isCorrect: true, isNearly, correctAnswer: currentItem.english });
    } else {
      if (soundEnabled) audioService.playIncorrect();
      const explanation = getWrongAnswerExplanation({
        type: 'translation',
        italian: currentItem.italian,
        correctAnswer: currentItem.english
      });
      setFeedback({ isCorrect: false, isNearly: false, correctAnswer: currentItem.english, explanation });
    }
  }, [feedback, currentItem, typedAnswer, soundEnabled]);

  const nextSentence = useCallback(() => {
    setFeedback(null);
    setTypedAnswer('');
    if (currentIndex + 1 < sentencesForLevel.length) {
      setCurrentIndex(i => i + 1);
    } else {
      if (soundEnabled) audioService.playComplete();
      setGameState('win');
      updateHighScore('translationGame', score);
      if (score >= 100 && level < 3) {
        if (soundEnabled) audioService.playLevelUp();
        unlockLevel('translationGame', level + 1);
      }
    }
  }, [currentIndex, sentencesForLevel.length, score, level, updateHighScore, unlockLevel, soundEnabled]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (gameState !== 'playing') return;
      if (e.key === 'Enter') {
        e.preventDefault();
        if (feedback) {
          nextSentence();
        } else if (typedAnswer.trim()) {
          handleCheck();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameState, feedback, typedAnswer, handleCheck, nextSentence]);


  if (gameState === 'lobby') {
    return (
      <Screen>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{isIt ? 'Traduzione' : 'Translation'}</h1>
          <p style={{ color: colors.textSecondary }}>{isIt ? 'Traduci le frasi italiane in inglese.' : 'Translate the Italian sentences to English.'}</p>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {[1, 2, 3].map(l => {
            const isUnlocked = l <= translationGame.unlockedLevels;
            return (
              <button
                key={l}
                disabled={!isUnlocked}
                onClick={() => { 
                  if (soundEnabled) audioService.playClick();
                  setLevel(l); setGameState('playing'); setScore(0); setCurrentIndex(0); setTypedAnswer(''); setFeedback(null); 
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
                  <h3 style={{ margin: 0, color: colors.primary }}>{isIt ? 'Livello' : 'Level'} {l}</h3>
                  <p style={{ margin: 4, fontSize: 14, color: colors.textSecondary }}>
                    {l === 1 ? (isIt ? 'Frasi brevi A1' : 'Short A1 sentences') : l === 2 ? (isIt ? 'Frasi di media lunghezza' : 'Medium length sentences') : (isIt ? 'Frasi complesse A2' : 'Complex A2 sentences')}
                  </p>
                </div>
                {!isUnlocked && <span>🔒</span>}
              </button>
            );
          })}
          <PrimaryButton label={isIt ? "Torna ai Giochi" : "Back to Games"} onPress={() => navigate('/games')} variant="secondary" />
        </div>
      </Screen>
    );
  }

  if (gameState === 'win') {
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <div className="card fade-in" style={{ padding: spacing.xl, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h1 style={{ fontSize: 48 }}>{isIt ? '🎉 Livello Completato!' : '🎉 Level Completed!'}</h1>
          <p style={{ fontSize: 24, color: colors.textSecondary }}>{isIt ? 'Punteggio Finale' : 'Final Score'}: {score} / 100</p>
          <PrimaryButton label={isIt ? "Gioca Ancora" : "Play Again"} onPress={() => setGameState('lobby')} />
          <PrimaryButton label={isIt ? "Esci" : "Exit"} onPress={() => navigate('/games')} variant="secondary" />
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
            {isIt ? 'Livello' : 'Level'} {level}
            <ShortcutHelp />
          </div>
          <div style={{ display: 'flex', gap: spacing.md }}>
            <div style={{ color: colors.accent, fontWeight: 900 }}>Score: {score} / 100</div>
          </div>
        </div>
        <ProgressBar progress={progressPercent} />
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
        <div className="card" style={{ 
          padding: spacing.xl, fontSize: 24, fontWeight: 900, color: colors.primary, textAlign: 'center'
        }}>
          {currentItem?.italian}
        </div>

        {!feedback ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <input
              autoFocus
              type="text"
              value={typedAnswer}
              onChange={e => setTypedAnswer(e.target.value)}
              placeholder={isIt ? "Traduci in inglese..." : "Translate to English..."}
              style={{
                padding: spacing.lg,
                borderRadius: 16,
                border: `2px solid ${colors.border}`,
                fontSize: 18,
                backgroundColor: colors.bg,
                outline: 'none',
              }}
            />
            <PrimaryButton label={isIt ? "Controlla" : "Check"} onPress={handleCheck} disabled={!typedAnswer.trim()} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, fontWeight: 800 }}>
              {isIt ? 'Suggerimento: Premi Invio per inviare' : 'Tip: Press Enter to submit'}
            </p>
          </div>
        ) : (
          <div className="fade-in" style={{ textAlign: 'center' }}>
            <FeedbackMessage 
              type={feedback.isCorrect ? 'correct' : 'incorrect'} 
              message={
                <>
                  <div>{feedback.isCorrect ? (feedback.isNearly ? (isIt ? 'Quasi corretto!' : 'Almost correct!') : (isIt ? 'Perfetto!' : 'Perfect!')) : (isIt ? 'Non corretto' : 'Incorrect')}</div>
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
                <p style={{ margin: 0, fontSize: 14, color: colors.textSecondary }}>{isIt ? 'Risposta corretta:' : 'Correct answer:'}</p>
                <p style={{ margin: '4px 0 0 0', fontWeight: 'bold', fontSize: 18 }}>{feedback.correctAnswer}</p>
                <p style={{ margin: '4px 0 0 0', fontSize: 14, color: colors.textSecondary }}>({currentItem?.italian})</p>
              </div>
            )}
            <PrimaryButton label={isIt ? "Avanti" : "Next"} onPress={nextSentence} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, marginTop: 8, fontWeight: 800 }}>
              {isIt ? 'Suggerimento: Premi Invio per continuare' : 'Tip: Press Enter to continue'}
            </p>
          </div>
        )}
      </div>

      <div style={{ marginTop: 'auto' }}>
        <PrimaryButton label={isIt ? "Esci" : "Quit"} onPress={() => setGameState('lobby')} variant="secondary" />
      </div>
    </Screen>
  );
};
