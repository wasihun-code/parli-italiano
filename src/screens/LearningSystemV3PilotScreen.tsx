import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { LearningPathGenerator } from '../services/learningPathGenerator';
import { SessionGenerator } from '../services/sessionGenerator';
import { SessionPersistenceService } from '../services/sessionPersistenceService';
import { resolveExercise } from '../exercises/resolver';
import { ExerciseRenderer } from '../components/learning/ExerciseRenderer';
import { FeedbackOverlay } from '../components/learning/FeedbackOverlay';
import { SessionValidator } from '../services/sessionValidator';
import { PathGenerationInput, LearningStep } from '../types/learningPath';

import { ValidationResult } from '../exercises/types';
import { ConversationReadinessService } from '../services/conversationReadinessService';
import { GlobalProgressService } from '../services/globalProgressService';
import { useProgressStore } from '../store/progressStore';
import { db } from '../lib/db';
import { colors } from '../theme/colors';
import { spacing } from '../theme/spacing';
import { loadProductionScenarioData } from '../data/corpusLoader';
import { audioService } from '../lib/audioService';
import { Tts } from '../lib/tts';

export const LearningSystemV3PilotScreen: React.FC = () => {
  const { scenarioId, lessonId } = useParams<{ scenarioId: string, lessonId: string }>();
  const currentScenarioId = Number(scenarioId || 22);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [hasStarted, setHasStarted] = useState(false);
  const [scenarioData, setScenarioData] = useState<any>(null);
  const [learningPath, setLearningPath] = useState<LearningStep[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [lastResult, setLastResult] = useState<ValidationResult | null>(null);
  
  // Pilot Local State for Mastery Simulation (Eventually moves to GlobalProgressService)
  const [localMastery, setLocalMastery] = useState<Record<string, number>>({});
  const [reviewQueue] = useState<string[]>(['v184']); // 'portone' in Review Queue for pilot demo

  useEffect(() => {
    async function initPilot() {
      try {
        const data = await loadProductionScenarioData(currentScenarioId);
        if (!data) throw new Error("Scenario data not found");
        setScenarioData(data);

        // Fetch current mastery from DB to link readiness meters
        const allItemIds = [
          ...data.vocabulary.map((v: any) => v.id),
          ...data.phrases.map((p: any) => p.id),
          ...data.sentences.map((s: any) => s.id)
        ];
        
        const existingProgress = await db.global_progress.bulkGet(allItemIds);
        const masteryMap: Record<string, number> = {};
        existingProgress.forEach((p, i) => {
          if (p) masteryMap[allItemIds[i]] = p.mastery_level / 4; // Normalize to 0-1
        });
        setLocalMastery(masteryMap);

        // Try to load saved session
        const saved = await SessionPersistenceService.loadSession(currentScenarioId);
        
        if (saved && !saved.is_completed) {
          const loadedSteps = JSON.parse(saved.steps_json);
          if (SessionValidator.validateSession(loadedSteps, data)) {
            setLearningPath(loadedSteps);
            setCurrentIndex(saved.current_step_index);
          } else {
            throw new Error("Saved session corrupted or invalid. Please restart.");
          }
        } else {
          const input: PathGenerationInput = {
            scenarioId: currentScenarioId,
            scenarioData: data,
            globalMastery: localMastery,
            reviewQueue: reviewQueue
          };

          const fullPathResult = LearningPathGenerator.generatePath(input);
          
          // PILOT CHUNKING: Convert Master Path to Session
          const pilotTypes = ['Listen', 'Match', 'Spelling'];
          const filteredSteps = fullPathResult.path.steps.filter(s => pilotTypes.includes(s.exerciseType));
          const sessionSteps = SessionGenerator.generateSession({ ...fullPathResult.path, steps: filteredSteps });
          
          if (!SessionValidator.validateSession(sessionSteps, data)) {
            throw new Error("Generated session contains invalid exercises. Cannot start.");
          }

          setLearningPath(sessionSteps);
          setCurrentIndex(0);
          
          // Initial persistence save
          await SessionPersistenceService.saveSession(currentScenarioId, 0, sessionSteps, false);
        }
        
        setLoading(false);
      } catch (e) {
        setError(e instanceof Error ? e.message : 'Unknown error');
        setLoading(false);
      }
    }
    initPilot();
  }, [currentScenarioId]);

  const currentStep = learningPath[currentIndex];

  const { definition, payload } = useMemo(() => {
    if (!currentStep || !scenarioData) return { definition: null, payload: null };
    return resolveExercise(currentStep, scenarioData);
  }, [currentStep, scenarioData]);

  const handleComplete = useCallback(async (result: ValidationResult) => {
    if (lastResult) return; // Prevent double completion

    setLastResult(result);
    
    if (result.isValid) {
      audioService.playCorrect();
    } else {
      audioService.playIncorrect();
    }

    // Update Global Progress (Actual Persistence)
    await GlobalProgressService.recordAnswer(currentStep.itemId, result.isValid, currentScenarioId);
    
    // Update local state for readiness UI update
    const oldScore = localMastery[currentStep.itemId] ?? 0;
    // Boost impact for pilot visibility
    const newScore = result.isValid ? Math.min(1.0, oldScore + 0.4) : Math.max(0.0, oldScore - 0.2);
    setLocalMastery(prev => ({ ...prev, [currentStep.itemId]: newScore }));

  }, [currentStep, lastResult, localMastery, currentScenarioId]);

  const handleContinue = useCallback(async () => {
    if (!lastResult) return;

    const nextIndex = currentIndex + 1;
    const isSessionEnd = nextIndex >= learningPath.length;

    if (isSessionEnd) {
      // 1. Mark Lesson as Complete in Legacy Store (to unlock next lesson)
      if (lessonId) {
        useProgressStore.getState().completeMiniLesson(currentScenarioId, lessonId, scenarioData?.miniLessons?.length || 6);
      }
      
      // 2. Persist V3 Session state
      await SessionPersistenceService.saveSession(currentScenarioId, currentIndex, learningPath, true);
      
      audioService.playComplete();
      alert("Sessione completata! La prossima lezione è sbloccata.");
      navigate(`/scenarios/${currentScenarioId}`);
    } else {
      setCurrentIndex(nextIndex);
      setLastResult(null);
      await SessionPersistenceService.saveSession(currentScenarioId, nextIndex, learningPath, false);
    }
  }, [currentIndex, lastResult, learningPath, navigate, lessonId, currentScenarioId, scenarioData]);

  const currentLesson = useMemo(() => {
    return scenarioData?.miniLessons?.find((l: any) => l.id === lessonId);
  }, [scenarioData, lessonId]);

  const displayProgress = useMemo(() => {
    if (!scenarioData) return { lesson: 0, scenario: 0 };
    
    let lessonMastery = 0;
    if (currentLesson) {
      const lessonItemIds = currentLesson.sections.flatMap((s: any) => s.exerciseIds);
      if (lessonItemIds.length > 0) {
        const sum = lessonItemIds.reduce((acc: number, id: string) => acc + (localMastery[id] ?? 0), 0);
        lessonMastery = Math.round((sum / lessonItemIds.length) * 100);
      }
    }

    const allItems = [...scenarioData.vocabulary, ...scenarioData.phrases, ...scenarioData.sentences];
    let scenarioProgress = 0;
    if (allItems.length > 0) {
      const sum = allItems.reduce((acc: number, item: any) => acc + (localMastery[item.id] ?? 0), 0);
      scenarioProgress = Math.round((sum / allItems.length) * 100);
    }

    return {
      lesson: lessonMastery,
      scenario: scenarioProgress
    };
  }, [localMastery, scenarioData, currentLesson]);

  const readiness = useMemo(() => {
    if (!scenarioData) return null;
    return ConversationReadinessService.checkReadiness({
      scenarioId: currentScenarioId,
      scenarioData,
      globalMastery: localMastery,
      reviewQueue: []
    });
  }, [localMastery, scenarioData, currentScenarioId]);

  // Keyboard Navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        const confirmExit = window.confirm("Vuoi uscire dalla sessione?");
        if (confirmExit) navigate('/');
        return;
      }

      if (e.key === ' ') {
        e.preventDefault();
        if (payload) Tts.speak(payload.italian, payload.audio);
        return;
      }

      if (e.key === 'Enter') {
        if (lastResult) {
          handleContinue();
        }
        return;
      }

      // 1-4 selection is currently handled within components if they support it
      // but we could hoist it here if we establish a standard ref or interface.
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [lastResult, handleContinue, payload, navigate]);

  if (loading) return <Screen><div style={{ padding: spacing.xl, textAlign: 'center' }}>Caricamento scenario...</div></Screen>;
  if (error) return <Screen><div style={{ padding: spacing.xl, color: colors.error, textAlign: 'center' }}>Errore: {error}</div></Screen>;
  
  if (!hasStarted) {
    return (
      <Screen style={{ backgroundColor: colors.bg, padding: spacing.xl, alignItems: 'center' }}>
        <div style={{ 
          maxWidth: 600, 
          width: '100%', 
          backgroundColor: colors.surface, 
          borderRadius: 24, 
          overflow: 'hidden',
          boxShadow: '0 8px 32px rgba(0,0,0,0.1)'
        }}>
          {/* Scenario Banner */}
          <div style={{ 
            backgroundColor: colors.primary, 
            color: colors.onPrimary, 
            padding: spacing.xl, 
            textAlign: 'center' 
          }}>
            <div style={{ fontSize: 48, marginBottom: spacing.sm }}>🗝️</div>
            <h1 style={{ fontSize: 28, fontWeight: 900, margin: '0 0 8px 0' }}>
              {scenarioData.title || 'Apartment Key Pickup'}
            </h1>
            <div style={{ fontSize: 16, opacity: 0.9 }}>
              Conversation Stage: <span style={{ fontWeight: 700 }}>Arrival</span>
            </div>
          </div>

          <div style={{ padding: spacing.xl }}>
            <h2 style={{ color: colors.primary, fontSize: 22, fontWeight: 800, marginTop: 0 }}>
              Current Goal
            </h2>
            <p style={{ color: colors.textSecondary, fontSize: 16, marginBottom: spacing.xl, lineHeight: 1.5 }}>
              Master the vocabulary and sentences needed to complete: <strong style={{ color: colors.primary }}>{currentLesson?.goal || 'Preparazione'}</strong>.
            </p>
            
            <h3 style={{ color: colors.accent, fontSize: 18, fontWeight: 800 }}>
              Why This Matters
            </h3>
            <p style={{ color: colors.textSecondary, fontSize: 16, marginBottom: spacing.xl, lineHeight: 1.5 }}>
              By mastering these specific phrases, you will build the conversational reflexes necessary for the upcoming scenario.
            </p>

            <div style={{ backgroundColor: colors.chipBg, padding: spacing.lg, borderRadius: 16, marginBottom: spacing.xl }}>
              <h4 style={{ margin: '0 0 12px 0', fontSize: 16, color: colors.primary }}>Conversation Preview</h4>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                <div style={{ display: 'flex', gap: 12 }}>
                  <span style={{ fontSize: 24 }}>👱‍♂️</span>
                  <div style={{ backgroundColor: 'white', padding: '8px 12px', borderRadius: 12, fontSize: 14, color: colors.textPrimary, border: `1px solid ${colors.border}` }}>
                    "Scusi, può ripetere?"
                  </div>
                </div>
                <div style={{ display: 'flex', gap: 12, justifyContent: 'flex-end' }}>
                  <div style={{ backgroundColor: colors.primary, color: 'white', padding: '8px 12px', borderRadius: 12, fontSize: 14 }}>
                    "Certo, nessun problema."
                  </div>
                  <span style={{ fontSize: 24 }}>👩</span>
                </div>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md, alignItems: 'center' }}>
              <PrimaryButton label="Inizia Lezione" onPress={() => setHasStarted(true)} style={{ width: '100%', maxWidth: 300 }} />
              <button 
                onClick={() => navigate('/')}
                style={{ background: 'none', border: 'none', color: colors.textSecondary, cursor: 'pointer', textDecoration: 'underline', fontWeight: 700, padding: spacing.sm }}
              >
                Torna alla Home
              </button>
            </div>
          </div>
        </div>
      </Screen>
    );
  }

  if (!currentStep) return <Screen><div>No steps found.</div></Screen>;

  return (
    <Screen style={{ backgroundColor: colors.bg, position: 'relative', padding: 0 }}>
      {/* Fullscreen Header */}
      <div style={{
        padding: `${spacing.md}px ${spacing.lg}px`,
        backgroundColor: colors.surface,
        borderBottom: `2px solid ${colors.border}`,
        display: 'flex',
        alignItems: 'center',
        gap: spacing.md
      }}>
        <button 
          onClick={() => { if(window.confirm("Esci dalla sessione?")) navigate('/'); }}
          style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 4 }}
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={colors.textSecondary} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>
        
        <div style={{ flex: 1 }}>
          <div style={{ fontSize: 14, fontWeight: 900, color: colors.primary, marginBottom: 4, display: 'flex', alignItems: 'center', gap: 8 }}>
             <span>{scenarioData.title}</span>
             <span style={{ color: colors.textSecondary, fontWeight: 500 }}>•</span>
             <span style={{ color: colors.accent }}>{currentLesson?.goal || 'Preparazione'}</span>
          </div>
          <div style={{ height: 10, backgroundColor: colors.border, borderRadius: 5, overflow: 'hidden' }}>
            <div style={{ 
              height: '100%', 
              backgroundColor: colors.success, 
              width: `${((currentIndex + 1) / learningPath.length) * 100}%`, 
              transition: 'width 0.4s cubic-bezier(0.4, 0, 0.2, 1)' 
            }} />
          </div>
        </div>

        <div style={{ 
          padding: '4px 12px', 
          backgroundColor: colors.chipBg, 
          borderRadius: 16, 
          fontSize: 14, 
          fontWeight: 900, 
          color: colors.primary 
        }}>
          {currentIndex + 1}/{learningPath.length}
        </div>
      </div>

      {/* Context Banner */}
      <div style={{ 
        padding: '8px 16px', 
        backgroundColor: colors.surface, 
        borderBottom: `1px solid ${colors.border}`,
        textAlign: 'center',
        fontSize: 13,
        fontWeight: 700,
        color: colors.textSecondary,
        display: 'flex',
        justifyContent: 'center',
        gap: 12
      }}>
        <span style={{ color: colors.accent }}>CONTEXT:</span>
        <span>Situazione: {currentLesson?.title || scenarioData.title}</span>
        <span style={{ opacity: 0.3 }}>|</span>
        <span>Relevanza: Preparazione per Conversazione</span>
      </div>

      {/* Main Content Area - Centered & Immersive */}
      <main style={{ 
        flex: 1, 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center', 
        justifyContent: 'center',
        maxWidth: 1000,
        margin: '0 auto',
        width: '100%',
        padding: spacing.xl,
        position: 'relative',
        boxSizing: 'border-box'
      }}>
        <div style={{
          width: '100%',
          flex: 1,
          backgroundColor: colors.surface,
          borderRadius: 32,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          boxShadow: '0 12px 48px rgba(0,0,0,0.06)',
          overflow: 'hidden'
        }}>
          {definition && payload && (
            <ExerciseRenderer 
              key={currentStep.id}
              definition={definition} 
              payload={payload} 
              onComplete={handleComplete} 
            />
          )}
        </div>

        {lastResult && (
          <FeedbackOverlay 
            result={lastResult} 
            onContinue={handleContinue} 
          />
        )}
      </main>

      {/* Minimal Footer for Status */}
      <footer style={{ 
        padding: spacing.md, 
        borderTop: `1px solid ${colors.border}`,
        backgroundColor: colors.surface,
        display: 'flex', 
        justifyContent: 'center', 
        gap: spacing.xl,
      }}>
        <StatMini label="Lesson Mastery" value={displayProgress.lesson} isReady={readiness?.isReady} />
        <StatMini label="Scenario Readiness" value={displayProgress.scenario} isReady={readiness?.isReady} />
      </footer>
    </Screen>
  );
};

const StatMini: React.FC<{ label: string, value: number, isReady?: boolean }> = ({ label, value, isReady }) => (
  <div style={{ textAlign: 'center', minWidth: 60 }}>
    <div style={{ fontSize: 10, fontWeight: 900, color: colors.textSecondary, textTransform: 'uppercase' }}>{label}</div>
    <div style={{ fontSize: 16, fontWeight: 900, color: isReady ? colors.success : colors.primary }}>
      {value > 0 && value < 1 ? value.toFixed(1) : Math.round(value)}%
    </div>
  </div>
);
