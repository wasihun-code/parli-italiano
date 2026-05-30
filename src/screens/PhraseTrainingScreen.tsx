import React, { useEffect, useMemo, useState, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { setupDatabase, loadScenarioHeader, loadScenarioPhrases } from '../lib/db';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { WordChip } from '../components/WordChip';
import { Keyboard } from '../components/Keyboard';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';
import { useUserSettingsStore } from '../store/userSettingsStore';
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
  progressBar,
  progressFill,
  isLearnedByIdOrItalian,
} from '@shared/utils/trainingUi';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';

type FeedbackState = {
  status: AnswerStatus;
  correctAnswer: string;
  explanation?: string;
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
  const addXP = useProgressStore(state => state.addXP);

  const { feedbackLanguage } = useUserSettingsStore();
  const isIt = feedbackLanguage === 'it';

  const [scenarioTitle, setScenarioTitle] = useState(isIt ? 'Frasi' : 'Phrases');
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
    const srsState = useSrsStore.getState();
    return getNextUnlearnedPhrase(
      phrases,
      currentIndex,
      id => {
        const phrase = phrases.find(p => p.id === id);
        if (!phrase) return false;
        return isLearnedByIdOrItalian(phrase, srsState);
      },
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
      void Tts.speak(currentPhrase.italian, currentPhrase.audio);
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

    const isCorrect = status !== 'incorrect';
    if (isCorrect) {
      addXP(10);
    } else {
      addXP(-2);
    }

    recordAnswer(currentPhrase.id, isCorrect);
    if (isCorrect) {
      setPhraseAttemptCounts(current => ({
        ...current,
        [currentPhrase.id]: (current[currentPhrase.id] ?? 0) + 1,
      }));
    }
    setStats(current => recordPhraseAttempt(current, currentPhrase.id, isCorrect));
    
    let explanation: string | undefined;
    if (currentPhrase.feedback) {
      if (status === 'correct' || status === 'nearly_correct') {
        explanation = isIt ? currentPhrase.feedback.correctItalian : currentPhrase.feedback.correctEnglish;
      } else {
        explanation = isIt ? currentPhrase.feedback.incorrectItalian : currentPhrase.feedback.incorrectEnglish;
      }
    } else if (status === 'incorrect') {
      explanation = getWrongAnswerExplanation({
        type: 'phrase',
        italian: currentPhrase.italian,
        correctAnswer: currentExercise.answer
      });
    }

    setFeedback({ status, correctAnswer: currentExercise.answer, explanation });
  }, [currentPhrase, currentExercise, feedback, typedAnswer, selectedWords, selectedAnswer, recordAnswer, addXP, isIt]);

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
            void Tts.speak(ans);
            setSelectedAnswer(ans);
            submitAnswer(ans);
          }
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [feedback, advance, submitAnswer, typedAnswer, selectedWords, selectedAnswer, currentExercise]);

  if (loading) return <Screen style={{ justifyContent: 'center', alignItems: 'center' }}>{isIt ? 'Caricamento frasi...' : 'Loading phrases...'}</Screen>;
  if (loadError) return <Screen><p>{loadError}</p></Screen>;

  if (!activeItem) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          <div style={{ fontSize: 64 }}>🎯</div>
          <h1 style={{ color: colors.primary }}>{isIt ? 'Tutto Imparato!' : 'All Learned!'}</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>{isIt ? 'Hai imparato tutte le frasi per questo scenario.' : "You've mastered all phrases for this scenario."}</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <PrimaryButton label={isIt ? "Vai alle Frasi Complesse" : "Go to Sentences"} onPress={() => navigate(`/scenarios/${scenarioId}/sentences`)} />
            <PrimaryButton label={isIt ? "Torna agli Scenari" : "Back to Scenarios"} onPress={() => navigate('/scenarios')} variant="secondary" />
          </div>
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ padding: 0, backgroundColor: colors.bg }}>
      {/* Immersive Header */}
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
          title="Back"
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
        </button>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
            <span style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1 }}>
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
      </div>

      {/* Main Content Area */}
      <div style={{
        flex: 1, 
        overflowY: 'auto', 
        padding: `${spacing.xl}px ${spacing.md}px`,
        display: 'flex', 
        flexDirection: 'column', 
        width: '100%'
      }}>
        <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
          {feedback ? (
            <div className="fade-in" style={{ textAlign: 'center' }}>
              <FeedbackMessage 
                type={feedback.status === 'correct' || feedback.status === 'nearly_correct' ? 'correct' : 'incorrect'} 
                message={
                  <>
                    <div style={{ fontSize: 24, marginBottom: 8 }}>
                      {feedback.status === 'correct' ? (isIt ? '✅ Ottimo!' : '✅ Excellent!') : feedback.status === 'nearly_correct' ? (isIt ? '⚠️ Quasi corretto!' : '⚠️ Almost correct!') : (isIt ? '❌ Non corretto.' : '❌ Not quite.')}
                    </div>
                    {feedback.status !== 'correct' && (
                      <div style={{ fontSize: 16 }}>
                        {isIt ? 'La risposta corretta è:' : 'The correct answer is:'} <br/>
                        <span style={{ fontSize: 24, textDecoration: 'underline' }}>{feedback.correctAnswer}</span>
                      </div>
                    )}
                    {feedback.explanation && (
                      <div style={{ marginTop: 16, fontSize: 14, fontWeight: 'normal', color: colors.textSecondary }}>
                        {feedback.explanation}
                      </div>
                    )}
                  </>
                } 
              />
            </div>
          ) : (
            <div className="fade-in" key={currentIndex} style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
              <div style={{ marginBottom: spacing.xl, textAlign: 'center' }}>
                 <h2 style={{ color: colors.textSecondary, fontSize: 16, textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 8, fontWeight: 900 }}>
                  {currentExercise?.kind === 'speaking' ? (isIt ? 'Parla a voce alta' : 'Speak aloud') : currentExercise?.kind === 'assembly' ? (isIt ? 'Assembla la frase' : 'Assemble the phrase') : currentExercise?.kind === 'dictation' ? (isIt ? 'Ascolta e scrivi' : 'Listen and write') : (isIt ? 'Traduci' : 'Translate')}
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
                    <div style={{ width: '100%', maxWidth: 400 }}>
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
                        style={{ color: colors.textSecondary, background: 'none', border: 'none', cursor: 'pointer', fontSize: 14, fontWeight: 700, marginTop: spacing.md, width: '100%' }}
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
                  <div style={{ minHeight: 120, padding: spacing.md, borderRadius: 20, border: `2px dashed ${colors.border}`, backgroundColor: 'rgba(78, 52, 46, 0.02)', display: 'flex', flexWrap: 'wrap', alignContent: 'flex-start', gap: 8 }}>
                    {selectedWords.map((word, idx) => (
                      <WordChip key={idx} word={word} onPress={() => {
                        void Tts.speak(word);
                        setSelectedWords(prev => prev.filter((_, i) => i !== idx));
                      }} />
                    ))}
                  </div>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, justifyContent: 'center', padding: spacing.md, backgroundColor: colors.chipBg, borderRadius: 20 }}>
                    {currentExercise.assemblyWords.filter((word: string) => !selectedWords.includes(word) || currentExercise.assemblyWords.filter((w: string) => w === word).length > selectedWords.filter((w: string) => w === word).length).map((word: string, idx: number) => (
                      <WordChip key={idx} word={word} onPress={() => {
                        void Tts.speak(word);
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
                    placeholder={currentExercise.kind === 'fillBlank' ? (isIt ? "Parola mancante..." : "Missing word...") : (isIt ? "Scrivi in italiano..." : "Type in Italian...")}
                    style={{
                      width: '100%',
                      padding: spacing.lg,
                      borderRadius: 20,
                      border: `2px solid ${colors.border}`,
                      fontSize: 22,
                      outline: 'none',
                      backgroundColor: colors.surface,
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
      </div>

      {/* Sticky Footer */}
      <div style={{
        padding: spacing.lg,
        paddingBottom: `calc(${spacing.lg}px + env(safe-area-inset-bottom))`,
        backgroundColor: colors.surface,
        borderTop: `2px solid ${colors.border}`,
        width: '100%',
        zIndex: 10
      }}>
        {!feedback ? (
          <PrimaryButton 
            label={isIt ? "Controlla" : "Check"} 
            onPress={() => submitAnswer()} 
            disabled={(currentExercise?.kind === 'assembly' && selectedWords.length === 0) || (currentExercise?.kind === 'multipleChoice' && !selectedAnswer) || (['fillBlank', 'dictation'].includes(currentExercise?.kind || '') && !typedAnswer.trim())} 
          />
        ) : (
          <PrimaryButton label={isIt ? "Continua" : "Continue"} onPress={advance} variant={feedback.status === 'incorrect' ? 'secondary' : 'primary'} />
        )}
      </div>
    </Screen>
  );
};
