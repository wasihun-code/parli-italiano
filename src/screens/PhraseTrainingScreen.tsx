import React, { useEffect, useMemo, useState, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { setupDatabase, loadScenarioHeader, loadScenarioPhrases } from '../lib/db';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { WordChip } from '../components/WordChip';
import { Keyboard } from '../components/Keyboard';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import {
  buildPhraseExercise,
  calculatePhraseScore,
  completePhrasePhase,
  checkPhraseAnswer,
  recordPhraseAttempt,
  registerPhraseItems,
  getNextUnlearnedPhrase,
  sortPhrasesByDifficulty,
  type PhraseTrainingStats,
  type AnswerStatus,
} from '@shared/utils/phraseTraining';
import type { ScenarioPhraseRow } from '@app/db/vocabularyRepository';
import {
  feedbackCardStyle,
  progressBar,
  progressFill,
} from '@shared/utils/trainingUi';

type FeedbackState = {
  status: AnswerStatus;
  correctAnswer: string;
};

type SpeechRecognitionConstructor = new () => {
  lang: string;
  onstart: (() => void) | null;
  onresult: ((event: { results: ArrayLike<ArrayLike<{ transcript: string }>> }) => void) | null;
  onerror: (() => void) | null;
  onend: (() => void) | null;
  start: () => void;
};

type SpeechWindow = Window & {
  SpeechRecognition?: SpeechRecognitionConstructor;
  webkitSpeechRecognition?: SpeechRecognitionConstructor;
};

const SpeechRecognition =
  (window as SpeechWindow).SpeechRecognition ||
  (window as SpeechWindow).webkitSpeechRecognition;

export const PhraseTrainingScreen: React.FC = () => {
  const { scenarioId } = useParams<{ scenarioId: string }>();
  const navigate = useNavigate();
  const [scenarioTitle, setScenarioTitle] = useState('Scenario Phrases');
  const [phrases, setPhrases] = useState<ScenarioPhraseRow[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [stats, setStats] = useState<PhraseTrainingStats>({});
  const [phraseAttemptCounts, setPhraseAttemptCounts] = useState<Record<string, number>>({});
  const [typedAnswer, setTypedAnswer] = useState('');
  const [selectedWords, setSelectedWords] = useState<string[]>([]);
  const [selectedAnswer, setSelectedAnswer] = useState<string>();
  const [feedback, setFeedback] = useState<FeedbackState>();
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState<string>();
  const [canListen] = useState(true);
  const [canSpeak, setCanSpeak] = useState(true);
  const [isListening, setIsListening] = useState(false);

  const srsItems = useSrsStore(state => state.items);
  const recordAnswer = useSrsStore(state => state.recordAnswer);
  
  const activeItem = useMemo(() => {
    return getNextUnlearnedPhrase(
      phrases,
      currentIndex,
      id => srsItems[id]?.learned ?? false,
    );
  }, [phrases, currentIndex, srsItems]);

  const currentPhrase = activeItem?.phrase;

  const currentExercise = useMemo(() => {
    if (!currentPhrase) return null;
    let ex = buildPhraseExercise(currentPhrase, phrases, phraseAttemptCounts[currentPhrase.id] ?? 0);
    
    // Fallback logic
    if (ex.kind === 'speaking' && (!canSpeak || !SpeechRecognition)) {
      // Switch speaking to assembly or multiple choice
      ex = buildPhraseExercise(currentPhrase, phrases, 1); // 1 is assembly
    }

    return ex;
  }, [currentPhrase, phrases, phraseAttemptCounts, canSpeak]);

  const currentScore = useMemo(() => calculatePhraseScore(stats), [stats]);

  // PROGRESS CALCULATION: Consistent with vocabulary
  const totalSteps = phrases.length * 3;
  const currentSteps = useMemo(() => {
    return phrases.reduce((sum, phrase) => {
      if (srsItems[phrase.id]?.learned) return sum + 3;
      return sum + Math.min(phraseAttemptCounts[phrase.id] ?? 0, 3);
    }, 0);
  }, [phrases, phraseAttemptCounts, srsItems]);

  const progressFraction = Math.max(0, Math.min(1, currentSteps / Math.max(1, totalSteps)));

  useEffect(() => {
    let cancelled = false;

    async function loadPhrases(): Promise<void> {
      try {
        setLoading(true);
        setLoadError(undefined);
        await setupDatabase();
        const [header, scenarioPhrases] = await Promise.all([
          loadScenarioHeader(Number(scenarioId)),
          loadScenarioPhrases(Number(scenarioId)),
        ]);

        if (cancelled) return;

        setScenarioTitle(header?.title ?? `Scenario ${scenarioId}`);
        const srsState = useSrsStore.getState();
        const sortedPhrases = sortPhrasesByDifficulty(scenarioPhrases);
        registerPhraseItems(sortedPhrases, srsState);
        setPhrases(sortedPhrases); // Load all, filter learned in activeItem useMemo
      } catch (error) {
        if (!cancelled) {
          setLoadError(error instanceof Error ? error.message : 'Unable to load phrases.');
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    loadPhrases();
    return () => { cancelled = true; };
  }, [scenarioId]);

  const playAudio = useCallback((): void => {
    if (currentPhrase) {
      Tts.speak(currentPhrase.italian);
    }
  }, [currentPhrase]);

  useEffect(() => {
    if ((currentExercise?.kind === 'dictation' || currentExercise?.kind === 'speaking') && !feedback && canListen) {
      playAudio();
    }
  }, [currentExercise?.kind, feedback, playAudio, canListen]);

  const submitAnswer = useCallback((ans?: string): void => {
    if (!currentPhrase || !currentExercise || feedback) return;

    let submitted = '';
    if (ans) {
      submitted = ans;
    } else if (currentExercise.kind === 'assembly') {
      submitted = selectedWords.join(' ');
    } else if (currentExercise.kind === 'fillBlank') {
      submitted = typedAnswer;
    } else if (currentExercise.kind === 'multipleChoice') {
      submitted = selectedAnswer ?? '';
    } else if (currentExercise.kind === 'dictation') {
      submitted = typedAnswer;
    } else if (currentExercise.kind === 'speaking') {
      submitted = typedAnswer; // If they type instead of speak
    }

    if (!submitted.trim()) return;

    const status = checkPhraseAnswer(submitted, currentExercise.answer);

    recordAnswer(currentPhrase.id, status !== 'incorrect');
    if (status !== 'incorrect') {
      setPhraseAttemptCounts(current => ({
        ...current,
        [currentPhrase.id]: (current[currentPhrase.id] ?? 0) + 1,
      }));
    }
    setStats(current => recordPhraseAttempt(current, currentPhrase.id, status !== 'incorrect'));
    setFeedback({ status, correctAnswer: currentExercise.answer });
  }, [currentPhrase, currentExercise, feedback, typedAnswer, selectedWords, selectedAnswer, recordAnswer]);

  const advance = useCallback((): void => {
    setFeedback(undefined);
    setTypedAnswer('');
    setSelectedWords([]);
    setSelectedAnswer(undefined);

    const nextIndex = currentIndex + 1;
    if (currentSteps >= totalSteps && totalSteps > 0) {
      completePhrasePhase(Number(scenarioId), stats, useProgressStore.getState());
    }

    setCurrentIndex(nextIndex);
  }, [currentIndex, currentSteps, totalSteps, scenarioId, stats]);

  const startSpeechRecognition = () => {
    if (!SpeechRecognition || isListening) return;
    
    const recognition = new SpeechRecognition();
    recognition.lang = 'it-IT';
    recognition.onstart = () => setIsListening(true);
    recognition.onresult = (event: { results: ArrayLike<ArrayLike<{ transcript: string }>> }) => {
      const transcript = event.results[0][0].transcript;
      submitAnswer(transcript);
    };
    recognition.onerror = () => setIsListening(false);
    recognition.onend = () => setIsListening(false);
    recognition.start();
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (feedback) {
        if (e.key === 'Enter') advance();
        return;
      }

      if (e.key === 'Enter') {
        if (currentExercise?.kind === 'multipleChoice' && selectedAnswer) submitAnswer();
        else if (typedAnswer.trim() || selectedWords.length > 0) submitAnswer();
      }

      if (currentExercise?.kind === 'multipleChoice' && !feedback) {
        if (e.key >= '1' && e.key <= '4') {
          const idx = parseInt(e.key) - 1;
          if (currentExercise.options[idx]) {
            const ans = currentExercise.options[idx];
            Tts.speak(ans);
            setSelectedAnswer(ans);
            submitAnswer(ans);
          }
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [feedback, advance, submitAnswer, typedAnswer, selectedWords, selectedAnswer, currentExercise]);

  if (loading) return <Screen style={{ justifyContent: 'center', alignItems: 'center' }}>Loading phrases...</Screen>;
  if (loadError) return <Screen><p>{loadError}</p></Screen>;

  if (!activeItem) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          <div style={{ fontSize: 64 }}>🎯</div>
          <h1 style={{ color: colors.primary }}>All Learned!</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>You've mastered all phrases for this scenario.</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <PrimaryButton label="Go to Sentences" onPress={() => navigate(`/scenarios/${scenarioId}/sentences`)} />
            <PrimaryButton label="Back to Scenarios" onPress={() => navigate('/scenarios')} variant="secondary" />
          </div>
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', marginBottom: spacing.lg, alignItems: 'center' }}>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
            <span data-testid="scenario-title" style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1 }}>
              {scenarioTitle}
            </span>
            <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>
              Score: {currentScore}% | {Math.round(progressFraction * 100)}%
            </span>
          </div>
          <div style={{ ...progressBar(), overflow: 'visible' }}>
            <div style={progressFill(progressFraction)} />
          </div>
        </div>
      </header>

      <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
        {feedback ? (
          <div className={feedback.status === 'correct' ? 'bounce' : 'shake'} style={feedbackCardStyle(feedback.status)}>
            <div style={{ fontSize: 48, marginBottom: 12 }}>
              {feedback.status === 'correct' ? '✅' : feedback.status === 'nearly_correct' ? '⚠️' : '❌'}
            </div>
            <div>
              {feedback.status === 'correct' && 'Excellent!'}
              {feedback.status === 'nearly_correct' && 'Almost correct!'}
              {feedback.status === 'incorrect' && 'Not quite.'}
            </div>
            {(feedback.status !== 'correct') && (
              <div style={{ marginTop: 12, fontSize: 16, opacity: 0.9 }}>
                The correct answer is: <br/>
                <span style={{ fontSize: 24, textDecoration: 'underline' }}>{feedback.correctAnswer}</span>
              </div>
            )}
          </div>
        ) : (
          <div className="fade-in" key={currentIndex}>
            <div style={{ marginBottom: spacing.xl }}>
               <h2 style={{ color: colors.textSecondary, fontSize: 16, textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 8, fontWeight: 900 }}>
                {currentExercise?.kind === 'speaking' ? 'Speak aloud' : currentExercise?.kind === 'assembly' ? 'Assemble the phrase' : currentExercise?.kind === 'dictation' ? 'Listen and write' : 'Translate'}
              </h2>
              <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>
                {currentExercise?.prompt}
              </h1>
            </div>

            {(currentExercise?.kind === 'dictation' || currentExercise?.kind === 'speaking') && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg, alignItems: 'center', marginBottom: spacing.xl }}>
                <button 
                  onClick={playAudio}
                  className="card active"
                  style={{ 
                    width: 100, 
                    height: 100, 
                    borderRadius: 50, 
                    display: 'flex', 
                    alignItems: 'center', 
                    justifyContent: 'center',
                    borderWidth: 3,
                    boxShadow: `0 8px 0 rgba(78, 52, 46, 0.1)`
                  }}
                >
                  <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                    <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
                    <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
                  </svg>
                </button>
                
                {currentExercise.kind === 'speaking' && (
                  <div style={{ width: '100%', maxWidth: 300 }}>
                    <PrimaryButton
                      label={isListening ? 'Listening...' : 'Tap to Speak'}
                      onPress={startSpeechRecognition}
                      disabled={isListening}
                      variant="accent"
                      icon={
                         <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                          <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/>
                        </svg>
                      }
                    />
                    <button
                      onClick={() => setCanSpeak(false)}
                      style={{ 
                        color: colors.textSecondary, 
                        background: 'none', 
                        border: 'none', 
                        cursor: 'pointer', 
                        fontSize: 14, 
                        fontWeight: 700,
                        marginTop: spacing.md,
                        width: '100%'
                      }}
                    >
                      I can't speak now
                    </button>
                  </div>
                )}
              </div>
            )}

            {currentExercise?.kind === 'multipleChoice' && (
               <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.md }}>
                {currentExercise.options.map((choice, idx) => (
                  <button
                    key={choice}
                    onClick={() => {
                      Tts.speak(choice);
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
                      borderBottomWidth: selectedAnswer === choice ? 2 : 4,
                      transform: selectedAnswer === choice ? 'translateY(2px)' : 'translateY(0)',
                    }}
                  >
                    <div style={{ 
                      width: 32, 
                      height: 32, 
                      borderRadius: 16, 
                      backgroundColor: selectedAnswer === choice ? colors.primary : colors.chipBg,
                      color: selectedAnswer === choice ? colors.onPrimary : colors.textSecondary,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: 14,
                      fontWeight: 900,
                      border: `1px solid ${colors.border}`
                    }}>
                      {idx + 1}
                    </div>
                    {choice}
                  </button>
                ))}
              </div>
            )}

            {currentExercise?.kind === 'assembly' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
                <div style={{
                  minHeight: 120,
                  padding: spacing.md,
                  borderRadius: 20,
                  border: `2px dashed ${colors.border}`,
                  backgroundColor: 'rgba(78, 52, 46, 0.02)',
                  display: 'flex',
                  flexWrap: 'wrap',
                  alignContent: 'flex-start',
                  gap: 8
                }}>
                  {selectedWords.map((word, idx) => (
                    <WordChip key={idx} word={word} onPress={() => {
                      Tts.speak(word);
                      setSelectedWords(prev => prev.filter((_, i) => i !== idx));
                    }} />
                  ))}
                </div>
                <div style={{ 
                  display: 'flex', 
                  flexWrap: 'wrap', 
                  gap: 8, 
                  justifyContent: 'center',
                  padding: spacing.md,
                  backgroundColor: colors.chipBg,
                  borderRadius: 20
                }}>
                  {currentExercise.assemblyWords.filter((word: string) => !selectedWords.includes(word) || currentExercise.assemblyWords.filter((w: string) => w === word).length > selectedWords.filter((w: string) => w === word).length).map((word: string, idx: number) => (
                    <WordChip key={idx} word={word} onPress={() => {
                      Tts.speak(word);
                      setSelectedWords(prev => [...prev, word]);
                    }} />
                  ))}
                </div>
              </div>
            )}

            {(currentExercise?.kind === 'fillBlank' || currentExercise?.kind === 'dictation' || (currentExercise?.kind === 'speaking' && !isListening)) && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
                {currentExercise.kind === 'fillBlank' && (
                  <p style={{ fontSize: 24, color: colors.primary, fontWeight: 700, textAlign: 'center' }}>{currentExercise.displayItalian}</p>
                )}
                <input
                  autoFocus
                  type="text"
                  value={typedAnswer}
                  onChange={e => setTypedAnswer(e.target.value)}
                  placeholder={currentExercise.kind === 'fillBlank' ? "Missing word..." : "Type in Italian..."}
                  style={{
                    width: '100%',
                    padding: spacing.lg,
                    borderRadius: 20,
                    border: `2px solid ${colors.border}`,
                    fontSize: 22,
                    outline: 'none',
                    backgroundColor: colors.bg,
                    textAlign: 'center',
                    fontWeight: 700,
                    color: colors.primary
                  }}
                />
                <Keyboard onKeyPress={char => setTypedAnswer(prev => prev + char)} />
              </div>
            )}
          </div>
        )}
      </div>

      <div style={{
        position: 'fixed',
        bottom: 0,
        left: 0,
        right: 0,
        padding: spacing.lg,
        paddingBottom: `calc(${spacing.lg}px + env(safe-area-inset-bottom))`,
        backgroundColor: colors.surface,
        borderTop: `2px solid ${colors.border}`,
        maxWidth: 900,
        margin: '0 auto',
        zIndex: 10
      }}>
        {!feedback ? (
          <PrimaryButton 
            label="Check" 
            onPress={() => submitAnswer()} 
            disabled={(currentExercise?.kind === 'assembly' && selectedWords.length === 0) || (currentExercise?.kind === 'multipleChoice' && !selectedAnswer) || (['fillBlank', 'dictation'].includes(currentExercise?.kind || '') && !typedAnswer.trim())} 
          />
        ) : (
          <PrimaryButton label="Continue" onPress={advance} variant={feedback.status === 'incorrect' ? 'secondary' : 'primary'} />
        )}
      </div>
    </Screen>
  );
};
