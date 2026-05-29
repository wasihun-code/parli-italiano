import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Scenario } from '@shared/data/scenarios';
import { useProgressStore, emptyScenarioProgress } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { PrimaryButton } from '../components/PrimaryButton';

interface Props {
  scenario: Scenario;
}

export const MiniLessonScenarioView: React.FC<Props> = ({ scenario }) => {
  const navigate = useNavigate();
  const progress = useProgressStore(state => state.scenarioProgress[scenario.id] || emptyScenarioProgress);
  const completedLessons = progress.miniLessonsCompleted || [];
  
  const totalLessons = scenario.miniLessons?.length || 0;
  const completedCount = completedLessons.length;

  return (
    <>
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

      <div style={{ backgroundColor: colors.surface, padding: spacing.lg, borderRadius: 20, marginBottom: spacing.xl }}>
        <h3 style={{ margin: '0 0 8px', color: colors.primary }}>Progress</h3>
        <p style={{ margin: 0, color: colors.textSecondary, fontWeight: 600 }}>
          {completedCount} / {totalLessons} lessons completed
        </p>
        <div style={{ 
          height: 8, 
          backgroundColor: colors.border, 
          borderRadius: 4, 
          marginTop: spacing.md,
          overflow: 'hidden'
        }}>
          <div style={{ 
            height: '100%', 
            backgroundColor: colors.success, 
            width: `${(completedCount / totalLessons) * 100}%`,
            transition: 'width 0.3s ease'
          }} />
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
        <h2 style={{ fontSize: 24, fontWeight: 900, color: colors.primary, margin: '0 0 16px' }}>Lessons</h2>
        
        {scenario.miniLessons?.map((lesson, idx) => {
          const isCompleted = completedLessons.includes(lesson.id);
          let isUnlocked = false;
          
          if (idx === 0) {
             isUnlocked = true;
          } else if (lesson.unlockCriteria === 'complete_previous') {
             const prevLessonId = scenario.miniLessons![idx - 1].id;
             isUnlocked = completedLessons.includes(prevLessonId);
          } else if (lesson.unlockCriteria === 'none') {
             isUnlocked = true;
          }

          return (
            <div 
              key={lesson.id}
              className={`card fade-in ${!isUnlocked ? 'locked' : ''}`}
              style={{ 
                display: 'flex', 
                gap: spacing.lg, 
                alignItems: 'center',
                opacity: isUnlocked ? 1 : 0.7,
                backgroundColor: isUnlocked ? colors.surface : 'rgba(0,0,0,0.02)',
                cursor: isUnlocked ? 'default' : 'not-allowed',
                padding: spacing.lg
              }}
            >
              <div style={{ 
                width: 48, 
                height: 48, 
                borderRadius: '50%', 
                backgroundColor: isUnlocked ? 'rgba(78, 52, 46, 0.05)' : colors.border,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: 24,
                flexShrink: 0
              }}>
                {isCompleted ? '✓' : (isUnlocked ? '🔓' : '🔒')}
              </div>
              
              <div style={{ flex: 1 }}>
                <h3 style={{ color: colors.primary, fontSize: 18, fontWeight: 800, margin: 0 }}>
                  {lesson.title}
                </h3>
              </div>

              <div style={{ minWidth: 100 }}>
                <PrimaryButton 
                  label={isCompleted ? "Review" : "Start"} 
                  onPress={() => navigate(`/scenarios/${scenario.id}/lesson/${lesson.id}/intro`)}
                  disabled={!isUnlocked}
                  variant={isCompleted ? "secondary" : "primary"}
                />
              </div>
            </div>
          );
        })}

        <div style={{ marginTop: spacing.xl, paddingTop: spacing.xl, borderTop: `2px dashed ${colors.border}` }}>
          <h2 style={{ fontSize: 24, fontWeight: 900, color: colors.primary, margin: '0 0 8px' }}>Scenario Conversations</h2>
          <p style={{ color: colors.textSecondary, marginBottom: spacing.lg }}>
            {completedCount === totalLessons 
              ? '4 Realistic Conversations available to practice.' 
              : 'Complete all lessons to unlock.'}
          </p>
          <PrimaryButton 
            label="Start Conversation" 
            onPress={() => {}}
            disabled={completedCount !== totalLessons}
            variant="primary"
          />
        </div>
      </div>
    </>
  );
};
