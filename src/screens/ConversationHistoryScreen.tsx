import React, { useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { useConversationStore } from '@shared/store/conversationStore';
import { scenarios } from '@shared/data/scenarios';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

export const ConversationHistoryScreen: React.FC = () => {
  const navigate = useNavigate();
  const allMessages = useConversationStore(state => state.messages);
  
  const conversationScenarios = useMemo(() => {
    const scenarioIdsWithMessages = Array.from(new Set(allMessages.map(m => m.scenarioId)));
    return scenarioIdsWithMessages
      .map(id => scenarios.find(s => s.id === id))
      .filter((s): s is typeof scenarios[0] => s !== undefined)
      .sort((a, b) => b.id - a.id); // Or sort by last message date if available
  }, [allMessages]);

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Conversations 💬</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
          Review your past chats with Antonio.
        </p>
      </header>

      {conversationScenarios.length === 0 ? (
        <div className="card" style={{ textAlign: 'center', padding: spacing.xl }}>
          <div style={{ fontSize: 64, marginBottom: spacing.md }}>☕</div>
          <h2 style={{ color: colors.primary }}>No conversations yet</h2>
          <p style={{ color: colors.textSecondary, marginBottom: spacing.lg }}>
            Complete training phases for a scenario to start chatting with Antonio!
          </p>
          <button 
            onClick={() => navigate('/scenarios')}
            style={{
              backgroundColor: colors.primary,
              color: 'white',
              border: 'none',
              padding: '12px 24px',
              borderRadius: 12,
              fontWeight: 800,
              cursor: 'pointer'
            }}
          >
            BROWSE SCENARIOS
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          {conversationScenarios.map(scenario => {
            const scenarioMessages = allMessages.filter(m => m.scenarioId === scenario.id);
            const lastMessage = scenarioMessages[scenarioMessages.length - 1];
            
            return (
              <div 
                key={scenario.id} 
                className="card fade-in" 
                onClick={() => navigate(`/scenarios/${scenario.id}/conversation`)}
                style={{ display: 'flex', alignItems: 'center', gap: spacing.md }}
              >
                <div style={{ 
                  width: 50, 
                  height: 50, 
                  borderRadius: 12, 
                  backgroundColor: colors.chipBg,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: 24
                }}>
                  💬
                </div>
                <div style={{ flex: 1 }}>
                  <h3 style={{ margin: 0, color: colors.primary }}>{scenario.title}</h3>
                  <p style={{ 
                    margin: '4px 0 0', 
                    color: colors.textSecondary, 
                    fontSize: 14,
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                    maxWidth: 250
                  }}>
                    {lastMessage ? lastMessage.text : 'Start chatting...'}
                  </p>
                </div>
                <div style={{ color: colors.accent }}>
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                    <path d="m9 18 6-6-6-6"/>
                  </svg>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </Screen>
  );
};
