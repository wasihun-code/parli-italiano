import React, { useEffect, useMemo, useState, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { setupDatabase } from '../lib/db';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { scenarios } from '@shared/data/scenarios';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';
import { shuffle } from '@shared/utils/trainingUi';

type TrainingItem = {
  type: 'vocabulary' | 'phrase' | 'sentence';
  data: any; // Raw DB row
  isMastery: boolean;
  sectionTitle: string;
  sectionType: string;
};

const getTimestamp = () => new Date().toLocaleTimeString('it-IT', { hour12: false }) + '.' + new Date().getMilliseconds().toString().padStart(3, '0');

export const MiniLessonTrainingScreen: React.FC = () => {
  const { scenarioId, lessonId } = useParams<{ scenarioId: string; lessonId: string }>();
  const navigate = useNavigate();
  
  const scenario = scenarios.find(s => s.id === Number(scenarioId));
  const lesson = scenario?.miniLessons?.find(l => l.id === lessonId);

  const { feedbackLanguage } = useUserSettingsStore();
  const isIt = feedbackLanguage === 'it';

  const [items, setItems] = useState<TrainingItem[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  
  const [selectedAnswer, setSelectedAnswer] = useState<string>();
  const [feedback, setFeedback] = useState<{ status: 'correct' | 'incorrect' | 'nearly_correct'; correctAnswer: string; explanation?: string }>();
  
  const [loading, setLoading] = useState(true);
  const [showMasterySplash, setShowMasterySplash] = useState(false);
  const [masterySplashShownForIndex, setMasterySplashShownForIndex] = useState(-1);

  useEffect(() => {
    let cancelled = false;
    async function loadData() {
      if (!scenario || !lesson) return;
      
      console.log(`[${getTimestamp()}] [UI] Waiting for database setup...`);
      await setupDatabase();
      
      console.log(`[${getTimestamp()}] [UI] Using JSON Source of Truth for Scenario ${scenarioId}`);
      
      // ABSOLUTE SOURCE OF TRUTH: Use registry data directly
      const vocab = scenario.vocabulary;
      const phrases = scenario.phrases;
      const sentences = scenario.sentences;

      console.log(`[${getTimestamp()}] [UI] Registry counts: V:${vocab.length}, P:${phrases.length}, S:${sentences.length}`);

      if (cancelled) return;

      const buildItems = (section: any) => {
        const isMastery = section.type === 'mastery';
        return section.exerciseIds.map((id: string) => {
          let type: 'vocabulary' | 'phrase' | 'sentence' = 'vocabulary';
          let data: any = vocab.find(v => v.id === id);
          if (!data) { data = phrases.find(p => p.id === id); type = 'phrase'; }
          if (!data) { data = sentences.find(s => s.id === id); type = 'sentence'; }
          
          if (!data) {
             console.error(`[${getTimestamp()}] [UI] CRITICAL MISSING ID: ${id}. Registry Search Result: null`);
          }
          
          return data ? { type, data, isMastery, sectionTitle: section.title, sectionType: section.type } : null;
        }).filter(Boolean) as TrainingItem[];
      };

      console.log(`[${getTimestamp()}] [UI] Starting finalSequence construction...`);
      const finalSequence = lesson.sections.flatMap(buildItems);
      console.log(`[${getTimestamp()}] [UI] finalSequence construction complete. Length: ${finalSequence.length}`);

      setItems(finalSequence);
      setLoading(false);
    }
    loadData();
    return () => { cancelled = true; };
  }, [scenario, lesson, scenarioId]);

  const currentItem = items[currentIndex];

  useEffect(() => {
    if (currentItem?.isMastery && !feedback && !showMasterySplash && currentIndex > 0 && !items[currentIndex - 1]?.isMastery && masterySplashShownForIndex !== currentIndex) {
      setShowMasterySplash(true);
      setMasterySplashShownForIndex(currentIndex);
    }
  }, [currentItem, feedback, showMasterySplash, currentIndex, items, masterySplashShownForIndex]);

  const playAudio = useCallback((): void => {
    if (currentItem) {
      void Tts.speak(currentItem.data?.italian || '', currentItem.data?.audio);
    }
  }, [currentItem]);

  // Auto-play audio on new item
  useEffect(() => {
    if (currentItem && !feedback && !showMasterySplash) {
      playAudio();
    }
  }, [currentItem, feedback, showMasterySplash, playAudio]);

  const submitAnswer = useCallback((ans: string): void => {
    if (!currentItem || feedback) return;
    
    // For this prototype, all exercises are simple multiple choice
    const isCorrect = ans === currentItem.data?.italian;
    const status = isCorrect ? 'correct' : 'incorrect';
    
    let explanation: string | undefined;
    if (currentItem.data?.feedback) {
      if (status === 'correct') {
        explanation = isIt ? currentItem.data.feedback.correctItalian : currentItem.data.feedback.correctEnglish;
      } else {
        explanation = isIt ? currentItem.data.feedback.incorrectItalian : currentItem.data.feedback.incorrectEnglish;
      }
    } else if (status === 'incorrect') {
      explanation = getWrongAnswerExplanation({
        type: currentItem.type,
        italian: currentItem.data?.italian,
        correctAnswer: currentItem.data?.italian || ''
      });
    }

    setFeedback({ status, correctAnswer: currentItem.data?.italian || '', explanation });
  }, [currentItem, feedback, isIt]);

  const advance = useCallback((): void => {
    setFeedback(undefined);
    setSelectedAnswer(undefined);
    
    if (currentIndex + 1 >= items.length) {
      navigate(`/scenarios/${scenarioId}/lesson/${lessonId}/complete`, { replace: true });
    } else {
      setCurrentIndex(currentIndex + 1);
    }
  }, [currentIndex, items.length, navigate, scenarioId, lessonId]);

  // Generate options for the current item
  const options = useMemo(() => {
    if (!currentItem) return [];
    if (currentItem.data?.choicesItalian) {
      return shuffle([...currentItem.data.choicesItalian]);
    }
    // Fallback if no choices (shouldn't happen in production corpus)
    return shuffle([currentItem.data?.italian || '', "Distractor 1", "Distractor 2", "Distractor 3"]);
  }, [currentItem]);

  if (loading || !scenario || !lesson) {
    return <Screen><div style={{ padding: spacing.xl }}>Loading exercises...</div></Screen>;
  }

  // Error state: Curriculum mismatch
  if (items.length === 0) {
    return (
      <Screen>
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'center', alignItems: 'center', textAlign: 'center', padding: spacing.xl }}>
          <div style={{ fontSize: 64, marginBottom: spacing.lg }}>⚠️</div>
          <h1 style={{ color: colors.primary, fontSize: 24, fontWeight: 900, marginBottom: spacing.md }}>Curriculum Mismatch</h1>
          <p style={{ color: colors.textSecondary, fontSize: 16, marginBottom: spacing.xxl }}>
            The lesson content could not be loaded from the database. This usually happens after a data update.
          </p>
          <PrimaryButton label="Reload & Repair" onPress={() => window.location.reload()} />
          <button 
            onClick={() => navigate(`/scenarios/${scenarioId}`)}
            style={{ marginTop: spacing.lg, background: 'none', border: 'none', color: colors.textSecondary, fontWeight: 700, cursor: 'pointer', textDecoration: 'underline' }}
          >
            Go Back
          </button>
        </div>
      </Screen>
    );
  }

  if (showMasterySplash) {
    return (
      <Screen>
        <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'center', alignItems: 'center', textAlign: 'center', padding: spacing.xl }}>
          <div style={{ fontSize: 64, marginBottom: spacing.lg }}>👑</div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, marginBottom: spacing.md }}>Mastery Check</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginBottom: spacing.xxl }}>Let's see if you can handle this situation.</p>
          <PrimaryButton label="Start Mastery Check" onPress={() => setShowMasterySplash(false)} />
        </div>
      </Screen>
    );
  }

  const progressFraction = items.length > 0 ? Math.max(0, Math.min(1, currentIndex / items.length)) : 0;

  if (!currentItem) {
    return <Screen><div style={{ padding: spacing.xl }}>Loading exercises...</div></Screen>;
  }

  return (
    <Screen>
      <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
        <header style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: spacing.lg }}>
          <button onClick={() => navigate(`/scenarios/${scenarioId}`)} style={{ background: 'none', border: 'none', color: colors.textSecondary, fontSize: 24, cursor: 'pointer' }}>×</button>
          <div style={{ flex: 1, margin: '0 16px', height: 8, backgroundColor: colors.border, borderRadius: 4, overflow: 'hidden' }}>
            <div style={{ height: '100%', backgroundColor: colors.success, width: `${progressFraction * 100}%`, transition: 'width 0.3s ease' }} />
          </div>
          <div style={{ fontWeight: 900, color: colors.primary }}>{currentIndex}/{items.length}</div>
        </header>

        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflowY: 'auto', paddingBottom: spacing.xxl }}>
          <div style={{ marginBottom: spacing.xl, textAlign: 'center' }}>
             <span style={{ 
               backgroundColor: currentItem.isMastery ? 'rgba(255, 193, 7, 0.2)' : colors.chipBg, 
               color: currentItem.isMastery ? '#f57c00' : colors.primary, 
               fontSize: 12, 
               fontWeight: 900, 
               padding: '4px 10px', 
               borderRadius: 8,
               textTransform: 'uppercase'
             }}>
               {currentItem.sectionTitle}
             </span>
          </div>

          <h2 style={{ fontSize: 24, color: colors.primary, fontWeight: 800, textAlign: 'center', marginBottom: spacing.xl }}>
            {currentItem.data?.english ?? '...'}
          </h2>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.md }}>
            {options.map((choice) => (
              <button
                key={choice}
                onClick={() => {
                  if (feedback) return;
                  void Tts.speak(choice);
                  setSelectedAnswer(choice);
                  submitAnswer(choice);
                }}
                className={`card ${selectedAnswer === choice ? 'active' : ''}`}
                style={{
                  padding: spacing.lg,
                  textAlign: 'left',
                  display: 'flex',
                  alignItems: 'center',
                  gap: spacing.md,
                  fontSize: 18,
                  fontWeight: 700,
                  color: colors.primary,
                  border: selectedAnswer === choice ? `2px solid ${colors.accent}` : `2px solid transparent`,
                  backgroundColor: selectedAnswer === choice ? 'rgba(212, 163, 115, 0.1)' : colors.surface,
                  cursor: feedback ? 'default' : 'pointer',
                  opacity: feedback && choice !== currentItem.data?.italian && choice !== selectedAnswer ? 0.5 : 1
                }}
              >
                {choice}
              </button>
            ))}
          </div>

          {feedback && (
            <div className="fade-in" style={{ marginTop: spacing.xl }}>
              <FeedbackMessage
                type={feedback.status === 'incorrect' ? 'incorrect' : 'correct'}
                message={feedback.status === 'correct' || feedback.status === 'nearly_correct' ? 'Esatto!' : `Sbagliato. La risposta corretta è: ${feedback.correctAnswer}`}
                explanation={feedback.explanation}
              />
            </div>
          )}
        </div>

        <div style={{ marginTop: 'auto', paddingTop: spacing.md }}>
          {feedback && (
            <PrimaryButton 
              label="Continue" 
              onPress={advance} 
              variant={feedback.status === 'incorrect' ? 'secondary' : 'primary'} 
            />
          )}
        </div>
      </div>
    </Screen>
  );
};
