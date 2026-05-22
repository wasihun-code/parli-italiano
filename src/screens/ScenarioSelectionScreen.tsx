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

  const groupedScenarios = scenarioCatalog.reduce((acc, scenario) => {
    if (!acc[scenario.category]) {
      acc[scenario.category] = [];
    }
    acc[scenario.category].push(scenario);
    return acc;
  }, {} as Record<string, typeof scenarioCatalog>);

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Scenarios 🗺️</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
          Practice Italian in real contexts.
        </p>
      </header>

      {Object.entries(groupedScenarios).map(([category, scenarios]) => (
        <section key={category} style={{ marginBottom: spacing.xl }}>
          <h2 style={{ 
            color: colors.primary, 
            fontSize: 24, 
            fontWeight: 900, 
            marginBottom: spacing.md, 
            display: 'flex', 
            alignItems: 'center', 
            gap: spacing.sm,
            paddingBottom: spacing.xs,
            borderBottom: `2px solid ${colors.border}`
          }}>
            <span style={{ fontSize: 28 }}>{getCategoryEmoji(category)}</span>
            {category}
          </h2>
          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', 
            gap: spacing.lg,
            marginBottom: spacing.xl
          }}>
            {scenarios.map(scenario => (
              <div 
                key={scenario.id} 
                className="card fade-in" 
                onClick={() => navigate(`/scenarios/${scenario.id}`)} 
                style={{ 
                  cursor: 'pointer', 
                  padding: spacing.lg,
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between'
                }}
              >
                <div>
                  <h3 style={{ color: colors.primary, fontSize: 18, fontWeight: 900, margin: '0 0 8px' }}>
                    {scenario.title}
                  </h3>
                  <p style={{ color: colors.textSecondary, fontSize: 14, margin: '0 0 16px', lineHeight: '1.5' }}>
                    {scenario.description}
                  </p>
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
                    View Details
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                      <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>
      ))}
    </Screen>
  );
};

function getCategoryEmoji(category: string): string {
  switch (category.toLowerCase()) {
    case 'travel': return '✈️';
    case 'accommodation': return '🏨';
    case 'dining': return '🍝';
    case 'shopping': return '🛍️';
    case 'daily life': return '🏠';
    case 'workstudy': return '💼';
    case 'social': return '🎉';
    case 'culture': return '🎭';
    case 'health': return '🏥';
    case 'tech': return '📱';
    case 'miscellaneous': return '📌';
    case 'animals': return '🐶';
    case 'verbs_are':
    case 'verbs_ere':
    case 'verbs_ire': return '📖';
    case 'reflexive_verbs': return '🔄';
    case 'adjectives': return '🌟';
    default: return '📘';
  }
}
