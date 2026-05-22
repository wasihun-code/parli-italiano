import React, { useState, useMemo, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { scenarioCatalog } from '@shared/data/scenarios';
import { useProgressStore } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
const CATEGORIES = [
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
  'Verbs ARE',
  'Verbs ERE',
  'Verbs IRE',
  'Reflexive Verbs',
  'Adjectives',
  'Miscellaneous'
];

const normalize = (s: string) => s.toLowerCase().trim().replace(/[\s_]+/g, '_');

export const ScenarioSelectionScreen: React.FC = () => {
  const navigate = useNavigate();
  const [activeCategory, setActiveCategory] = useState('Travel');
  const categoryScrollRef = useRef<HTMLDivElement>(null);
  const areFoundationsPassed = useProgressStore(state =>
    state.areFoundationsPassed(),
  );

  const filteredScenarios = useMemo(() => {
    const normalizedActive = normalize(activeCategory);
    return scenarioCatalog.filter(s => normalize(s.category) === normalizedActive);
  }, [activeCategory]);

  const scrollCategories = (direction: 'left' | 'right') => {
    if (categoryScrollRef.current) {
      const scrollAmount = 200;
      categoryScrollRef.current.scrollBy({
        left: direction === 'left' ? -scrollAmount : scrollAmount,
        behavior: 'smooth'
      });
    }
  };

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

        {/* Horizontal Category Row */}
        <div className="category-row-container" style={{ 
          position: 'relative', 
          display: 'flex', 
          alignItems: 'center',
          gap: spacing.sm,
          width: '100%'
        }}>
          <button 
            onClick={() => scrollCategories('left')}
            className="scroll-btn"
            style={{
              width: 36, height: 36, borderRadius: 18, backgroundColor: '#fff',
              border: `2px solid ${colors.border}`, cursor: 'pointer',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              boxShadow: '0 2px 4px rgba(0,0,0,0.1)', flexShrink: 0
            }}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M15 18l-6-6 6-6"/>
            </svg>
          </button>

          <div 
            className="category-scroll-wrapper"
            ref={categoryScrollRef}
            style={{ 
              display: 'flex', 
              flexDirection: 'row', 
              overflowX: 'auto', 
              gap: spacing.sm,
              padding: `${spacing.xs}px 0`,
              scrollSnapType: 'x mandatory',
              msOverflowStyle: 'none',
              scrollbarWidth: 'none',
              flex: 1
            }}
          >
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
                  gap: 6,
                  scrollSnapAlign: 'start'
                }}
              >
                <span>{getCategoryEmoji(cat)}</span>
                {cat}
              </button>
            ))}
          </div>

          <button 
            onClick={() => scrollCategories('right')}
            className="scroll-btn"
            style={{
              width: 36, height: 36, borderRadius: 18, backgroundColor: '#fff',
              border: `2px solid ${colors.border}`, cursor: 'pointer',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              boxShadow: '0 2px 4px rgba(0,0,0,0.1)', flexShrink: 0
            }}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M9 18l6-6-6-6"/>
            </svg>
          </button>
        </div>

        {/* Scenario Grid */}
        <div 
          className="scenarios-grid"
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
            gap: '1.5rem',
            width: '100%',
            paddingBottom: spacing.xxl
          }}
        >
          {filteredScenarios.map(scenario => (
            <div 
              key={scenario.id} 
              className="coffee-card fade-in" 
              onClick={() => navigate(`/scenarios/${scenario.id}`)} 
              style={{ 
                cursor: 'pointer', 
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                height: '100%',
                minHeight: 220,
              }}
            >
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: spacing.sm }}>
                  <span style={{ fontSize: 24 }}>{getCategoryEmoji(scenario.category)}</span>
                  <span style={{ fontSize: 12, fontWeight: 900, color: colors.accent, textTransform: 'uppercase', backgroundColor: 'rgba(0,0,0,0.05)', padding: '2px 6px', borderRadius: 4 }}>
                    {scenario.category.replace('_', ' ')}
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

      <style>{`
        .category-scroll-wrapper::-webkit-scrollbar {
          display: none;
        }
        @media (min-width: 1024px) {
          .scenarios-grid {
            grid-template-columns: repeat(3, 1fr) !important;
          }
        }
        @media (max-width: 768px) {
          .scenarios-grid {
            grid-template-columns: repeat(2, 1fr);
          }
        }
        @media (max-width: 480px) {
          .scenarios-grid {
            grid-template-columns: 1fr;
          }
        }
      `}</style>
    </Screen>
  );
};

function getCategoryEmoji(category: string): string {
  const norm = normalize(category);
  switch (norm) {
    case 'travel': return '✈️';
    case 'accommodation': return '🏨';
    case 'dining': return '🍝';
    case 'shopping': return '🛍️';
    case 'daily_life': return '🏠';
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
