import React from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { scenarioCatalog } from '@shared/data/scenarios';
import { useProgressStore } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

export const ScenarioSelectionScreen: React.FC = () => {
  const navigate = useNavigate();
  const areFoundationsPassed = useProgressStore(state =>
    state.areFoundationsPassed(),
  );

  if (!areFoundationsPassed) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{
          backgroundColor: 'rgba(227, 155, 20, 0.03)',
          borderColor: colors.warning,
          padding: spacing.xl,
          display: 'flex',
          flexDirection: 'column',
          gap: spacing.md,
          textAlign: 'center',
          cursor: 'default'
        }}>
          <div style={{ fontSize: 64, marginBottom: spacing.sm }}>🔒</div>
          <h1 style={{ color: colors.warning, fontSize: 32, fontWeight: 900, margin: 0 }}>Scenarios Locked</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, lineHeight: '1.6', margin: 0 }}>
            Complete all 5 foundation lessons with a 90%+ score to unlock real-world scenarios.
          </p>
          <PrimaryButton
            label="Go to Foundations"
            onPress={() => navigate('/foundations')}
            variant="accent"
            style={{ marginTop: spacing.lg }}
          />
        </div>
      </Screen>
    );
  }

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Scenarios 🗺️</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
          Practice Italian in real contexts.
        </p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.lg }}>
        {scenarioCatalog.map(scenario => (
          <div key={scenario.id} className="card fade-in" onClick={() => navigate(`/scenarios/${scenario.id}/vocabulary`)}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div style={{ flex: 1 }}>
                <span style={{ 
                  backgroundColor: colors.chipBg, 
                  color: colors.primary, 
                  fontSize: 12, 
                  fontWeight: 900, 
                  padding: '4px 10px', 
                  borderRadius: 8,
                  textTransform: 'uppercase',
                  letterSpacing: 1
                }}>
                  {scenario.category}
                </span>
                <h2 style={{ color: colors.primary, fontSize: 22, fontWeight: 900, margin: '12px 0 6px' }}>
                  {scenario.title}
                </h2>
                <p style={{ color: colors.textSecondary, fontSize: 16, margin: '0 0 16px', lineHeight: '1.5' }}>
                  {scenario.description}
                </p>
              </div>
              <div style={{ 
                width: 56, 
                height: 56, 
                backgroundColor: 'rgba(78, 52, 46, 0.05)', 
                borderRadius: 16,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: 28,
                marginLeft: spacing.md
              }}>
                {getCategoryEmoji(scenario.category)}
              </div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <div style={{ 
                color: colors.accent, 
                fontWeight: 900, 
                fontSize: 14, 
                display: 'flex', 
                alignItems: 'center', 
                gap: 4 
              }}>
                Start now
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
              </div>
            </div>
          </div>
        ))}
      </div>
    </Screen>
  );
};

function getCategoryEmoji(category: string): string {
  switch (category.toLowerCase()) {
    case 'travel': return '✈️';
    case 'food': return '🍝';
    case 'social': return '👋';
    case 'business': return '💼';
    case 'daily': return '🏠';
    case 'animals': return '🐾';
    case 'verbs_are':
    case 'verbs_ere':
    case 'verbs_ire':
    case 'reflexive_verbs':
      return '📝';
    case 'adjectives': return '✨';
    default: return '🇮🇹';
  }
}
