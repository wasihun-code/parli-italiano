import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { setupDatabase, loadScenarioHeader, loadScenarioSentences } from '../lib/db';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { Keyboard } from '../components/Keyboard';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import {
  buildSentenceExercise,
  calculateSentenceScore,
  checkSentenceAnswer,
  completeSentencePhase,
  hasPracticedAllSentenceExercises,
  recordSentenceAttempt,
  registerSentenceItems,
  sortSentencesByDifficulty,
  type SentenceTrainingStats,
  type AnswerStatus,
} from '@shared/utils/sentenceTraining';
import type { ScenarioSentenceRow } from '@app/db/vocabularyRepository';
import {
  isLearnedByIdOrItalian,
  progressBar,
  progressFill,
} from '@shared/utils/trainingUi';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';

type FeedbackState = {
  status: AnswerStatus;
  correctAnswer: string;
  explanation?: string;
};

export const SentenceTrainingScreen: React.FC = () => {
  const { scenarioId } = useParams<{ scenarioId: string }>();
  const navigate = useNavigate();
  const addXP = useProgressStore(state => state.addXP);
  const { feedbackLanguage } = useUserSettingsStore();
  const isIt = feedbackLanguage === 'it';

  const [scenarioTitle, setScenarioTitle] = useState(isIt ? 'Frasi Complesse' : 'Complex Sentences');
  const [sentences, setSentences] = useState<ScenarioSentenceRow[]>([]);

  const [exerciseIndex, setExerciseIndex] = useState(0);
  const [stats, setStats] = useState<SentenceTrainingStats>({});
  const [typedAnswer, setTypedAnswer] = useState('');
  const [feedback, setFeedback] = useState<FeedbackState>();
  const [finishedScore, setFinishedScore] = useState<number>();
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState<string>();

  const recordAnswer = useSrsStore(state => state.recordAnswer);
  
  const currentSentence = sentences[exerciseIndex % Math.max(sentences.length, 1)];
  const currentExercise = currentSentence
    ? buildSentenceExercise(currentSentence, exerciseIndex)
    : null;
  const currentScore = useMemo(() => calculateSentenceScore(stats), [stats]);

  useEffect(() => {
    let cancelled = false;

    async function loadSentences(): Promise<void> {
      try {
        setLoading(true);
        setLoadError(undefined);
        await setupDatabase();
        const [header, scenarioSentences] = await Promise.all([
          loadScenarioHeader(Number(scenarioId)),
          loadScenarioSentences(Number(scenarioId)),
        ]);

        if (cancelled) return;

        setScenarioTitle(header?.title ?? `Scenario ${scenarioId}`);
        const srsState = useSrsStore.getState();
        const sortedSentences = sortSentencesByDifficulty(scenarioSentences);
        registerSentenceItems(sortedSentences, srsState);
        setSentences(sortedSentences.filter(sentence => !isLearnedByIdOrItalian(sentence, srsState)));
      } catch (error) {
        if (!cancelled) {
          setLoadError(error instanceof Error ? error.message : 'Unable to load sentences.');
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    loadSentences();
    return () => { cancelled = true; };
  }, [scenarioId]);

  const canSubmit = typedAnswer.trim().length > 0;

  const playAudio = useCallback((): void => {
    if (currentSentence) {
      Tts.speak(currentSentence.italian);
    }
  }, [currentSentence]);

  useEffect(() => {
    if (currentExercise?.kind === 'dictation' && !feedback) {
      playAudio();
    }
  }, [exerciseIndex, feedback, currentExercise?.kind]); // Fix: removed playAudio from deps

  const submitAnswer = useCallback((): void => {
    if (!currentSentence || !currentExercise || feedback) return;

    const status = checkSentenceAnswer(typedAnswer, currentExercise.answer);
    const isCorrect = status !== 'incorrect';

    if (isCorrect) {
      addXP(10);
    } else {
      addXP(-2);
    }

    recordAnswer(currentSentence.id, isCorrect);
    setStats(current => recordSentenceAttempt(current, currentSentence.id, isCorrect));
    const explanation = !isCorrect ? getWrongAnswerExplanation({
      type: 'sentence',
      italian: currentSentence.italian,
      correctAnswer: currentExercise.answer
    }) : undefined;

    setFeedback({ status, correctAnswer: currentExercise.answer, explanation });
  }, [currentExercise, currentSentence, feedback, recordAnswer, typedAnswer, addXP]);

  const advance = useCallback((): void => {
    setFeedback(undefined);
    setTypedAnswer('');

    const nextIndex = exerciseIndex + 1;
    if (hasPracticedAllSentenceExercises(sentences, nextIndex)) {
      const finalScore = calculateSentenceScore(stats);
      setFinishedScore(finalScore);
      completeSentencePhase(Number(scenarioId), stats, useProgressStore.getState());
      return;
    }

    setExerciseIndex(nextIndex);
  }, [exerciseIndex, scenarioId, sentences, stats]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (feedback) {
        if (e.key === 'Enter') advance();
        return;
      }
      if (e.key === 'Enter' && canSubmit) {
        submitAnswer();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [advance, canSubmit, feedback, submitAnswer]);

  if (loading) return <Screen style={{ justifyContent: 'center', alignItems: 'center' }}>{isIt ? 'Caricamento frasi...' : 'Loading sentences...'}</Screen>;
  if (loadError) return <Screen><p>{loadError}</p></Screen>;

  if (sentences.length === 0) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          <div style={{ fontSize: 64 }}>🎯</div>
          <h1 style={{ color: colors.primary }}>{isIt ? 'Tutto Imparato!' : 'All Learned!'}</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>{isIt ? 'Hai imparato tutte le frasi complesse per questo scenario.' : "You've mastered all sentences for this scenario."}</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <PrimaryButton label={isIt ? "Inizia Conversazione" : "Start Conversation"} onPress={() => navigate(`/scenarios/${scenarioId}/conversation`)} />
            <PrimaryButton label={isIt ? "Torna agli Scenari" : "Back to Scenarios"} onPress={() => navigate('/scenarios')} variant="secondary" />
          </div>
        </div>
      </Screen>
    );
  }


  if (finishedScore !== undefined) {
    const passed = finishedScore >= 80;
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          <h1 style={{ color: colors.primary }}>{isIt ? 'Fase Completata' : 'Phase Complete'}</h1>

          <div style={{ fontSize: 72, fontWeight: 900, color: passed ? colors.success : colors.error }}>{finishedScore}%</div>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>{passed ? 'Ottimo lavoro! Hai superato la fase delle frasi.' : 'Ci sei quasi! Riprova per raggiungere l\'80%.'}</p>
          <PrimaryButton label={passed ? 'Inizia Conversazione' : 'Riprova'} onPress={() => {
            if (passed) {
              navigate(`/scenarios/${scenarioId}/conversation`);
            } else {
              setExerciseIndex(0);
              setStats({});
              setFinishedScore(undefined);
            }
          }} />
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: spacing.lg }}>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
            <span data-testid="scenario-title" style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1 }}>
              {scenarioTitle}
            </span>
            <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>
              {isIt ? 'Punteggio' : 'Score'}: {currentScore}%
            </span>
          </div>
          <div style={progressBar()}>
            <div style={progressFill((exerciseIndex + 1) / Math.max(sentences.length * 3, 1))} />
          </div>
        </div>
      </header>

      <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
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
          <div className="fade-in" key={exerciseIndex}>
            <div style={{ marginBottom: spacing.xl }}>
               <h2 style={{ color: colors.textSecondary, fontSize: 16, textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 8, fontWeight: 900 }}>
                {currentExercise?.kind === 'dictation' ? (isIt ? 'Ascolta e scrivi' : 'Listen and write') : currentExercise?.kind === 'completion' ? (isIt ? 'Completa la frase' : 'Complete the sentence') : (isIt ? 'Traduci' : 'Translate')}
              </h2>
              <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{currentExercise?.prompt}</h1>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg, alignItems: 'center', marginBottom: spacing.xl }}>
               <button 
                  onClick={playAudio}
                  className="card active"
                  style={{ 
                    width: 80, 
                    height: 80, 
                    borderRadius: 40, 
                    display: 'flex', 
                    alignItems: 'center', 
                    justifyContent: 'center',
                    borderWidth: 3,
                    boxShadow: `0 6px 0 rgba(78, 52, 46, 0.1)`
                  }}
                >
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
                    <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
                    <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
                  </svg>
                </button>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
              <div className="card" style={{ padding: spacing.md, backgroundColor: colors.chipBg, borderColor: 'transparent', textAlign: 'center', cursor: 'default' }}>
                <span style={{ color: colors.textSecondary, fontSize: 12, fontWeight: 900, textTransform: 'uppercase', display: 'block', marginBottom: 4 }}>Grammar</span>
                <span style={{ color: colors.primary, fontWeight: 700 }}>{currentSentence?.grammarPoint}</span>
              </div>

              {currentExercise?.kind === 'completion' && (
                <p style={{ fontSize: 22, color: colors.primary, textAlign: 'center', margin: '8px 0', fontWeight: 700 }}>
                  {currentExercise.displayItalian}
                </p>
              )}

              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
                <input
                  autoFocus
                  type="text"
                  value={typedAnswer}
                  onChange={e => setTypedAnswer(e.target.value)}
                  placeholder={currentExercise?.kind === 'completion' ? (isIt ? "Scrivi la parola..." : "Type the word...") : (isIt ? "Scrivi la frase in italiano..." : "Type the Italian sentence...")}
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
            </div>
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
          <PrimaryButton label={isIt ? "Controlla" : "Check"} onPress={submitAnswer} disabled={!canSubmit} />
        ) : (
          <PrimaryButton label={isIt ? "Continua" : "Continue"} onPress={advance} variant={feedback.status === 'incorrect' ? 'secondary' : 'primary'} />
        )}
      </div>
    </Screen>
  );
};
