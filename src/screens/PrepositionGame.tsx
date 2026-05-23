import React, { useState, useMemo, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { prepositionsGame } from '@shared/data/prepositionsGame';
import { useGameStore } from '@shared/store/gameStore';
import { PrimaryButton } from '../components/PrimaryButton';
import { shuffle } from '@shared/utils/trainingUi';
import { ProgressBar } from '../components/ProgressBar';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { ShortcutHelp } from '../components/ShortcutHelp';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { audioService } from '../lib/audioService';

export const PrepositionGame: React.FC = () => {
  const navigate = useNavigate();
  const { prepositionGame, unlockLevel, updateHighScore } = useGameStore();
  const { feedbackLanguage, soundEnabled } = useUserSettingsStore();
  const isIt = feedbackLanguage === 'it';
  
  const [level, setLevel] = useState(1);
  const [gameState, setGameState] = useState<'lobby' | 'playing' | 'gameOver' | 'win'>('lobby');
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [feedback, setFeedback] = useState<{ isCorrect: boolean, explanation?: string } | null>(null);

  const [hintsLeft, setHintsLeft] = useState(3);
  const [showHint, setShowHint] = useState(false);

  const sentencesForLevel = useMemo(() => {
    const filtered = prepositionsGame.filter(s => s.difficulty === level);
    return shuffle([...filtered]).slice(0, 15);
  }, [level]);

  const currentItem = sentencesForLevel[currentIndex];
  
  const options = useMemo(() => {
    if (!currentItem) return [];
    return shuffle([currentItem.correctPreposition, ...currentItem.distractors]);
  }, [currentItem]);

  const nextSentence = useCallback(() => {
    setFeedback(null);
    setSelectedOption(null);
    setShowHint(false);
    if (currentIndex + 1 < sentencesForLevel.length) {
      setCurrentIndex(i => i + 1);
    } else {
      if (soundEnabled) audioService.playComplete();
      setGameState('win');
      updateHighScore('prepositionGame', score);
      if (score >= 100 && level < 3) {
        if (soundEnabled) audioService.playLevelUp();
        unlockLevel('prepositionGame', level + 1);
      }
    }
  }, [currentIndex, sentencesForLevel.length, score, level, updateHighScore, unlockLevel, soundEnabled]);

  const handleCheck = useCallback(() => {
    if (feedback || !currentItem || !selectedOption) return;

    if (selectedOption === currentItem.correctPreposition) {
      if (soundEnabled) audioService.playCorrect();
      setScore(s => s + 15);
      setFeedback({ isCorrect: true });
      setTimeout(() => {
        nextSentence();
      }, 800);
    } else {
      if (soundEnabled) audioService.playIncorrect();
      setLives(l => l - 1);
      const explanation = getWrongAnswerExplanation({
        type: 'preposition',
        correctAnswer: currentItem.correctPreposition
      });
      setFeedback({ isCorrect: false, explanation });
    }
  }, [feedback, currentItem, selectedOption, nextSentence, soundEnabled]);

  useEffect(() => {
    if (lives <= 0) {
      setGameState('gameOver');
      updateHighScore('prepositionGame', score);
    }
  }, [lives, score, updateHighScore]);

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
          nextSentence();
        } else if (!feedback && selectedOption) {
          handleCheck();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameState, feedback, options, selectedOption, handleCheck, nextSentence]);

  if (gameState === 'lobby') {
    return (
      <Screen>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{isIt ? 'Preposizioni' : 'Prepositions'}</h1>
          <p style={{ color: colors.textSecondary }}>{isIt ? 'Scegli la preposizione corretta.' : 'Choose the correct preposition.'}</p>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {[1, 2, 3].map(l => {
            const isUnlocked = l <= prepositionGame.unlockedLevels;
            return (
              <button
                key={l}
                disabled={!isUnlocked}
                onClick={() => { 
                  if (soundEnabled) audioService.playClick();
                  setLevel(l); setGameState('playing'); setScore(0); setLives(3); setCurrentIndex(0); 
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
                  <h3 style={{ margin: 0, color: colors.primary }}>{isIt ? 'Livello' : 'Level'} {l}</h3>
                  <p style={{ margin: 4, fontSize: 14, color: colors.textSecondary }}>
                    {l === 1 ? (isIt ? 'Preposizioni di base' : 'Basic prepositions') : l === 2 ? (isIt ? 'Città vs Nazione e Combinazioni' : 'City vs Country & Combinations') : (isIt ? 'Uso particolare e idiomatico' : 'Tricky & Idiomatic usage')}
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

  if (gameState === 'gameOver' || gameState === 'win') {
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <div className="card fade-in" style={{ padding: spacing.xl, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h1 style={{ fontSize: 48 }}>{gameState === 'win' ? (isIt ? '🎉 Vittoria!' : '🎉 Victory!') : (isIt ? '😢 Riprova!' : '😢 Try Again!')}</h1>
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
            <div style={{ color: colors.accent, fontWeight: 900 }}>{isIt ? 'Punteggio' : 'Score'}: {score} / 100</div>
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
            {isIt ? 'Traduci' : 'Translate'} ({hintsLeft} {isIt ? 'rimasti' : 'left'})
          </button>
        </div>

        <div className="card" style={{ 
          padding: spacing.xl, display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center'
        }}>
          <div style={{ fontSize: 28, fontWeight: 900, color: colors.primary }}>{currentItem?.sentenceItalian}</div>
          {showHint && <div className="fade-in" style={{ fontSize: 16, color: colors.textSecondary, marginTop: spacing.sm }}>{currentItem?.english}</div>}
        </div>

        {!feedback ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: spacing.md }}>
              {options.map((opt) => {
                const isSelected = opt === selectedOption;
                return (
                  <button
                    key={opt}
                    onClick={() => setSelectedOption(opt)}
                    style={{
                      padding: spacing.xl,
                      borderRadius: 16,
                      border: `2px solid ${isSelected ? colors.primary : colors.border}`,
                      background: isSelected ? 'rgba(33, 150, 243, 0.1)' : colors.surface,
                      color: isSelected ? colors.primary : colors.textSecondary,
                      fontSize: 22,
                      fontWeight: 'bold',
                      cursor: 'pointer',
                      transition: 'all 0.2s'
                    }}
                  >
                    {opt}
                  </button>
                );
              })}
            </div>
            <PrimaryButton label={isIt ? "Controlla" : "Check"} onPress={handleCheck} disabled={!selectedOption} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, fontWeight: 800 }}>
              {isIt ? 'Suggerimento: Premi 1-4 per selezionare, Invio per inviare' : 'Tip: Press 1-4 to select, Enter to submit'}
            </p>
          </div>
        ) : (
          <div className="fade-in" style={{ textAlign: 'center', marginTop: spacing.md }}>
            <FeedbackMessage 
              type={feedback.isCorrect ? 'correct' : 'incorrect'} 
              message={
                feedback.isCorrect 
                  ? (isIt ? 'Corretto!' : 'Correct!') 
                  : (
                    <>
                      <div>{isIt ? 'Non corretto' : 'Incorrect'}</div>
                      <div style={{ marginTop: spacing.sm, fontSize: 14, fontWeight: 'normal', color: colors.textSecondary }}>
                        {feedback.explanation}
                      </div>
                    </>
                  )
              }
            />
            {!feedback.isCorrect && (
              <div className="card" style={{ marginBottom: spacing.md, padding: spacing.md }}>
                <p style={{ margin: 0, fontSize: 14, color: colors.textSecondary }}>{isIt ? 'Risposta corretta:' : 'Correct answer:'}</p>
                <p style={{ margin: '4px 0 0 0', fontWeight: 'bold', fontSize: 18 }}>{currentItem.correctPreposition}</p>
                <p style={{ margin: '8px 0 0 0', fontSize: 16, color: colors.primary }}>{currentItem.english}</p>
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
