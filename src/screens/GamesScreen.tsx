import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useGameStore } from '@shared/store/gameStore';
import { PrimaryButton } from '../components/PrimaryButton';

const GAMES = [
  { id: 'genderGame', title: 'Feminine or Masculine', description: 'Guess the gender of Italian nouns.', icon: '🚻', path: '/games/gender' },
  { id: 'translationGame', title: 'Sentence Translation', description: 'Translate sentences between English and Italian.', icon: '🔄', path: '/games/translation' },
  { id: 'prepositionGame', title: 'Prepositions Game', description: 'Choose the correct preposition to complete the sentence.', icon: '🔗', path: '/games/prepositions' },
  { id: 'idiomsGame', title: 'Expressions', description: 'Learn common Italian idioms and sayings.', icon: '💬', path: '/games/idioms' },
  { id: 'oppositesGame', title: 'Opposites', description: 'Type the antonym of the given word.', icon: '↔️', path: '/games/opposites' },
  { id: 'numbersGame', title: 'Numbers', description: 'Practice reading and writing numbers.', icon: '🔢', path: '/games/numbers' },
  { id: 'pluralGame', title: 'Plural Game', description: 'Type the plural form of Italian words.', icon: '👯', path: '/games/plural' },
  { id: 'stories', title: 'Storie', description: 'Read Italian stories and test your comprehension.', icon: '📖', path: '/stories' },
];

export const GamesScreen: React.FC = () => {
  const navigate = useNavigate();
  const gameStore = useGameStore();

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Games 🎮</h1>
        <p style={{ color: colors.textSecondary }}>Test your skills in a fun way.</p>
      </header>

      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', 
        gap: '32px',
        paddingBottom: '100px'
      }}>
        {GAMES.map(game => {
          const isStoryGame = game.id === 'stories';
          const progress = (gameStore as any)[game.id];
          
          return (
            <div 
              key={game.id} 
              className="card fade-in" 
              onClick={() => navigate(game.path)}
              style={{ 
                cursor: 'pointer', 
                display: 'flex', 
                flexDirection: 'column',
                gap: spacing.md, 
                backgroundColor: '#FDFBF7',
                padding: spacing.lg,
                borderRadius: 24,
                border: `2px solid ${colors.border}`,
                transition: 'transform 0.2s ease, box-shadow 0.2s ease',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-4px)';
                e.currentTarget.style.boxShadow = '0 8px 24px rgba(78, 52, 46, 0.12)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = 'none';
              }}
            >
              <div style={{ display: 'flex', gap: spacing.md, alignItems: 'center' }}>
                <div style={{ 
                  width: 56, 
                  height: 56, 
                  borderRadius: 16, 
                  backgroundColor: 'rgba(78, 52, 46, 0.05)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: 28,
                  flexShrink: 0
                }}>
                  {game.icon}
                </div>
                <div style={{ flex: 1 }}>
                  <h2 style={{ color: colors.primary, fontSize: 20, fontWeight: 900, margin: '0 0 4px' }}>
                    {game.title}
                  </h2>
                  <div style={{ display: 'flex', gap: spacing.md, alignItems: 'center' }}>
                    {!isStoryGame && progress && (
                      <span style={{ fontSize: 12, fontWeight: 900, color: colors.accent, textTransform: 'uppercase' }}>
                        Level {progress.unlockedLevels}
                      </span>
                    )}
                    {isStoryGame && (
                      <span style={{ fontSize: 12, fontWeight: 900, color: colors.accent, textTransform: 'uppercase' }}>
                        {gameStore.completedStories.length} Completed
                      </span>
                    )}
                  </div>
                </div>
              </div>
              
              <p style={{ color: colors.textSecondary, fontSize: 15, margin: 0, lineHeight: '1.5', flex: 1 }}>
                {game.description}
              </p>

              <PrimaryButton 
                label="Play" 
                onPress={() => navigate(game.path)} 
                style={{ marginTop: spacing.sm }}
              />
            </div>
          );
        })}
      </div>
    </Screen>
  );
};

