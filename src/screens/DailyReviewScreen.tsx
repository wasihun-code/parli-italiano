import React, { useState, useMemo, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { ReviewQueueService, ReviewItem } from '../services/reviewQueueService';
import { colors } from '../theme/colors';
import { spacing } from '../theme/spacing';

type ViewState = 'loading' | 'intro' | 'reviewing' | 'outro';

export const DailyReviewScreen: React.FC = () => {
  const navigate = useNavigate();
  
  const [viewState, setViewState] = useState<ViewState>('loading');
  const [dueItems, setDueItems] = useState<ReviewItem[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isRevealed, setIsRevealed] = useState(false);
  const [sessionResults, setSessionResults] = useState<{ id: string; feedback: string }[]>([]);

  useEffect(() => {
    async function loadQueue() {
      const queue = await ReviewQueueService.getDailyQueue();
      setDueItems(queue);
      setViewState('intro');
    }
    loadQueue();
  }, []);

  const currentItem = dueItems[currentIndex];

  const stats = useMemo(() => {
    return {
      vocabulary: dueItems.filter(i => i.type === 'vocabulary').length,
      phrases: dueItems.filter(i => i.type === 'phrase').length,
      sentences: dueItems.filter(i => i.type === 'sentence').length,
      total: dueItems.length
    };
  }, [dueItems]);

  const handleStartSession = () => {
    if (dueItems.length > 0) {
      setViewState('reviewing');
    } else {
      navigate('/');
    }
  };

  const handleFeedback = async (feedback: 'again' | 'hard' | 'good' | 'easy') => {
    if (!currentItem) return;

    // Record in global progress
    await ReviewQueueService.recordReviewResult(currentItem.globalId, feedback.toUpperCase() as any);

    // Record for session summary
    setSessionResults(prev => [...prev, { id: currentItem.globalId, feedback }]);

    // Move to next or finish
    if (currentIndex < dueItems.length - 1) {
      setCurrentIndex(prev => prev + 1);
      setIsRevealed(false);
    } else {
      setViewState('outro');
    }
  };

  const playAudio = () => {
    if (currentItem) {
      void Tts.speak(currentItem.italian);
    }
  };

  useEffect(() => {
    if (viewState === 'reviewing' && isRevealed) {
      playAudio();
    }
  }, [isRevealed, viewState]);

  // --- RENDERING ---

  if (viewState === 'loading') {
    return <Screen style={{ justifyContent: 'center', alignItems: 'center' }}><div className="fade-in">☕ Preparazione ripasso...</div></Screen>;
  }

  if (viewState === 'intro') {
    return (
      <Screen style={{ justifyContent: 'center', alignItems: 'center', padding: spacing.xl }}>
        <div style={{ textAlign: 'center', maxWidth: 400 }}>
          <div style={{ fontSize: 64, marginBottom: spacing.md }}>🧠</div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, marginBottom: spacing.sm }}>
            Pronto per il ripasso?
          </h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginBottom: spacing.xl }}>
            Hai {stats.total} elementi da ripassare oggi per mantenere la tua memoria al 100%.
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: spacing.md, marginBottom: spacing.xl }}>
            <div className="card" style={{ padding: spacing.md, backgroundColor: colors.chipBg }}>
              <div style={{ fontSize: 24, fontWeight: 900, color: colors.primary }}>{stats.vocabulary}</div>
              <div style={{ fontSize: 12, fontWeight: 800, color: colors.textSecondary, textTransform: 'uppercase' }}>Parole</div>
            </div>
            <div className="card" style={{ padding: spacing.md, backgroundColor: colors.chipBg }}>
              <div style={{ fontSize: 24, fontWeight: 900, color: colors.primary }}>{stats.phrases + stats.sentences}</div>
              <div style={{ fontSize: 12, fontWeight: 800, color: colors.textSecondary, textTransform: 'uppercase' }}>Frasi</div>
            </div>
          </div>

          <PrimaryButton label="Inizia Sessione" onPress={handleStartSession} />
          <button 
            onClick={() => navigate('/')}
            style={{ marginTop: spacing.lg, background: 'none', border: 'none', color: colors.textSecondary, fontWeight: 700, cursor: 'pointer' }}
          >
            Magari più tardi
          </button>
        </div>
      </Screen>
    );
  }

  if (viewState === 'reviewing' && currentItem) {
    const progress = ((currentIndex) / dueItems.length) * 100;

    return (
      <Screen>
        {/* Progress Bar */}
        <div style={{ height: 6, backgroundColor: colors.chipBg, borderRadius: 3, marginBottom: spacing.xl }}>
          <div style={{ height: '100%', width: `${progress}%`, backgroundColor: colors.accent, borderRadius: 3, transition: 'width 0.3s' }} />
        </div>

        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          <div 
            onClick={() => setIsRevealed(true)}
            className="card" 
            style={{ 
              minHeight: 300, 
              display: 'flex', 
              flexDirection: 'column', 
              alignItems: 'center', 
              justifyContent: 'center',
              padding: spacing.xl,
              backgroundColor: isRevealed ? colors.surface : colors.chipBg,
              cursor: isRevealed ? 'default' : 'pointer',
              border: `3px solid ${isRevealed ? colors.accent : 'transparent'}`,
              textAlign: 'center'
            }}
          >
            <span style={{ fontSize: 12, fontWeight: 900, color: colors.accent, textTransform: 'uppercase', letterSpacing: 2, marginBottom: spacing.md }}>
              {currentItem.type === 'vocabulary' ? 'VOCABOLARIO' : 'FRASE'}
            </span>
            
            <h2 style={{ fontSize: 42, fontWeight: 900, color: colors.primary, margin: 0 }}>
              {currentItem.italian}
            </h2>

            {isRevealed ? (
              <div className="fade-in" style={{ marginTop: spacing.xl, textAlign: 'center' }}>
                <div style={{ height: 2, width: 40, backgroundColor: colors.border, margin: '0 auto 24px' }} />
                <h3 style={{ fontSize: 28, fontWeight: 700, color: colors.textSecondary, margin: 0 }}>
                  {currentItem.english}
                </h3>
              </div>
            ) : (
              <div style={{ marginTop: spacing.xl, color: colors.textSecondary, fontWeight: 700, fontSize: 14 }}>
                Tocca per rivelare
              </div>
            )}
          </div>
        </div>

        {/* Feedback Buttons */}
        <div style={{ marginTop: spacing.xl }}>
          {isRevealed ? (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: spacing.md }}>
              <FeedbackButton label="Ancora" sublabel="<1m" color={colors.error} onClick={() => handleFeedback('again')} />
              <FeedbackButton label="Difficile" sublabel="2g" color={colors.warning} onClick={() => handleFeedback('hard')} />
              <FeedbackButton label="Bene" sublabel="4g" color={colors.primary} onClick={() => handleFeedback('good')} />
              <FeedbackButton label="Facile" sublabel="7g" color={colors.success} onClick={() => handleFeedback('easy')} />
            </div>
          ) : (
            <PrimaryButton label="Ascolta" variant="secondary" onPress={playAudio} />
          )}
        </div>
      </Screen>
    );
  }

  if (viewState === 'outro') {
    return (
      <Screen style={{ justifyContent: 'center', alignItems: 'center', padding: spacing.xl }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: 64, marginBottom: spacing.md }}>🎉</div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, marginBottom: spacing.sm }}>
            Sessione Completata!
          </h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginBottom: spacing.xl }}>
            Hai ripassato {sessionResults.length} elementi. Ottimo lavoro!
          </p>

          <div style={{ backgroundColor: colors.chipBg, padding: spacing.lg, borderRadius: 16, marginBottom: spacing.xl }}>
             <div style={{ fontSize: 14, fontWeight: 800, color: colors.primary }}>
               PRECISIONE SESSIONE: {Math.round((sessionResults.filter(r => r.feedback !== 'again').length / sessionResults.length) * 100)}%
             </div>
          </div>

          <PrimaryButton label="Torna alla Home" onPress={() => navigate('/')} />
        </div>
      </Screen>
    );
  }

  return null;
};

const FeedbackButton: React.FC<{ label: string; sublabel: string; color: string; onClick: () => void }> = ({ label, sublabel, color, onClick }) => (
  <button
    onClick={onClick}
    style={{
      backgroundColor: colors.surface,
      border: `2px solid ${color}`,
      borderRadius: 12,
      padding: spacing.md,
      cursor: 'pointer',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 4
    }}
  >
    <span style={{ fontWeight: 900, color: color, fontSize: 14 }}>{label.toUpperCase()}</span>
    <span style={{ fontSize: 10, fontWeight: 700, color: colors.textSecondary }}>{sublabel}</span>
  </button>
);
