import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useGameStore } from '@shared/store/gameStore';
import storiesData from '@shared/data/stories.json';
import { ProgressBar } from '../components/ProgressBar';

export const StoriesScreen: React.FC = () => {
  const navigate = useNavigate();
  const { unlockedStories, completedStories, storyProgress, unlockStory } = useGameStore();

  useEffect(() => {
    // Unlock all difficulty 1 stories initially
    storiesData.stories.forEach(story => {
      if (story.difficulty === 1 && !unlockedStories.includes(story.title)) {
        unlockStory(story.title);
      }
    });
  }, [unlockStory, unlockedStories]);

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Storie 📖</h1>
        <p style={{ color: colors.textSecondary }}>Read stories and test your comprehension.</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.lg, paddingBottom: 100 }}>
        {storiesData.stories.map((story) => {
          const isUnlocked = unlockedStories.includes(story.title);
          const isCompleted = completedStories.includes(story.title);
          const progress = storyProgress[story.title];
          
          const totalPages = story.parts.reduce((acc, part) => acc + part.pages.length, 0);
          const completedPagesCount = progress?.completedPages.length || 0;
          const progressPercent = Math.round((completedPagesCount / totalPages) * 100);

          return (
            <div 
              key={story.title} 
              className={`card fade-in ${!isUnlocked ? 'locked' : ''}`} 
              onClick={() => isUnlocked && navigate(`/stories/${encodeURIComponent(story.title)}`)}
              style={{ 
                cursor: isUnlocked ? 'pointer' : 'default', 
                display: 'flex', 
                flexDirection: 'column', 
                gap: spacing.sm,
                opacity: isUnlocked ? 1 : 0.6,
                position: 'relative',
                padding: spacing.lg
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h2 style={{ color: colors.primary, fontSize: 20, fontWeight: 900, margin: 0 }}>
                  {story.title}
                </h2>
                {!isUnlocked && <span style={{ fontSize: 24 }}>🔒</span>}
                {isCompleted && <span style={{ fontSize: 24, color: colors.success }}>✅</span>}
              </div>

              <div style={{ display: 'flex', gap: spacing.md, alignItems: 'center' }}>
                <span style={{ 
                  fontSize: 12, 
                  fontWeight: 900, 
                  color: story.difficulty === 1 ? colors.success : story.difficulty === 2 ? colors.primary : colors.error,
                  textTransform: 'uppercase',
                  backgroundColor: 'rgba(0,0,0,0.05)',
                  padding: '4px 8px',
                  borderRadius: 4
                }}>
                  {story.difficulty === 1 ? 'Easy' : story.difficulty === 2 ? 'Medium' : 'Hard'}
                </span>
                <span style={{ fontSize: 12, color: colors.textSecondary }}>
                  {totalPages} pages
                </span>
              </div>

              {isUnlocked && (
                <div style={{ marginTop: spacing.xs }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4, fontSize: 12, fontWeight: 'bold' }}>
                    <span style={{ color: colors.textSecondary }}>Progress</span>
                    <span style={{ color: colors.accent }}>{progressPercent}%</span>
                  </div>
                  <ProgressBar progress={progressPercent} />
                </div>
              )}
            </div>
          );
        })}
      </div>
    </Screen>
  );
};
