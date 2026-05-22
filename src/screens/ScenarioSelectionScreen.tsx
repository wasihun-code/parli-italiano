import React, { useState, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { scenarioCatalog } from '@shared/data/scenarios';
import { useProgressStore } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

const CATEGORIES = [
  'All',
  'Travel',
  'Accommodation',
  'Dining',
  'Shopping',
  'Daily Life',
  'WorkStudy',
  'Social',
  'Culture',
  'Health',
  'Tech',
  'Animals',
  'Verbs_ARE',
  'Verbs_ERE',
  'Verbs_IRE',
  'Reflexive_Verbs',
  'Adjectives',
  'Miscellaneous'
];

export const ScenarioSelectionScreen: React.FC = () => {
  const navigate = useNavigate();
  const [activeCategory, setActiveCategory] = useState('All');
  const areFoundationsPassed = useProgressStore(state =>
    state.areFoundationsPassed(),
  );

  const filteredScenarios = useMemo(() => {
    if (activeCategory === 'All') return scenarioCatalog;
    return scenarioCatalog.filter(s => s.category === activeCategory);
  }, [activeCategory]);

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
      <div className="scenario-selection-container" style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
        <header>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Scenarios 🗺️</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
            Practice Italian in real contexts.
          </p>
        </header>

        <div className="scenario-layout" style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
          {/* Category Filter */}
          <div className="category-sidebar" style={{ 
            display: 'flex', 
            flexDirection: 'row', 
            overflowX: 'auto', 
            gap: spacing.sm,
            paddingBottom: spacing.sm,
            msOverflowStyle: 'none',
            scrollbarWidth: 'none',
          }}>
            {CATEGORIES.map(cat => (
              <button
                key={cat}
                onClick={() => setActiveCategory(cat)}
                style={{
                  padding: `${spacing.xs}px ${spacing.md}px`,
                  borderRadius: 12,
                  border: `2px solid ${activeCategory === cat ? colors.primary : colors.border}`,
                  backgroundColor: activeCategory === cat ? colors.primary : '#fff',
                  color: activeCategory === cat ? '#fff' : colors.textSecondary,
                  fontWeight: '900',
                  fontSize: 14,
                  whiteSpace: 'nowrap',
                  cursor: 'pointer',
                  transition: 'all 0.2s',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6
                }}
              >
                <span>{cat === 'All' ? '🌐' : getCategoryEmoji(cat)}</span>
                {cat.replace('_', ' ')}
              </button>
            ))}
          </div>

          {/* Scenario Grid */}
          <div className="games-grid">
            {filteredScenarios.map(scenario => (
              <div 
                key={scenario.id} 
                className="coffee-card fade-in" 
                onClick={() => navigate(`/scenarios/${scenario.id}`)} 
                style={{ 
                  cursor: 'pointer', 
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between'
                }}
              >
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: spacing.sm }}>
                    <span style={{ fontSize: 24 }}>{getCategoryEmoji(scenario.category)}</span>
                    <span style={{ fontSize: 12, fontWeight: 900, color: colors.accent, textTransform: 'uppercase', backgroundColor: 'rgba(0,0,0,0.05)', padding: '2px 6px', borderRadius: 4 }}>
                      {scenario.category}
                    </span>
                  </div>
                  <h3 style={{ color: colors.primary, fontSize: 18, fontWeight: 900, margin: '0 0 8px' }}>
                    {scenario.title}
                  </h3>
                  <p style={{ color: colors.textSecondary, fontSize: 14, margin: '0 0 16px', lineHeight: '1.5' }}>
                    {scenario.description}
                  </p>
                </div>
                
                <PrimaryButton 
                  label="View Details" 
                  onPress={() => navigate(`/scenarios/${scenario.id}`)} 
                  variant="primary"
                />
              </div>
            ))}
          </div>
        </div>
      </div>

      <style>{`
        .category-sidebar::-webkit-scrollbar {
          display: none;
        }
        @media (min-width: 1024px) {
          .scenario-layout {
            flex-direction: row !important;
            align-items: flex-start;
          }
          .category-sidebar {
            flex-direction: column !important;
            width: 220px;
            flex-shrink: 0;
            overflow-x: visible !important;
            position: sticky;
            top: 24px;
          }
          .category-sidebar button {
            width: 100%;
            text-align: left;
            justify-content: flex-start;
          }
        }
      `}</style>
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
