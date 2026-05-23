import React, { useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { useProgressStore } from '@shared/store/progressStore';
import { useSubscriptionStore } from '../store/subscriptionStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { findResumeScenario } from '@shared/utils/home';

export const HomeScreen: React.FC = () => {
  const navigate = useNavigate();
  const xp = useProgressStore(state => state.xp);
  const streak = useProgressStore(state => state.streak);
  const scenarioProgress = useProgressStore(state => state.scenarioProgress);
  const resumeScenario = findResumeScenario(scenarioProgress);

  const masteredCount = useMemo(() => {
    return Object.values(scenarioProgress).filter(p => p.conversationUnlocked).length;
  }, [scenarioProgress]);

  const recentActivity = useMemo(() => {
    // Simulated recent activity
    return [
      { id: 1, type: 'Allenamento', title: 'Vocabolario: Al Mercato', date: 'Oggi', xp: 40 },
      { id: 2, type: 'Gioco', title: 'Il Genere delle Parole', date: 'Ieri', xp: 15 },
      { id: 3, type: 'Grammatica', title: 'Articoli Determinativi', date: 'Ieri', xp: 20 },
    ];
  }, []);

  const { plan, isValid } = useSubscriptionStore();
  const isPremium = plan !== 'free' && isValid;

  return (
    <Screen style={{ backgroundColor: colors.bg }}>
      <div style={{ maxWidth: 800, margin: '0 auto', width: '100%', padding: `0 ${spacing.sm}px` }}>
        {isPremium && window.location.search.includes('premium=true') && (
          <div style={{ 
            backgroundColor: colors.success, 
            color: 'white', 
            padding: '8px 16px', 
            borderRadius: 8, 
            marginBottom: spacing.md,
            fontSize: 14,
            fontWeight: 900,
            textAlign: 'center'
          }}>
            MODALITÀ DEVELOPER: PREMIUM ATTIVATO 👑
          </div>
        )}
        <header style={{ marginBottom: spacing.xl, textAlign: 'left' }}>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Ciao! ☕</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
            Bentornato alla tua lezione di italiano.
          </p>
        </header>

        {/* Header Stats */}
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(2, 1fr)', 
          gap: spacing.md, 
          marginBottom: spacing.xl 
        }}>
          <div className="card active" style={{ textAlign: 'center', padding: spacing.lg }}>
            <div style={{ fontSize: 32, marginBottom: 8 }}>🔥</div>
            <div style={{ fontSize: 24, fontWeight: 900, color: colors.primary }}>{streak}</div>
            <div style={{ fontSize: 12, fontWeight: 900, color: colors.textSecondary, textTransform: 'uppercase', letterSpacing: 1 }}>Giorno di fila</div>
          </div>
          <div className="card active" style={{ textAlign: 'center', padding: spacing.lg }}>
            <div style={{ fontSize: 32, marginBottom: 8 }}>☕</div>
            <div style={{ fontSize: 24, fontWeight: 900, color: colors.primary }}>{xp}</div>
            <div style={{ fontSize: 12, fontWeight: 900, color: colors.textSecondary, textTransform: 'uppercase', letterSpacing: 1 }}>XP Totale</div>
          </div>
        </div>

        {/* Main Action Card */}
        {resumeScenario ? (
          <div className="card" style={{ 
            marginBottom: spacing.xl, 
            padding: spacing.xl,
            background: `linear-gradient(135deg, ${colors.surface} 0%, ${colors.bg} 100%)`,
            borderLeft: `8px solid ${colors.accent}`
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: spacing.sm }}>
              <span style={{ color: colors.accent, fontSize: 12, fontWeight: 900, textTransform: 'uppercase', letterSpacing: 1.5 }}>Continua ad imparare</span>
              <span style={{ fontSize: 24 }}>🇮🇹</span>
            </div>
            <h3 style={{ color: colors.primary, fontSize: 26, fontWeight: 900, margin: 0 }}>{resumeScenario.title}</h3>
            <p style={{ color: colors.textSecondary, fontSize: 16, margin: `${spacing.sm}px 0 ${spacing.lg}px` }}>{resumeScenario.label}</p>
            
            <PrimaryButton 
              label="Riprendi Lezione" 
              onPress={() => {
                const pathMap: Record<string, string> = {
                  'VocabularyTraining': `/scenarios/${resumeScenario.route.params.scenarioId}/vocabulary`,
                  'PhraseTraining': `/scenarios/${resumeScenario.route.params.scenarioId}/phrases`,
                  'SentenceTraining': `/scenarios/${resumeScenario.route.params.scenarioId}/sentences`,
                  'Conversation': `/scenarios/${resumeScenario.route.params.scenarioId}/conversation`,
                };
                navigate(pathMap[resumeScenario.route.name] || '/scenarios');
              }} 
              variant="primary"
            />
          </div>
        ) : (
          <div className="card" style={{ 
            marginBottom: spacing.xl, 
            padding: spacing.xl,
            background: `linear-gradient(135deg, ${colors.surface} 0%, ${colors.bg} 100%)`,
            borderLeft: `8px solid ${colors.accent}`
          }}>
            <h2 style={{ color: colors.primary, fontSize: 24, fontWeight: 900, marginBottom: 8 }}>Inizia ora!</h2>
            <p style={{ color: colors.textSecondary, marginBottom: spacing.lg }}>Hai completato {masteredCount} scenari finora. Scegline uno nuovo!</p>
            
            <PrimaryButton 
              label="Sfoglia Scenari" 
              onPress={() => navigate('/scenarios')} 
              variant="primary"
            />
          </div>
        )}

        {/* Recent Activity */}
        <div style={{ marginBottom: spacing.xl }}>
          <h3 style={{ color: colors.primary, fontWeight: 900, marginBottom: spacing.md, fontSize: 18 }}>Attività Recente</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
            {recentActivity.map(activity => (
              <div key={activity.id} className="card" style={{ 
                display: 'flex', 
                justifyContent: 'space-between', 
                alignItems: 'center',
                padding: '12px 20px',
                cursor: 'default'
              }}>
                <div>
                  <div style={{ fontSize: 10, fontWeight: 900, color: colors.accent, textTransform: 'uppercase' }}>{activity.type}</div>
                  <div style={{ fontWeight: 700, color: colors.primary }}>{activity.title}</div>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontWeight: 900, color: colors.success }}>+{activity.xp} XP</div>
                  <div style={{ fontSize: 10, color: colors.textSecondary }}>{activity.date}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Quick Links Grid */}
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(2, 1fr)', 
          gap: spacing.md,
          marginBottom: spacing.xxl
        }}>
          <div className="card active" onClick={() => navigate('/games')} style={{ cursor: 'pointer', padding: spacing.lg, textAlign: 'center' }}>
            <div style={{ fontSize: 24, marginBottom: 8 }}>🎮</div>
            <div style={{ fontWeight: 900, color: colors.primary }}>Giochi</div>
          </div>
          <div className="card active" onClick={() => navigate('/review')} style={{ cursor: 'pointer', padding: spacing.lg, textAlign: 'center' }}>
            <div style={{ fontSize: 24, marginBottom: 8 }}>🔁</div>
            <div style={{ fontWeight: 900, color: colors.primary }}>Ripassa</div>
          </div>
        </div>
      </div>
    </Screen>
  );
};
