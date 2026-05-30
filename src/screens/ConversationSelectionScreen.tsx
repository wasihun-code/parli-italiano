import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { scenarios } from '@shared/data/scenarios';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { PrimaryButton } from '../components/PrimaryButton';
import { useProgressStore, emptyScenarioProgress } from '@shared/store/progressStore';

export const ConversationSelectionScreen: React.FC = () => {
  const { scenarioId } = useParams<{ scenarioId: string }>();
  const navigate = useNavigate();
  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  
  const progress = useProgressStore(state => state.scenarioProgress[Number(scenarioId)] || emptyScenarioProgress);
  const completedLessons = progress.miniLessonsCompleted || [];
  const totalLessons = scenario?.miniLessons?.length || 0;
  
  const isUnlocked = completedLessons.length >= totalLessons;

  // Keyboard navigation
  React.useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        navigate(`/scenarios/${scenarioId}`);
        return;
      }
      
      if (isUnlocked && scenario?.scriptedConversations) {
        const num = parseInt(e.key, 10);
        if (!isNaN(num) && num >= 1 && num <= scenario.scriptedConversations.length) {
          const conv = scenario.scriptedConversations[num - 1];
          navigate(`/scenarios/${scenarioId}/conversation/${conv.id}`);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [navigate, scenarioId, isUnlocked, scenario?.scriptedConversations]);

  if (!scenario) return null;

  if (!isUnlocked) {
    return (
      <Screen>
        <div style={{ padding: spacing.xl, textAlign: 'center' }}>
          <h1 style={{ color: colors.primary }}>Locked</h1>
          <p style={{ color: colors.textSecondary }}>Complete all mini lessons to unlock conversations.</p>
          <PrimaryButton label="Go Back" onPress={() => navigate(`/scenarios/${scenarioId}`)} />
        </div>
      </Screen>
    );
  }

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md, marginBottom: spacing.sm }}>
          <button 
            onClick={() => navigate(`/scenarios/${scenarioId}`)}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: colors.primary, display: 'flex', alignItems: 'center', padding: 0 }}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M19 12H5M12 19l-7-7 7-7"/>
            </svg>
          </button>
          <span style={{ fontSize: 14, fontWeight: 800, color: colors.accent, textTransform: 'uppercase' }}>Conversations</span>
        </div>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Choose a Story</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xs }}>Practice real-world situations with branching paths.</p>
      </header>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
        {scenario.scriptedConversations?.map((conv, idx) => (
          <button
            key={conv.id}
            onClick={() => navigate(`/scenarios/${scenarioId}/conversation/${conv.id}`)}
            className="card fade-in"
            style={{
              display: 'flex',
              flexDirection: 'row',
              alignItems: 'center',
              gap: spacing.lg,
              padding: spacing.lg,
              textAlign: 'left',
              border: `2px solid ${colors.border}`,
              backgroundColor: colors.surface,
              cursor: 'pointer'
            }}
          >
            <div style={{ 
              width: 32, 
              height: 32, 
              borderRadius: 16, 
              backgroundColor: colors.chipBg, 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center',
              fontSize: 14,
              fontWeight: 900,
              color: colors.primary,
              flexShrink: 0
            }}>{idx + 1}</div>
            <div style={{ flex: 1 }}>
              <h3 style={{ color: colors.primary, fontSize: 20, fontWeight: 800, margin: 0 }}>{conv.title}</h3>
              <p style={{ color: colors.textSecondary, fontSize: 15, margin: 0 }}>{conv.description}</p>
            </div>
            <div style={{ color: colors.accent, fontWeight: 800, fontSize: 12, textTransform: 'uppercase' }}>
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </div>
          </button>
        ))}
      </div>
    </Screen>
  );
};
