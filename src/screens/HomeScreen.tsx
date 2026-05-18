import React from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { foundationLessons } from '@shared/data/foundations';
import { useProgressStore } from '@shared/store/progressStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { calculateFoundationProgress, findResumeScenario } from '@shared/utils/home';

export const HomeScreen: React.FC = () => {
  const navigate = useNavigate();
  const foundationScores = useProgressStore(state => state.foundationScores);
  const scenarioProgress = useProgressStore(state => state.scenarioProgress);
  const resumeScenario = findResumeScenario(scenarioProgress);
  const foundationProgress = calculateFoundationProgress(
    foundationScores,
    foundationLessons.length,
  );

  const areFoundationsPassed = useProgressStore(state => state.areFoundationsPassed());

  return (
    <Screen>
      <header style={{ marginBottom: spacing.xl, textAlign: 'left', padding: `0 ${spacing.sm}px` }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Ciao! ☕</h1>
        <p style={{ color: colors.textSecondary, fontSize: 18, marginTop: spacing.xxs }}>
          Welcome back to your Italian lesson.
        </p>
      </header>

      <div className="home-desktop-layout">
        <div className="home-col">
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: spacing.md, marginBottom: spacing.lg }}>
            <div className="card active" style={{ textAlign: 'center', padding: spacing.md }}>
              <div style={{ fontSize: 32, marginBottom: 8 }}>🔥</div>
              <div style={{ fontSize: 24, fontWeight: 900, color: colors.primary }}>{Object.keys(scenarioProgress).length}</div>
              <div style={{ fontSize: 12, color: colors.textSecondary, textTransform: 'uppercase', fontWeight: 900, letterSpacing: 1 }}>Scenarios</div>
            </div>
            <div className="card active" style={{ textAlign: 'center', padding: spacing.md }}>
              <div style={{ fontSize: 32, marginBottom: 8 }}>🎯</div>
              <div style={{ fontSize: 24, fontWeight: 900, color: colors.primary }}>{foundationProgress}%</div>
              <div style={{ fontSize: 12, color: colors.textSecondary, textTransform: 'uppercase', fontWeight: 900, letterSpacing: 1 }}>Mastery</div>
            </div>
          </div>

          {!areFoundationsPassed && (
            <div className="card" style={{ 
              marginBottom: spacing.lg, 
              backgroundColor: 'rgba(227, 155, 20, 0.05)',
              borderColor: colors.warning,
              cursor: 'default'
            }}>
              <h2 style={{ color: colors.warning, fontSize: 20, fontWeight: 900, margin: 0, display: 'flex', alignItems: 'center', gap: 8 }}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                </svg>
                Foundations incomplete
              </h2>
              <p style={{ color: colors.textSecondary, fontSize: 16, margin: `${spacing.sm}px 0` }}>
                Complete the foundation lessons to unlock 100+ real-world scenarios.
              </p>
              <div className="progress-bar-container" style={{ margin: `${spacing.md}px 0` }}>
                <div className="progress-bar-fill" style={{ width: `${foundationProgress}%`, backgroundColor: colors.warning }} />
              </div>
              <PrimaryButton 
                label="Resume Foundations" 
                onPress={() => navigate('/foundations')}
                variant="accent"
              />
            </div>
          )}
        </div>

        <div className="home-col">
          {resumeScenario && (
            <div className="card" style={{ marginBottom: spacing.lg, padding: spacing.lg }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: spacing.sm }}>
                <span style={{ color: colors.accent, fontSize: 12, fontWeight: 900, textTransform: 'uppercase', letterSpacing: 1.5 }}>Current Scenario</span>
                <span style={{ fontSize: 24 }}>🇮🇹</span>
              </div>
              <h3 style={{ color: colors.primary, fontSize: 26, fontWeight: 900, margin: 0 }}>{resumeScenario.title}</h3>
              <p style={{ color: colors.textSecondary, fontSize: 16, margin: `${spacing.sm}px 0 ${spacing.lg}px` }}>{resumeScenario.label}</p>
              <PrimaryButton
                label="Continue Learning"
                onPress={() => {
                  const pathMap: Record<string, string> = {
                    'VocabularyTraining': `/scenarios/${resumeScenario.route.params.scenarioId}/vocabulary`,
                    'PhraseTraining': `/scenarios/${resumeScenario.route.params.scenarioId}/phrases`,
                    'SentenceTraining': `/scenarios/${resumeScenario.route.params.scenarioId}/sentences`,
                    'Conversation': `/scenarios/${resumeScenario.route.params.scenarioId}/conversation`,
                  };
                  navigate(pathMap[resumeScenario.route.name] || '/scenarios');
                }}
              />
            </div>
          )}

          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <PrimaryButton
              label="Grammar Lessons"
              onPress={() => navigate('/grammar')}
              variant="secondary"
              icon={
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>
                </svg>
              }
            />
            <PrimaryButton
              label="Browse Scenarios"
              onPress={() => navigate('/scenarios')}
              variant="secondary"
              icon={
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                </svg>
              }
            />
            <PrimaryButton 
              label="Daily Review" 
              onPress={() => navigate('/review')}
              variant="accent"
              icon={
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/>
                  <polyline points="21 3 21 8 16 8"/>
                </svg>
              }
            />
          </div>
        </div>
      </div>
    </Screen>
  );
};
