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

import { useUserSettingsStore } from '../store/userSettingsStore';
import { audioService } from '../lib/audioService';

export const GenderGame: React.FC = () => {
  const navigate = useNavigate();
  const { genderGame, unlockLevel, updateHighScore } = useGameStore();
  const { plan, isValid } = useSubscriptionStore();
  const isPremium = plan !== 'free' && isValid;
  
  const { feedbackLanguage, soundEnabled } = useUserSettingsStore();
  const isIt = feedbackLanguage === 'it';
  
  const [level, setLevel] = useState(1);
  const [gameState, setGameState] = useState<'lobby' | 'playing' | 'gameOver' | 'win'>('lobby');
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [feedback, setFeedback] = useState<{ isCorrect: boolean, message: string, explanation?: string } | null>(null);
  
  const [selectedArticle, setSelectedArticle] = useState<string | null>(null);
  const [hintsLeft, setHintsLeft] = useState(3);
  const [showHint, setShowHint] = useState(false);

  const wordsForLevel = useMemo(() => {
    const m = genderWords.filter(w => w.difficulty === level && w.gender === 'm');
    const f = genderWords.filter(w => w.difficulty === level && w.gender === 'f');
    const selectedM = shuffle([...m]).slice(0, 5);
    const selectedF = shuffle([...f]).slice(0, 5);
    return shuffle([...selectedM, ...selectedF]);
  }, [level]);

  const currentWord = wordsForLevel[currentIndex];

  const nextWord = useCallback(() => {
    setFeedback(null);
    setSelectedArticle(null);
    setShowHint(false);
    if (currentIndex + 1 < wordsForLevel.length) {
      setCurrentIndex(i => i + 1);
    } else {
      setGameState('win');
      updateHighScore('genderGame', score);
      if (score >= 80 && level < 3) {
        unlockLevel('genderGame', level + 1);
      }
    }
  }, [currentIndex, wordsForLevel.length, score, level, updateHighScore, unlockLevel]);

  const handleCheck = useCallback(() => {
    if (feedback || !currentWord || !selectedArticle) return;

    if (currentWord.article === selectedArticle) {
      if (soundEnabled) audioService.playCorrect();
      setScore(s => s + 10);
      setFeedback({ isCorrect: true, message: isIt ? 'Ottimo!' : 'Excellent!' });
      setTimeout(() => {
        nextWord();
      }, 800);
    } else {
      if (soundEnabled) audioService.playIncorrect();
      setLives(l => l - 1);
      const explanation = getWrongAnswerExplanation({
        type: 'gender',
        italian: currentWord.word,
        correctAnswer: currentWord.gender
      });
      setFeedback({ 
        isCorrect: false, 
        message: isIt ? `Sbagliato. Si dice "${currentWord.article} ${currentWord.word}".` : `Wrong. It is "${currentWord.article} ${currentWord.word}".`,
        explanation: `${explanation} ${isIt ? 'Traduzione' : 'Translation'}: ${currentWord.translation}`
      });
    }
  }, [feedback, currentWord, selectedArticle, nextWord]);

  useEffect(() => {
    if (lives <= 0) {
      setGameState('gameOver');
      updateHighScore('genderGame', score);
    }
  }, [lives, score, updateHighScore]);

  useEffect(() => {
    const articles = ['il', 'lo', "l'", 'la', 'i', 'gli', 'le'];
    const handleKeyDown = (e: KeyboardEvent) => {
      if (gameState !== 'playing') return;
      const num = parseInt(e.key);
      if (num >= 1 && num <= articles.length) {
        setSelectedArticle(articles[num - 1]);
      }
      if (e.key === 'Enter') {
        e.preventDefault();
        if (feedback && !feedback.isCorrect) {
          nextWord();
        } else if (!feedback && selectedArticle) {
          handleCheck();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [gameState, feedback, selectedArticle, handleCheck, nextWord]);

  if (gameState === 'lobby') {
    return (
      <Screen>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{isIt ? 'Maschile o Femminile?' : 'Masculine or Feminine?'}</h1>
          <p style={{ color: colors.textSecondary }}>{isIt ? 'Indovina il genere dei sostantivi.' : 'Guess the gender of the nouns.'}</p>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {[1, 2, 3].map(l => {
            const isPremiumLocked = l > 1 && !isPremium;
            const isUnlocked = l <= genderGame.unlockedLevels && !isPremiumLocked;
            
            const handleClick = () => {
              if (isPremiumLocked) {
                navigate('/premium');
              } else if (isUnlocked) {
                if (soundEnabled) audioService.playClick();
                setLevel(l); 
                setGameState('playing'); 
                setScore(0); 
                setLives(3); 
                setCurrentIndex(0); 
                setHintsLeft(3); 
                setShowHint(false); 
                setSelectedArticle(null); 
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
                  <h3 style={{ margin: 0, color: colors.primary }}>{isIt ? 'Livello' : 'Level'} {l}</h3>
                  <p style={{ margin: 4, fontSize: 14, color: colors.textSecondary }}>
                    {l === 1 ? (isIt ? 'Nomi comuni (o/a)' : 'Common nouns (o/a)') : l === 2 ? (isIt ? 'Nomi che finiscono in -e' : 'Nouns ending in -e') : (isIt ? 'Eccezioni difficili' : 'Tricky exceptions')}
                  </p>
                </div>
                {isPremiumLocked && <span style={{ fontSize: 24 }}>👑</span>}
                {!isPremiumLocked && !isUnlocked && <span>🔒</span>}
              </button>
            );
          })}
          <PrimaryButton label={isIt ? "Torna ai Giochi" : "Back to Games"} onPress={() => navigate('/games')} variant="secondary" />
        </div>
      </Screen>
    );
  }

  if (gameState === 'gameOver' || gameState === 'win') {
    if (gameState === 'win' && soundEnabled) audioService.playComplete();
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <div className="card fade-in" style={{ padding: spacing.xl, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h1 style={{ fontSize: 48 }}>{gameState === 'win' ? (isIt ? '🎉 Bravissimo!' : '🎉 Well done!') : (isIt ? '😢 Fine Partita' : '😢 Game Over')}</h1>
          <p style={{ fontSize: 24, color: colors.textSecondary }}>{isIt ? 'Punteggio Finale' : 'Final Score'}: {score} / 100</p>
          <PrimaryButton label={isIt ? "Gioca Ancora" : "Play Again"} onPress={() => setGameState('lobby')} />
          <PrimaryButton label={isIt ? "Esci" : "Exit"} onPress={() => navigate('/games')} variant="secondary" />
        </div>
      </Screen>
    );
  }

  const progressPercent = Math.min(100, (currentIndex / wordsForLevel.length) * 100);

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
          <div style={{ fontSize: 42, fontWeight: 900 }}>
            <span style={{ color: colors.accent, textDecoration: 'underline' }}>{selectedArticle || '___'}</span> {currentWord?.word}
          </div>
          {showHint && <div className="fade-in" style={{ fontSize: 18, color: colors.textSecondary, marginTop: spacing.sm }}>{currentWord?.translation}</div>}
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
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: spacing.sm }}>
              {['il', 'lo', "l'", 'la', 'i', 'gli', 'le'].map((art) => (
                <button 
                  key={art}
                  onClick={() => setSelectedArticle(art)}
                  style={{ 
                    padding: spacing.md, borderRadius: 12, border: `3px solid ${selectedArticle === art ? colors.primary : colors.border}`, 
                    background: selectedArticle === art ? 'rgba(33, 150, 243, 0.1)' : colors.surface, 
                    color: selectedArticle === art ? colors.primary : colors.textSecondary, 
                    fontWeight: '900', cursor: 'pointer', fontSize: 16, transition: 'all 0.2s'
                  }}
                >
                  {art}
                </button>
              ))}
            </div>
            <PrimaryButton label="Check" onPress={handleCheck} disabled={!selectedArticle} />
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: 0, fontWeight: 800 }}>
              Tip: Press 1-7 to select, Enter to submit
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
