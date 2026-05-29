import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { scenarios } from '@shared/data/scenarios';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { PrimaryButton } from '../components/PrimaryButton';
import { useProgressStore, emptyScenarioProgress } from '@shared/store/progressStore';

export const MiniLessonIntroScreen: React.FC = () => {
  const { scenarioId, lessonId } = useParams<{ scenarioId: string; lessonId: string }>();
  const navigate = useNavigate();

  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  const lesson = scenario?.miniLessons?.find(l => l.id === lessonId);
  const progress = useProgressStore(state => state.scenarioProgress[Number(scenarioId)] || emptyScenarioProgress);
  const completedLessons = progress.miniLessonsCompleted || [];
  const isCompleted = lesson ? completedLessons.includes(lesson.id) : false;

  if (!scenario || !lesson) {
    return (
      <Screen>
        <div style={{ textAlign: 'center', marginTop: spacing.xl }}>
          <h1 style={{ color: colors.primary }}>Lesson not found</h1>
          <PrimaryButton label="Go Back" onPress={() => navigate(`/scenarios/${scenarioId}`)} />
        </div>
      </Screen>
    );
  }

  const totalExercises = lesson.sections.reduce((acc, section) => acc + section.exerciseIds.length, 0);

  return (
    <Screen>
      <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
        <header style={{ marginBottom: spacing.xxl }}>
          <button 
            onClick={() => navigate(`/scenarios/${scenarioId}`)}
            style={{ 
              background: 'none', 
              border: 'none', 
              cursor: 'pointer',
              color: colors.primary,
              display: 'flex',
              alignItems: 'center',
              padding: 0,
              marginBottom: spacing.md
            }}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          
          <h1 style={{ color: colors.primary, fontSize: 36, fontWeight: 900, margin: '0 0 8px', lineHeight: 1.1 }}>
            {lesson.title}
          </h1>
        </header>

        <div className="card fade-in" style={{ padding: spacing.xl, marginBottom: spacing.xl, backgroundColor: colors.surface }}>
          <h2 style={{ fontSize: 16, textTransform: 'uppercase', letterSpacing: 1, color: colors.accent, margin: '0 0 8px', fontWeight: 800 }}>Goal</h2>
          <p style={{ fontSize: 20, color: colors.primary, fontWeight: 600, margin: 0, lineHeight: 1.4 }}>
            {lesson.goal}
          </p>
        </div>

        <div className="card fade-in" style={{ padding: spacing.xl, marginBottom: spacing.xl, display: 'flex', gap: spacing.lg }}>
           <div style={{ flex: 1 }}>
              <h2 style={{ fontSize: 16, textTransform: 'uppercase', letterSpacing: 1, color: colors.textSecondary, margin: '0 0 4px', fontWeight: 800 }}>Estimated time</h2>
              <p style={{ fontSize: 18, color: colors.primary, fontWeight: 700, margin: 0 }}>
                {lesson.estimatedDuration}
              </p>
           </div>
           <div style={{ flex: 1 }}>
              <h2 style={{ fontSize: 16, textTransform: 'uppercase', letterSpacing: 1, color: colors.textSecondary, margin: '0 0 4px', fontWeight: 800 }}>Exercises</h2>
              <p style={{ fontSize: 18, color: colors.primary, fontWeight: 700, margin: 0 }}>
                {totalExercises} steps
              </p>
           </div>
        </div>

        <div style={{ marginTop: 'auto', paddingTop: spacing.xl }}>
          <PrimaryButton 
            label={isCompleted ? "Review Lesson" : "Start Lesson"} 
            onPress={() => navigate(`/scenarios/${scenarioId}/lesson/${lessonId}/train`)} 
          />
        </div>
      </div>
    </Screen>
  );
};
