import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { useProgressStore } from '../store/progressStore';
import { useSrsStore } from '../store/srsStore';
import { useGameStore } from '../store/gameStore';
import { useGrammarStore } from '../store/grammarStore';

export const SettingsScreen: React.FC = () => {
  const navigate = useNavigate();
  const { 
    feedbackLanguage, setFeedbackLanguage, 
    soundEnabled, setSoundEnabled,
    flashcardDirection, setFlashcardDirection,
    ttsProvider, setTtsProvider
  } = useUserSettingsStore();
  
  const resetProgress = useProgressStore(state => state.resetProgress);
  const resetSrs = useSrsStore(state => state.reset);
  const resetGames = useGameStore(state => state.resetProgress);
  const resetGrammar = useGrammarStore(state => state.resetProgress);

  const handleReset = () => {
    if (window.confirm('Sei sicuro di voler resettare tutti i progressi? Questa azione non può essere annullata.')) {
      resetProgress();
      resetSrs();
      resetGames();
      resetGrammar();
      alert('Tutti i progressi sono stati resettati.');
      navigate('/');
    }
  };

  return (
    <Screen style={{ backgroundColor: colors.bg }}>
      <div style={{ maxWidth: 600, margin: '0 auto', width: '100%' }}>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Impostazioni ⚙️</h1>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          {/* Feedback Language */}
          <div className="card" style={{ padding: spacing.lg }}>
            <h3 style={{ color: colors.primary, marginBottom: spacing.md }}>Lingua Feedback</h3>
            <div style={{ display: 'flex', gap: spacing.md }}>
              <button
                onClick={() => setFeedbackLanguage('it')}
                style={{
                  flex: 1,
                  padding: spacing.md,
                  borderRadius: 12,
                  border: feedbackLanguage === 'it' ? `2px solid ${colors.accent}` : `1px solid ${colors.border}`,
                  backgroundColor: feedbackLanguage === 'it' ? 'rgba(212, 163, 115, 0.1)' : 'transparent',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                Italiano
              </button>
              <button
                onClick={() => setFeedbackLanguage('en')}
                style={{
                  flex: 1,
                  padding: spacing.md,
                  borderRadius: 12,
                  border: feedbackLanguage === 'en' ? `2px solid ${colors.accent}` : `1px solid ${colors.border}`,
                  backgroundColor: feedbackLanguage === 'en' ? 'rgba(212, 163, 115, 0.1)' : 'transparent',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                Inglese
              </button>
            </div>
          </div>

          {/* Sound */}
          <div className="card" style={{ padding: spacing.lg, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h3 style={{ color: colors.primary, margin: 0 }}>Suoni</h3>
            <button
              onClick={() => setSoundEnabled(!soundEnabled)}
              style={{
                width: 60,
                height: 30,
                borderRadius: 15,
                backgroundColor: soundEnabled ? colors.success : colors.border,
                border: 'none',
                position: 'relative',
                cursor: 'pointer',
                transition: 'background-color 0.2s'
              }}
            >
              <div style={{
                width: 24,
                height: 24,
                borderRadius: 12,
                backgroundColor: 'white',
                position: 'absolute',
                top: 3,
                left: soundEnabled ? 33 : 3,
                transition: 'left 0.2s'
              }} />
            </button>
          </div>

          {/* TTS Provider */}
          <div className="card" style={{ padding: spacing.lg }}>
            <h3 style={{ color: colors.primary, marginBottom: spacing.md }}>Voce (TTS)</h3>
            <div style={{ display: 'flex', gap: spacing.md }}>
              <button
                onClick={() => setTtsProvider('api')}
                style={{
                  flex: 1,
                  padding: spacing.md,
                  borderRadius: 12,
                  border: ttsProvider === 'api' ? `2px solid ${colors.accent}` : `1px solid ${colors.border}`,
                  backgroundColor: ttsProvider === 'api' ? 'rgba(212, 163, 115, 0.1)' : 'transparent',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                Alta Qualità (API)
              </button>
              <button
                onClick={() => setTtsProvider('browser')}
                style={{
                  flex: 1,
                  padding: spacing.md,
                  borderRadius: 12,
                  border: ttsProvider === 'browser' ? `2px solid ${colors.accent}` : `1px solid ${colors.border}`,
                  backgroundColor: ttsProvider === 'browser' ? 'rgba(212, 163, 115, 0.1)' : 'transparent',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                Browser
              </button>
            </div>
          </div>

          {/* Flashcard Direction */}
          <div className="card" style={{ padding: spacing.lg }}>
            <h3 style={{ color: colors.primary, marginBottom: spacing.md }}>Direzione Flashcard</h3>
            <div style={{ display: 'flex', gap: spacing.md }}>
              <button
                onClick={() => setFlashcardDirection('en-it')}
                style={{
                  flex: 1,
                  padding: spacing.md,
                  borderRadius: 12,
                  border: flashcardDirection === 'en-it' ? `2px solid ${colors.accent}` : `1px solid ${colors.border}`,
                  backgroundColor: flashcardDirection === 'en-it' ? 'rgba(212, 163, 115, 0.1)' : 'transparent',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                EN → IT
              </button>
              <button
                onClick={() => setFlashcardDirection('it-en')}
                style={{
                  flex: 1,
                  padding: spacing.md,
                  borderRadius: 12,
                  border: flashcardDirection === 'it-en' ? `2px solid ${colors.accent}` : `1px solid ${colors.border}`,
                  backgroundColor: flashcardDirection === 'it-en' ? 'rgba(212, 163, 115, 0.1)' : 'transparent',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                IT → EN
              </button>
            </div>
          </div>

          {/* Reset Progress */}
          <div className="card" style={{ padding: spacing.lg }}>
            <h3 style={{ color: colors.error, marginBottom: spacing.sm }}>Area Pericolosa</h3>
            <p style={{ fontSize: 14, color: colors.textSecondary, marginBottom: spacing.md }}>
              Resetta tutti i tuoi progressi, XP e streak. Questa operazione non può essere annullata.
            </p>
            <button
              onClick={handleReset}
              style={{
                width: '100%',
                padding: spacing.md,
                borderRadius: 12,
                border: `2px solid ${colors.error}`,
                backgroundColor: 'transparent',
                color: colors.error,
                fontWeight: 900,
                cursor: 'pointer'
              }}
            >
              RESETTA TUTTI I PROGRESSI
            </button>
          </div>
        </div>

        <div style={{ marginTop: spacing.xl, marginBottom: spacing.xxl }}>
          <PrimaryButton label="Torna alla Home" onPress={() => navigate('/')} variant="secondary" />
        </div>
      </div>
    </Screen>
  );
};
