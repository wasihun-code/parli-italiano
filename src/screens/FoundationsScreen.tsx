import React from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { foundationLessons } from '@shared/data/foundations';
import { useProgressStore } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

export const FoundationsScreen: React.FC = () => {
  const navigate = useNavigate();
  const foundationScores = useProgressStore(state => state.foundationScores);
  const areFoundationsPassed = useProgressStore(state =>
    state.areFoundationsPassed(),
  );

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl, display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end' }}>
        <div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Foundations 🎓</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
            The building blocks of Italian.
          </p>
        </div>
        <button 
          onClick={() => navigate('/placement-test')}
          className="card"
          style={{
            padding: '10px 16px',
            borderRadius: 14,
            borderColor: colors.accent,
            color: colors.accent,
            fontWeight: 900,
            fontSize: 14,
            backgroundColor: 'transparent',
            letterSpacing: 0.5
          }}
        >
          PLACEMENT TEST
        </button>
      </header>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
        {foundationLessons.map((lesson, index) => {
          const score = foundationScores[lesson.id] ?? 0;
          const passed = score >= 90;
          return (
            <div
              key={lesson.id}
              onClick={() => navigate(`/foundations/${lesson.id}`)}
              className={`card fade-in ${passed ? 'active' : ''}`}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: spacing.md,
                animationDelay: `${index * 0.1}s`
              }}
            >
              <div style={{ 
                width: 64, 
                height: 64, 
                borderRadius: 20, 
                backgroundColor: passed ? colors.success : colors.chipBg,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: 28,
                color: passed ? colors.onPrimary : colors.primary,
                boxShadow: passed ? '0 4px 12px rgba(56, 102, 65, 0.2)' : 'none',
                transition: 'all 0.3s ease'
              }}>
                {passed ? (
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="20 6 9 17 4 12"/>
                  </svg>
                ) : (
                  <span style={{ fontWeight: 900, fontSize: 24 }}>{index + 1}</span>
                )}
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: spacing.sm }}>
                  <span style={{ color: colors.primary, fontSize: 20, fontWeight: 900 }}>{lesson.title}</span>
                </div>
                <p style={{ color: colors.textSecondary, fontSize: 16, margin: '4px 0 0' }}>{lesson.description}</p>
                {passed && (
                  <div style={{ 
                    display: 'inline-flex', 
                    alignItems: 'center', 
                    gap: 4, 
                    color: colors.success, 
                    fontSize: 12, 
                    fontWeight: 900, 
                    marginTop: 8,
                    textTransform: 'uppercase',
                    letterSpacing: 1
                  }}>
                    Completed
                  </div>
                )}
              </div>
              <div style={{ textAlign: 'right' }}>
                <span style={{ 
                  color: passed ? colors.success : (score > 0 ? colors.accent : colors.textSecondary), 
                  fontSize: 24, 
                  fontWeight: 900,
                  fontFamily: 'monospace'
                }}>
                  {score}%
                </span>
              </div>
            </div>
          );
        })}
      </div>

      <div className="card" style={{
        backgroundColor: areFoundationsPassed ? 'rgba(56, 102, 65, 0.05)' : 'rgba(78, 52, 46, 0.03)',
        borderColor: areFoundationsPassed ? colors.success : colors.primary,
        marginTop: spacing.xl,
        padding: 24,
        display: 'flex',
        flexDirection: 'column',
        gap: spacing.md,
        cursor: 'default'
      }}>
        <h2 style={{ color: areFoundationsPassed ? colors.success : colors.primary, fontSize: 22, fontWeight: 900, margin: 0 }}>
          {areFoundationsPassed ? 'Scenarios Unlocked! 🎉' : 'Unlock Scenarios'}
        </h2>
        <p style={{ color: colors.textSecondary, fontSize: 17, margin: 0, lineHeight: '1.6' }}>
          {areFoundationsPassed
            ? 'Great job! You have the foundations to start practicing in real situations.'
            : 'Complete all foundations with 90%+ to unlock 100+ scenario-based exercises.'}
        </p>
        <PrimaryButton
          label="Browse Scenarios"
          disabled={!areFoundationsPassed}
          onPress={() => navigate('/scenarios')}
          variant={areFoundationsPassed ? 'primary' : 'secondary'}
        />
      </div>
    </Screen>
  );
};
