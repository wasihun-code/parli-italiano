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

  const playAudio = useCallback((text?: string, audioData?: any): void => {
    const targetText = text || currentItem?.data?.italian || '';
    const targetAudio = audioData || currentItem?.data?.audio;
    if (targetText) {
      void Tts.speak(targetText, targetAudio);
    }
  }, [currentItem]);

  // Removed redundant post-submission autoplay useEffect to prevent double playback

  const submitAnswer = useCallback((ans: string): void => {
    if (!currentItem || feedback) return;

    // Play selected audio immediately (regardless of correctness)
    void Tts.speak(ans);

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

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        navigate(`/scenarios/${scenarioId}`);
        return;
      }

      if (showMasterySplash) {
        if (e.key === 'Enter') {
          setShowMasterySplash(false);
        }
        return;
      }
      
      if (e.key === ' ') {
        e.preventDefault();
        playAudio();
        return;
      }

      if (e.key === 'Enter') {
        if (feedback) {
          advance();
        }
        return;
      }

      // Choice selection (1-4)
      if (!feedback && options.length > 0) {
        const num = parseInt(e.key, 10);
        if (!isNaN(num) && num >= 1 && num <= options.length) {
          const choice = options[num - 1];
          setSelectedAnswer(choice);
          submitAnswer(choice);
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [navigate, scenarioId, showMasterySplash, feedback, options, playAudio, advance, submitAnswer]);

  if (loading || !scenario || !lesson) {
    return <Screen><div style={{ padding: spacing.xl }}>Loading exercises...</div></Screen>;
  }

  // Error state: Curriculum mismatch
  if (items.length === 0) {
    return (
      <Screen style={{ padding: spacing.xl, justifyContent: 'center', alignItems: 'center', textAlign: 'center' }}>
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
      </Screen>
    );
  }

  if (showMasterySplash) {
    return (
      <Screen style={{ padding: spacing.xl, justifyContent: 'center', alignItems: 'center', textAlign: 'center' }}>
          <div style={{ fontSize: 64, marginBottom: spacing.lg }}>👑</div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, marginBottom: spacing.md }}>Mastery Check</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, marginBottom: spacing.xxl }}>Let's see if you can handle this situation.</p>
          <PrimaryButton label="Start Mastery Check" onPress={() => setShowMasterySplash(false)} />
      </Screen>
    );
  }

  const progressFraction = items.length > 0 ? Math.max(0, Math.min(1, currentIndex / items.length)) : 0;

  if (!currentItem) {
    return <Screen><div style={{ padding: spacing.xl }}>Loading exercises...</div></Screen>;
  }

  return (
    <Screen style={{ padding: 0, backgroundColor: colors.bg }}>
      {/* Header */}
      <div style={{
        padding: spacing.md, 
        borderBottom: `1px solid ${colors.border}`, 
        backgroundColor: colors.surface,
        display: 'flex',
        alignItems: 'center',
        gap: spacing.md,
        zIndex: 5
      }}>
        <button 
          onClick={() => navigate(`/scenarios/${scenarioId}`)}
          style={{ background: 'none', border: 'none', cursor: 'pointer', color: colors.primary, padding: 0 }}
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
        </button>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
            <span style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1 }}>
              {lesson.goal}
            </span>
            <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>{currentIndex}/{items.length}</span>
          </div>
          <div style={{ height: 8, backgroundColor: colors.border, borderRadius: 4, overflow: 'hidden' }}>
            <div style={{ height: '100%', backgroundColor: colors.success, width: `${progressFraction * 100}%`, transition: 'width 0.3s ease' }} />
          </div>
        </div>
      </div>

      {/* Content */}
      <div style={{
        flex: 1, 
        overflowY: 'auto', 
        padding: `${spacing.xl}px ${spacing.md}px`,
        display: 'flex', 
        flexDirection: 'column', 
        width: '100%'
      }}>
        <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
          <div style={{ textAlign: 'center', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: spacing.md }}>
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
             <button 
               onClick={() => playAudio()}
               style={{ background: colors.chipBg, border: 'none', borderRadius: 12, width: 32, height: 32, display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer' }}
               title="Replay Audio (Space)"
             >
               🔊
             </button>
          </div>

          <h2 style={{ fontSize: 24, color: colors.primary, fontWeight: 800, textAlign: 'center', margin: 0 }}>
            {currentItem.data?.english ?? '...'}
          </h2>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.md }}>
            {options.map((choice, idx) => (
              <div key={choice} style={{ display: 'flex', gap: spacing.sm, alignItems: 'center' }}>
                <button
                  onClick={() => {
                    if (feedback) return;
                    setSelectedAnswer(choice);
                    submitAnswer(choice);
                  }}
                  className={`card ${selectedAnswer === choice ? 'active' : ''}`}
                  style={{
                    flex: 1,
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
                  <span style={{ 
                    display: 'inline-flex', 
                    alignItems: 'center', 
                    justifyContent: 'center', 
                    width: 24, 
                    height: 24, 
                    borderRadius: 12, 
                    backgroundColor: colors.chipBg, 
                    fontSize: 12, 
                    fontWeight: 800 
                  }}>{idx + 1}</span>
                  {choice}
                </button>
                <button 
                  onClick={(e) => {
                    e.stopPropagation();
                    void Tts.speak(choice);
                  }}
                  style={{ 
                    background: colors.chipBg, 
                    border: 'none', 
                    borderRadius: 12, 
                    width: 44, 
                    height: 44, 
                    display: 'flex', 
                    alignItems: 'center', 
                    justifyContent: 'center', 
                    cursor: 'pointer',
                    fontSize: 20
                  }}
                  title="Listen to choice"
                >
                  🔊
                </button>
              </div>
            ))}
          </div>

          {feedback && (
            <div className="fade-in">
              <FeedbackMessage
                type={feedback.status === 'incorrect' ? 'incorrect' : 'correct'}
                message={feedback.status === 'correct' || feedback.status === 'nearly_correct' ? 'Esatto!' : `Sbagliato. La risposta corretta è: ${feedback.correctAnswer}`}
                explanation={feedback.explanation}
              />
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <div style={{
        padding: spacing.lg,
        paddingBottom: `calc(${spacing.lg}px + env(safe-area-inset-bottom))`,
        backgroundColor: colors.surface,
        borderTop: `2px solid ${colors.border}`,
        width: '100%',
        zIndex: 10
      }}>
        {feedback && (
          <PrimaryButton 
            label="Continue (Enter)" 
            onPress={advance} 
            variant={feedback.status === 'incorrect' ? 'secondary' : 'primary'} 
          />
        )}
      </div>
    </Screen>
  );
};
