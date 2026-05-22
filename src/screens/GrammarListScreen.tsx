import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useGrammarStore } from '@shared/store/grammarStore';
import grammarExpanded from '@shared/data/grammarExpanded.json';
import { ProgressBar } from '../components/ProgressBar';
import { useSubscriptionStore } from '@shared/store/subscriptionStore';

export const GrammarListScreen: React.FC = () => {
  const navigate = useNavigate();
  const completedLessons = useGrammarStore(state => state.completedLessons);
  const { plan, isValid } = useSubscriptionStore();
  const isPremium = plan !== 'free' && isValid;

  const completedCount = grammarExpanded.filter(l => completedLessons[l.id]).length;
  const progressPercent = Math.round((completedCount / grammarExpanded.length) * 100) || 0;

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.lg }}>
        <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Grammar 📚</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
          Master the rules of Italian.
        </p>
      </header>

      <div className="card" style={{ padding: spacing.lg, marginBottom: spacing.xl }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: spacing.sm }}>
          <span style={{ fontWeight: 'bold', color: colors.primary }}>Overall Progress</span>
          <span style={{ fontWeight: 'bold', color: colors.accent }}>{progressPercent}%</span>
        </div>
        <ProgressBar progress={progressPercent} />
      </div>

      <div className="games-grid">
        {grammarExpanded.map((lesson, index) => {
          const isCompleted = completedLessons[lesson.id];
          const isPremiumLocked = lesson.level !== 'A1' && !isPremium;
          
          return (
            <div 
              key={lesson.id} 
              className="card fade-in" 
              onClick={() => isPremiumLocked ? navigate('/premium') : navigate(`/grammar/${lesson.id}`)}
              style={{ cursor: 'pointer', display: 'flex', gap: spacing.md, opacity: (isCompleted || isPremiumLocked) ? 0.8 : 1 }}
            >
              <div style={{ 
                width: 48, 
                height: 48, 
                borderRadius: 24, 
                backgroundColor: isPremiumLocked ? 'rgba(255, 215, 0, 0.1)' : (isCompleted ? colors.success : 'rgba(78, 52, 46, 0.05)'),
                color: isCompleted ? colors.onPrimary : colors.primary,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: 20,
                fontWeight: 'bold',
                flexShrink: 0
              }}>
                {isPremiumLocked ? '👑' : (isCompleted ? '✓' : index + 1)}
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <h2 style={{ color: colors.primary, fontSize: 20, fontWeight: 900, margin: '0 0 4px' }}>
                    {lesson.title}
                  </h2>
                  <span style={{ fontSize: 12, fontWeight: 'bold', color: colors.accent }}>{lesson.level}</span>
                </div>
                <p style={{ color: colors.textSecondary, fontSize: 14, margin: 0, lineHeight: '1.4' }}>
                  10 exercises
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </Screen>
  );
};
