import React, { useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { useSrsStore } from '@shared/store/srsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { calculateReviewStats, getNextReviewIndex } from '@shared/utils/review';

export const ReviewScreen: React.FC = () => {
  const navigate = useNavigate();
  const items = useSrsStore(state => state.items);
  const dueItems = useMemo(() => {
    const now = new Date();
    return Object.values(items).filter(item => new Date(item.dueAt) <= now);
  }, [items]);
  const recordAnswer = useSrsStore(state => state.recordAnswer);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  
  const stats = useMemo(
    () => calculateReviewStats(items, dueItems),
    [dueItems, items],
  );
  
  const currentItem = dueItems[currentIndex] ?? dueItems[0];

  const playAudio = (): void => {
    if (currentItem) {
      Tts.speak(currentItem.italian);
    }
  };

  const answerCard = (correct: boolean): void => {
    if (!currentItem) return;

    recordAnswer(currentItem.id, correct);
    setCurrentIndex(index => getNextReviewIndex(index, dueItems.length));
    setRevealed(false);
  };

  if (!currentItem) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{
          textAlign: 'center',
          padding: spacing.xl,
          display: 'flex',
          flexDirection: 'column',
          gap: spacing.lg,
          cursor: 'default'
        }}>
          <div style={{ fontSize: 64 }}>☕</div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Review completed</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, margin: 0 }}>
            Nothing to review right now - come back later!
          </p>
          <div style={{ 
            backgroundColor: colors.chipBg, 
            padding: spacing.md, 
            borderRadius: 16,
            fontSize: 14,
            fontWeight: 800,
            color: colors.primary
          }}>
            {stats.learnedItems} learned / {stats.totalItems} total
          </div>
          <PrimaryButton label="Back Home" onPress={() => navigate('/')} />
        </div>
      </Screen>
    );
  }

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Review 🔁</h1>
        <p style={{ color: colors.textSecondary, fontSize: 16, marginTop: spacing.xxs, fontWeight: 700 }}>
          {stats.dueItems} due • {stats.learnedItems} learned
        </p>
      </header>

      <div
        onClick={() => {
          setRevealed(current => !current);
          if (!revealed) playAudio();
        }}
        className="card fade-in"
        style={{
          alignItems: 'center',
          minHeight: 300,
          justifyContent: 'center',
          padding: spacing.xl,
          textAlign: 'center',
          perspective: '1000px',
          borderWidth: 3,
          backgroundColor: revealed ? colors.surface : colors.chipBg,
          borderColor: revealed ? colors.accent : colors.border,
          boxShadow: `0 12px 30px rgba(78, 52, 46, 0.08)`
        }}
      >
        <div style={{ 
          transform: revealed ? 'rotateY(0deg)' : 'rotateY(0deg)',
          transition: 'transform 0.6s',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: spacing.md
        }}>
          <span style={{ color: colors.accent, fontSize: 12, fontWeight: 900, textTransform: 'uppercase', letterSpacing: 2 }}>
            {revealed ? 'Translation' : 'Italian'}
          </span>
          <span style={{ 
            color: colors.primary, 
            fontSize: revealed ? 32 : 42, 
            fontWeight: 900, 
            lineHeight: '1.2',
            wordBreak: 'break-word'
          }}>
            {revealed ? currentItem.english : currentItem.italian}
          </span>
          <div style={{ 
            marginTop: spacing.lg,
            color: colors.textSecondary, 
            fontSize: 13, 
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            gap: 6
          }}>
             <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21 12V7a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h7"/><path d="m16 20 2 2 4-4"/>
            </svg>
            Tap to flip
          </div>
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md, marginTop: spacing.xl }}>
        {revealed ? (
          <div className="fade-in" style={{ display: 'flex', gap: spacing.md }}>
            <button
              onClick={() => answerCard(false)}
              style={{
                flex: 1,
                backgroundColor: colors.surface,
                color: colors.error,
                border: `3px solid ${colors.error}`,
                borderRadius: 16,
                minHeight: 60,
                fontWeight: 900,
                fontSize: 16,
                cursor: 'pointer',
                transition: 'all 0.1s'
              }}
              onMouseDown={e => e.currentTarget.style.transform = 'scale(0.95)'}
              onMouseUp={e => e.currentTarget.style.transform = 'scale(1)'}
            >
              FORGOT
            </button>
            <button
              onClick={() => answerCard(true)}
              style={{
                flex: 1,
                backgroundColor: colors.success,
                color: colors.onPrimary,
                border: 'none',
                borderBottom: '4px solid rgba(0,0,0,0.2)',
                borderRadius: 16,
                minHeight: 60,
                fontWeight: 900,
                fontSize: 16,
                cursor: 'pointer',
                transition: 'all 0.1s'
              }}
              onMouseDown={e => e.currentTarget.style.transform = 'scale(0.95)'}
              onMouseUp={e => e.currentTarget.style.transform = 'scale(1)'}
            >
              REMEMBERED
            </button>
          </div>
        ) : (
          <PrimaryButton label="Play Audio" onPress={playAudio} variant="secondary" icon={
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
            </svg>
          } />
        )}
        <button 
          onClick={() => navigate('/')}
          style={{ 
            background: 'none', 
            border: 'none', 
            color: colors.textSecondary, 
            fontWeight: 800, 
            marginTop: spacing.md,
            cursor: 'pointer',
            textDecoration: 'underline'
          }}
        >
          Back Home
        </button>
      </div>
    </Screen>
  );
};
