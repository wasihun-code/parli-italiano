import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { scenarios } from '@shared/data/scenarios';
import { useProgressStore } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { PrimaryButton } from '../components/PrimaryButton';

export const ScenarioDetailScreen: React.FC = () => {
  const { scenarioId } = useParams<{ scenarioId: string }>();
  const navigate = useNavigate();
  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  const progress = useProgressStore(state => state.scenarioProgress[Number(scenarioId)] || {
    vocabularyCompleted: false,
    phraseCompleted: false,
    sentenceCompleted: false,
  });

  if (!scenario) {
    return (
      <Screen>
        <div style={{ textAlign: 'center', marginTop: spacing.xl }}>
          <h1 style={{ color: colors.primary }}>Scenario not found</h1>
          <PrimaryButton label="Go Back" onPress={() => navigate('/scenarios')} />
        </div>
      </Screen>
    );
  }

  const phases = [
    {
      id: 'vocabulary',
      title: 'Vocabulary',
      description: 'Learn the essential words for this scenario.',
      icon: '📚',
      isUnlocked: true,
      isCompleted: progress.vocabularyCompleted,
      path: `/scenarios/${scenario.id}/vocabulary`
    },
    {
      id: 'phrase',
      title: 'Phrases',
      description: 'Master common phrases used in this context.',
      icon: '💬',
      isUnlocked: progress.vocabularyCompleted,
      isCompleted: progress.phraseCompleted,
      path: `/scenarios/${scenario.id}/phrases`
    },
    {
      id: 'sentence',
      title: 'Sentences',
      description: 'Build full sentences and practice grammar.',
      icon: '✍️',
      isUnlocked: progress.phraseCompleted,
      isCompleted: progress.sentenceCompleted,
      path: `/scenarios/${scenario.id}/sentences`
    }
  ];

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md, marginBottom: spacing.sm }}>
          <button 
            onClick={() => navigate('/scenarios')}
            style={{ 
              background: 'none', 
              border: 'none', 
              cursor: 'pointer',
              color: colors.primary,
              display: 'flex',
              alignItems: 'center',
              padding: 0
            }}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          <span style={{ 
            backgroundColor: colors.chipBg, 
            color: colors.primary, 
            fontSize: 12, 
            fontWeight: 900, 
            padding: '4px 10px', 
            borderRadius: 8,
            textTransform: 'uppercase'
          }}>
            {scenario.category}
          </span>
        </div>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: '0 0 8px' }}>
          {scenario.title}
        </h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, lineHeight: '1.5', margin: 0 }}>
          {scenario.description}
        </p>
      </header>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
        {phases.map(phase => (
          <div 
            key={phase.id}
            className={`card fade-in ${!phase.isUnlocked ? 'locked' : ''}`}
            style={{ 
              display: 'flex', 
              gap: spacing.lg, 
              alignItems: 'center',
              opacity: phase.isUnlocked ? 1 : 0.7,
              backgroundColor: phase.isUnlocked ? colors.surface : 'rgba(0,0,0,0.02)',
              cursor: phase.isUnlocked ? 'default' : 'not-allowed',
              padding: spacing.lg
            }}
          >
            <div style={{ 
              width: 64, 
              height: 64, 
              borderRadius: 20, 
              backgroundColor: phase.isUnlocked ? 'rgba(78, 52, 46, 0.05)' : colors.border,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: 32,
              flexShrink: 0
            }}>
              {phase.isUnlocked ? phase.icon : '🔒'}
            </div>
            
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: spacing.sm }}>
                <h2 style={{ color: colors.primary, fontSize: 20, fontWeight: 900, margin: 0 }}>
                  {phase.title}
                </h2>
                {phase.isCompleted && (
                  <span style={{ color: colors.success, fontSize: 20 }}>✓</span>
                )}
              </div>
              <p style={{ color: colors.textSecondary, fontSize: 15, margin: '4px 0 0', lineHeight: '1.4' }}>
                {phase.description}
              </p>
            </div>

            <div style={{ minWidth: 120 }}>
              <PrimaryButton 
                label={phase.isCompleted ? "Review" : "Start"} 
                onPress={() => navigate(phase.path)}
                disabled={!phase.isUnlocked}
                variant={phase.isCompleted ? "secondary" : "primary"}
              />
            </div>
          </div>
        ))}
      </div>

      <div style={{ marginTop: spacing.xxl, display: 'flex', justifyContent: 'center' }}>
        <button 
          onClick={() => navigate(`/scenarios/${scenario.id}/vocabulary?skipTest=true`)}
          style={{ 
            background: 'none', 
            border: 'none', 
            color: colors.textSecondary, 
            textDecoration: 'underline', 
            fontSize: 16, 
            cursor: 'pointer',
            fontWeight: 600
          }}
        >
          Skip to Test
        </button>
      </div>
    </Screen>
  );
};
