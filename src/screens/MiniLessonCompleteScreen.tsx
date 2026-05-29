import React, { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { scenarios } from '@shared/data/scenarios';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { PrimaryButton } from '../components/PrimaryButton';
import { useProgressStore } from '@shared/store/progressStore';

export const MiniLessonCompleteScreen: React.FC = () => {
  const { scenarioId, lessonId } = useParams<{ scenarioId: string; lessonId: string }>();
  const navigate = useNavigate();
  
  const completeMiniLesson = useProgressStore(state => state.completeMiniLesson);

  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  const lesson = scenario?.miniLessons?.find(l => l.id === lessonId);

  useEffect(() => {
    if (scenarioId && lessonId) {
      completeMiniLesson(Number(scenarioId), lessonId);
    }
  }, [scenarioId, lessonId, completeMiniLesson]);

  if (!scenario || !lesson) return null;

  return (
    <Screen>
      <div className="fade-in" style={{ 
        display: 'flex', 
        flexDirection: 'column', 
        height: '100%',
        alignItems: 'center',
        justifyContent: 'center',
        padding: spacing.xl
      }}>
        
        <div style={{ fontSize: 64, marginBottom: spacing.lg }}>🎉</div>
        
        <h1 style={{ 
          color: colors.primary, 
          fontSize: 32, 
          fontWeight: 900, 
          margin: '0 0 16px',
          textAlign: 'center' 
        }}>
          Lesson Complete
        </h1>

        <div className="card" style={{ 
          backgroundColor: colors.surface,
          padding: spacing.xl, 
          borderRadius: 20, 
          width: '100%',
          marginBottom: spacing.xxl
        }}>
          <h2 style={{ color: colors.primary, fontSize: 18, marginBottom: spacing.md }}>You can now:</h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
             <p style={{ margin: 0, color: colors.textSecondary, display: 'flex', alignItems: 'center', gap: 8, fontWeight: 600 }}>
               <span style={{ color: colors.success }}>✓</span>
               {lesson.goal}
             </p>
          </div>

          <div style={{ 
            marginTop: spacing.xl, 
            paddingTop: spacing.md, 
            borderTop: `1px solid ${colors.border}`,
            display: 'flex',
            alignItems: 'center',
            gap: spacing.sm,
            color: colors.accent,
            fontWeight: 800,
            fontSize: 20
          }}>
            <span>⭐</span>
            +50 XP
          </div>
        </div>

        <div style={{ width: '100%', marginTop: 'auto' }}>
          <PrimaryButton 
            label="Continue" 
            onPress={() => navigate(`/scenarios/${scenarioId}`)} 
          />
        </div>
      </div>
    </Screen>
  );
};
