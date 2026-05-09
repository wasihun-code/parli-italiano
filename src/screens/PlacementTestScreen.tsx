import React, { useMemo, useState, useCallback, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { Keyboard } from '../components/Keyboard';
import { Tts } from '../lib/tts';
import { foundationLessons } from '@shared/data/foundations';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { normalizeString, levenshteinDistance } from '@shared/utils/string';
import {
  buildShuffledOptions,
  feedbackCardStyle,
  masterSrsItems,
  progressBar,
  progressFill,
  shuffle,
} from '@shared/utils/trainingUi';

type PlacementExercise = {
  id: string;
  kind: 'flashcard' | 'multipleChoice' | 'fillBlank';
  lessonId: number;
  prompt: string;
  answer: string;
  options?: string[];
};

type FeedbackState = {
  status: 'correct' | 'nearly_correct' | 'incorrect';
  answer: string;
};

export const PlacementTestScreen: React.FC = () => {
  const navigate = useNavigate();
  const recordFoundationScore = useProgressStore(state => state.recordFoundationScore);
  const recordSrsAnswer = useSrsStore(state => state.recordAnswer);

  const [exerciseIndex, setExerciseIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [typedAnswer, setTypedAnswer] = useState('');
  const [selectedAnswer, setSelectedAnswer] = useState<string>();
  const [feedback, setFeedback] = useState<FeedbackState>();
  const [finished, setFinished] = useState(false);

  const testExercises = useMemo<PlacementExercise[]>(() => {
    const allTerms = foundationLessons.flatMap(lesson => lesson.terms);
    const allExercises = foundationLessons.flatMap(lesson =>
      lesson.exercises
        .flatMap(exercise => {
          if (exercise.kind === 'listening') {
            return [];
          }

          const kind: PlacementExercise['kind'] =
            exercise.kind === 'flashcard' ? 'multipleChoice' : exercise.kind;
          return [{
            ...exercise,
            kind,
            lessonId: lesson.id,
            options:
              exercise.kind === 'fillBlank'
                ? undefined
                : buildShuffledOptions(
                    exercise.answer,
                    allTerms.map(term => term.italian),
                  ),
          }];
        }),
    );
    return shuffle(allExercises).slice(0, 20);
  }, []);

  const currentExercise = testExercises[exerciseIndex];

  const submitAnswer = useCallback((ans?: string) => {
    if (!currentExercise || feedback) return;
    const submitted = ans ?? (currentExercise.kind === 'fillBlank' ? typedAnswer : selectedAnswer ?? '');
    if (!submitted.trim()) return;

    const normSubmitted = normalizeString(submitted);
    const normExpected = normalizeString(currentExercise.answer);
    const isCorrect =
      normSubmitted === normExpected ||
      normSubmitted.endsWith(` ${normExpected}`);
    const isNearly = !isCorrect && normExpected.length >= 3 && levenshteinDistance(normSubmitted, normExpected) === 1;

    const accepted = isCorrect || isNearly;
    setFeedback({ status: isCorrect ? 'correct' : (isNearly ? 'nearly_correct' : 'incorrect'), answer: currentExercise.answer });

    if (accepted) {
      setCorrectCount(c => c + 1);
    }

    const lesson = foundationLessons.find(l => l.id === currentExercise.lessonId);
    const matchingTerm = lesson?.terms.find(t => normalizeString(t.italian) === normExpected);
    if (matchingTerm) {
      useSrsStore.getState().registerItem({
        id: matchingTerm.id,
        type: 'foundation',
        italian: matchingTerm.italian,
        english: matchingTerm.english,
      });
      recordSrsAnswer(matchingTerm.id, accepted);
    }
  }, [currentExercise, feedback, typedAnswer, selectedAnswer, recordSrsAnswer]);

  const advance = useCallback(() => {
    if (exerciseIndex + 1 >= testExercises.length) {
      const score = Math.round((correctCount / testExercises.length) * 100);
      if (score >= 90) {
        foundationLessons.forEach(l => recordFoundationScore(l.id, 100));
        masterSrsItems(
          foundationLessons.flatMap(lesson =>
            lesson.terms.map(term => ({
              id: term.id,
              type: 'foundation' as const,
              italian: term.italian,
              english: term.english,
            })),
          ),
          useSrsStore.getState(),
        );
      }
      setFinished(true);
      return;
    }
    setExerciseIndex(i => i + 1);
    setTypedAnswer('');
    setSelectedAnswer(undefined);
    setFeedback(undefined);
  }, [exerciseIndex, testExercises.length, correctCount, recordFoundationScore]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (feedback) {
        if (e.key === 'Enter') advance();
        return;
      }
      if (e.key === 'Enter' && (typedAnswer.trim() || selectedAnswer)) submitAnswer();
      if (currentExercise?.kind !== 'fillBlank' && e.key >= '1' && e.key <= '4') {
        const choice = currentExercise.options?.[Number(e.key) - 1];
        if (choice) {
          Tts.speak(choice);
          setSelectedAnswer(choice);
          submitAnswer(choice);
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [feedback, advance, submitAnswer, typedAnswer, selectedAnswer, currentExercise?.kind, currentExercise?.options]);

  if (finished) {
    const score = Math.round((correctCount / testExercises.length) * 100);
    const passed = score >= 90;
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: spacing.lg, padding: spacing.xl, cursor: 'default' }}>
          <h1 style={{ color: colors.primary, fontSize: 32 }}>Test Results</h1>
          <div style={{ fontSize: 72, fontWeight: 900, color: passed ? colors.success : colors.error }}>{score}%</div>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>
            {passed ? 'Excellent! You passed all foundations and unlocked scenarios.' : 'Not enough to skip foundations. Keep practicing!'}
          </p>
          <PrimaryButton label="Continue" onPress={() => navigate(passed ? '/scenarios' : '/foundations')} variant={passed ? 'primary' : 'secondary'} />
        </div>
      </Screen>
    );
  }

  if (!currentExercise) return null;

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: spacing.lg }}>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
            <span style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1 }}>Placement Test</span>
            <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>{exerciseIndex + 1} / {testExercises.length}</span>
          </div>
          <div style={progressBar()}>
            <div style={progressFill((exerciseIndex + 1) / testExercises.length)} />
          </div>
        </div>
      </header>

      <div style={{ flex: 1, minHeight: 0, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
        {!feedback ? (
          <div className="fade-in" key={exerciseIndex}>
            <div style={{ marginBottom: spacing.xl }}>
               <h2 style={{ color: colors.textSecondary, fontSize: 16, textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 8, fontWeight: 900 }}>
                {currentExercise.kind === 'fillBlank' ? 'Write in Italian' : 'Translate'}
              </h2>
              <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{currentExercise.prompt}</h1>
            </div>

            {currentExercise.kind === 'fillBlank' ? (
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
                {(currentExercise.options || []).map((choice: string, idx: number) => (
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
        ) : (
          <div className={feedback.status === 'correct' ? 'bounce' : 'shake'} style={feedbackCardStyle(feedback.status)}>
            <div style={{ fontSize: 48, marginBottom: 12 }}>
              {feedback.status === 'correct' ? '✅' : feedback.status === 'nearly_correct' ? '⚠️' : '❌'}
            </div>
            <div>
              {feedback.status === 'correct' ? 'Correct!' : (feedback.status === 'nearly_correct' ? 'Almost correct!' : 'Not quite.')}
            </div>
            {feedback.status !== 'correct' && (
              <div style={{ marginTop: 12, fontSize: 16, opacity: 0.9 }}>
                The correct answer is: <br/>
                <span style={{ fontSize: 24, textDecoration: 'underline' }}>{feedback.answer}</span>
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
          currentExercise.kind === 'fillBlank' ? (
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
