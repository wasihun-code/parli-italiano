import React, { useEffect, useMemo, useState, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { setupDatabase, loadScenarioHeader, loadScenarioVocabulary } from '../lib/db';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { Keyboard } from '../components/Keyboard';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import {
  buildVocabularyExercise,
  getNextUnlearnedTerm,
  maybeCompleteVocabularyPhase,
  checkVocabularyAnswer,
  registerVocabularyTerms,
  type AnswerStatus,
} from '@shared/utils/vocabularyTraining';
import type { ScenarioVocabularyRow } from '@app/db/vocabularyRepository';
import {
  feedbackCardStyle,
  isLearnedByIdOrItalian,
  masterSrsItems,
  progressBar,
  progressFill,
  shuffle,
} from '@shared/utils/trainingUi';

type FeedbackState = {
  status: AnswerStatus;
  correctAnswer: string;
};

export const VocabularyTrainingScreen: React.FC = () => {
  const { scenarioId } = useParams<{ scenarioId: string }>();
  const navigate = useNavigate();
  const [scenarioTitle, setScenarioTitle] = useState('Scenario Vocabulary');
  const [terms, setTerms] = useState<ScenarioVocabularyRow[]>([]);
  const [allTerms, setAllTerms] = useState<ScenarioVocabularyRow[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [termAttemptCounts, setTermAttemptCounts] = useState<Record<string, number>>({});
  const [selectedAnswer, setSelectedAnswer] = useState<string>();
  const [typedAnswer, setTypedAnswer] = useState('');
  const [feedback, setFeedback] = useState<FeedbackState>();
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState<string>();
  const [canListen, setCanListen] = useState(true);

  const srsItems = useSrsStore(state => state.items);
  const recordAnswer = useSrsStore(state => state.recordAnswer);

  const [isSkipTest, setIsSkipTest] = useState(false);
  const [skipTestScore, setSkipTestScore] = useState(0);

  const testTerms = useMemo(() => {
    if (terms.length === 0) return [];
    return shuffle(terms).slice(0, 10);
  }, [terms]);

  const startSkipTest = useCallback(() => {
    setIsSkipTest(true);
    setSkipTestScore(0);
    setCurrentIndex(0);
    setFeedback(undefined);
    setTypedAnswer('');
    setSelectedAnswer(undefined);
  }, []);

  const activeTerm = useMemo(() => {
    if (isSkipTest) {
      if (currentIndex < testTerms.length) {
        return { term: testTerms[currentIndex], index: currentIndex };
      }
      return null;
    }
    return getNextUnlearnedTerm(
      terms,
      currentIndex,
      id => srsItems[id]?.learned ?? false,
    );
  }, [isSkipTest, currentIndex, testTerms, terms, srsItems]);
  
  const exercise = useMemo(() => {
    if (!activeTerm) return null;
    if (isSkipTest) {
      return buildVocabularyExercise(activeTerm.term, terms, 0); // 0 is flashcard
    }
    let ex = buildVocabularyExercise(
      activeTerm.term,
      terms,
      termAttemptCounts[activeTerm.term.id] ?? 0,
    );
    if (!canListen && ex.kind === 'listening') {
      ex = buildVocabularyExercise(activeTerm.term, terms, 0); // 0 is flashcard
    }
    return ex;
  }, [activeTerm, terms, termAttemptCounts, canListen, isSkipTest]);

  // PROGRESS CALCULATION FIX: Based on total steps (3 per term)
  const totalSteps = terms.length * 3;
  const currentSteps = useMemo(() => {
    if (isSkipTest) return currentIndex;
    return terms.reduce((sum, term) => {
      // If the term is marked as learned in SRS, it contributes 3 steps
      if (srsItems[term.id]?.learned) return sum + 3;
      // Otherwise use the local session attempt count (max 3)
      return sum + Math.min(termAttemptCounts[term.id] ?? 0, 3);
    }, 0);
  }, [terms, termAttemptCounts, srsItems, isSkipTest, currentIndex]);

  const progressFraction = Math.max(0, Math.min(1, currentSteps / Math.max(1, totalSteps)));

  useEffect(() => {
    let cancelled = false;

    async function loadVocabulary(): Promise<void> {
      try {
        setLoading(true);
        setLoadError(undefined);
        await setupDatabase();
        const [header, vocabulary] = await Promise.all([
          loadScenarioHeader(Number(scenarioId)),
          loadScenarioVocabulary(Number(scenarioId)),
        ]);

        if (cancelled) return;

        setScenarioTitle(header?.title ?? `Scenario ${scenarioId}`);
        const srsState = useSrsStore.getState();
        registerVocabularyTerms(vocabulary, srsState);
        const unlearnedVocabulary = vocabulary.filter(v => !isLearnedByIdOrItalian(v, srsState));
        setAllTerms(vocabulary);
        setTerms(unlearnedVocabulary);
      } catch (error) {
        if (!cancelled) {
          setLoadError(error instanceof Error ? error.message : 'Unable to load vocabulary.');
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    loadVocabulary();
    return () => { cancelled = true; };
  }, [scenarioId]);

  useEffect(() => {
    if (terms.length === 0) return;

    maybeCompleteVocabularyPhase(
      Number(scenarioId),
      terms,
      useSrsStore.getState(),
      useProgressStore.getState(),
    );
  }, [srsItems, scenarioId, terms]);

  const playAudio = useCallback((): void => {
    if (activeTerm) {
      Tts.speak(activeTerm.term.italian);
    }
  }, [activeTerm]);

  useEffect(() => {
    if (exercise?.kind === 'listening' && !feedback && canListen) {
      playAudio();
    }
  }, [exercise, feedback, playAudio, canListen]);

  const submitAnswer = useCallback((ans?: string): void => {
    if (!activeTerm || !exercise || feedback) return;

    const submitted = ans ?? (exercise.kind === 'spelling' ? typedAnswer : selectedAnswer ?? '');
    if (!submitted.trim() && exercise.kind === 'spelling') return;

    const status = checkVocabularyAnswer(submitted, exercise.answer);
    
    if (isSkipTest) {
      if (status !== 'incorrect') {
        setSkipTestScore(prev => prev + 1);
      }
      setFeedback({ status, correctAnswer: exercise.answer });
      return;
    }

    recordAnswer(activeTerm.term.id, status !== 'incorrect');
    setTermAttemptCounts(current => ({
      ...current,
      [activeTerm.term.id]: (current[activeTerm.term.id] ?? 0) + (status !== 'incorrect' ? 1 : 0),
    }));
    setFeedback({ status, correctAnswer: exercise.answer });
  }, [activeTerm, exercise, feedback, typedAnswer, selectedAnswer, recordAnswer, isSkipTest]);

  const advance = useCallback((): void => {
    const nextIndex = currentIndex + 1;

    if (isSkipTest && nextIndex >= testTerms.length && testTerms.length > 0) {
      const passed = (skipTestScore / testTerms.length) >= 0.9;
      if (passed) {
        useProgressStore.getState().setScenarioVocabularyCompleted(Number(scenarioId), true);
        useProgressStore.getState().setScenarioPhraseScore(Number(scenarioId), 100);
        useProgressStore.getState().setScenarioSentenceScore(Number(scenarioId), 100);
        masterSrsItems(
          allTerms.map(term => ({
            id: term.id,
            type: 'vocabulary' as const,
            italian: term.italian,
            english: term.english,
          })),
          useSrsStore.getState(),
        );
      }
    }

    setFeedback(undefined);
    setTypedAnswer('');
    setSelectedAnswer(undefined);
    setCurrentIndex(nextIndex);
  }, [currentIndex, isSkipTest, testTerms, skipTestScore, scenarioId, allTerms]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (feedback) {
        if (e.key === 'Enter') advance();
        return;
      }

      if (e.key === 'Enter' && (typedAnswer.trim() || selectedAnswer)) {
        submitAnswer();
      }

      if (exercise?.kind !== 'spelling' && !feedback) {
        if (e.key >= '1' && e.key <= '4') {
          const idx = parseInt(e.key) - 1;
          if (exercise?.options[idx]) {
            const ans = exercise.options[idx];
            Tts.speak(ans);
            setSelectedAnswer(ans);
            submitAnswer(ans);
          }
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [feedback, advance, submitAnswer, typedAnswer, selectedAnswer, exercise]);

  if (isSkipTest) {
    if (currentIndex >= testTerms.length && testTerms.length > 0) {
      const passed = (skipTestScore / testTerms.length) >= 0.9;
      return (
        <Screen style={{ justifyContent: 'center' }}>
          <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
            <h1 style={{ color: colors.primary }}>Test Results</h1>
            <div style={{ fontSize: 72, fontWeight: 900, color: passed ? colors.success : colors.error }}>{Math.round((skipTestScore / testTerms.length) * 100)}%</div>
            <p style={{ color: colors.textSecondary, fontSize: 18 }}>{passed ? 'Phase passed! You are ready for conversation.' : 'Not enough to skip. Keep practicing!'}</p>
            <PrimaryButton label="Continue" onPress={() => passed ? navigate(`/scenarios/${scenarioId}/conversation`) : setIsSkipTest(false)} variant={passed ? 'primary' : 'secondary'} />
          </div>
        </Screen>
      );
    }
  }

  if (loading) return <Screen style={{ justifyContent: 'center', alignItems: 'center' }}><div className="fade-in">☕ Loading vocabulary...</div></Screen>;
  if (loadError) return <Screen><p>{loadError}</p></Screen>;

  if (!activeTerm) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
          <div style={{ fontSize: 64 }}>🎯</div>
          <h1 style={{ color: colors.primary }}>All Learned!</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>You've mastered all vocabulary for this scenario.</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            <PrimaryButton label="Go to Phrases" onPress={() => navigate(`/scenarios/${scenarioId}/phrases`)} />
            <PrimaryButton label="Back to Scenarios" onPress={() => navigate('/scenarios')} variant="secondary" />
          </div>
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
              {isSkipTest ? `Skip Test: ${currentIndex + 1} / ${testTerms.length}` : scenarioTitle}
            </span>
            <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>
              {Math.round(progressFraction * 100)}%
            </span>
          </div>
          <div style={{ ...progressBar(), overflow: 'visible' }}>
            <div style={progressFill(progressFraction)} />
          </div>
        </div>
        {!isSkipTest && (
          <button 
            onClick={startSkipTest}
            style={{ 
              color: colors.primary, 
              background: 'none', 
              border: 'none', 
              cursor: 'pointer', 
              fontWeight: 800, 
              fontSize: 12,
              marginLeft: spacing.md,
              textDecoration: 'underline'
            }}
          >
            SKIP
          </button>
        )}
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
                {exercise?.kind === 'listening' ? 'Listen and translate' : exercise?.kind === 'spelling' ? 'Write in Italian' : 'Translate'}
              </h2>
              <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{exercise?.prompt}</h1>
            </div>

            {(exercise?.kind === 'listening' || exercise?.kind === 'flashcard') && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md, alignItems: 'center', marginBottom: spacing.xl }}>
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
                {exercise?.kind === 'listening' && (
                  <button
                    onClick={() => setCanListen(false)}
                    style={{ color: colors.textSecondary, background: 'none', border: 'none', cursor: 'pointer', fontSize: 14, fontWeight: 700 }}
                  >
                    I can't listen now
                  </button>
                )}
              </div>
            )}

            {exercise?.kind === 'spelling' ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
                <input
                  autoFocus
                  type="text"
                  value={typedAnswer}
                  onChange={e => setTypedAnswer(e.target.value)}
                  placeholder="Type here..."
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
            ) : (
              <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.md }}>
                {exercise?.options.map((choice, idx) => (
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
          exercise?.kind === 'spelling' ? (
            <PrimaryButton label="Check" onPress={() => submitAnswer()} disabled={!typedAnswer.trim()} />
          ) : (
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, fontWeight: 700, margin: 0 }}>
              Choose the correct answer
            </p>
          )
        ) : (
          <PrimaryButton label="Continue" onPress={advance} variant={feedback.status === 'incorrect' ? 'secondary' : 'primary'} />
        )}
      </div>
    </Screen>
  );
};
