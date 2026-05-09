import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { Keyboard } from '../components/Keyboard';
import { foundationLessons } from '@shared/data/foundations';
import { useProgressStore } from '@shared/store/progressStore';
import { useSrsStore } from '@shared/store/srsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { percentageScore } from '@shared/utils/scoring';
import { progressBar, progressFill, feedbackCardStyle } from '@shared/utils/trainingUi';

function normalizeAnswer(value: string): string {
  return value.trim().toLocaleLowerCase('it-IT');
}

export const FoundationLessonScreen: React.FC = () => {
  const { lessonId } = useParams<{ lessonId: string }>();
  const navigate = useNavigate();
  const lesson = foundationLessons.find(item => item.id === Number(lessonId));
  
  const registerItem = useSrsStore(state => state.registerItem);
  const recordSrsAnswer = useSrsStore(state => state.recordAnswer);
  const recordFoundationScore = useProgressStore(state => state.recordFoundationScore);
  const bestScore = useProgressStore(state => state.foundationScores[Number(lessonId)] ?? 0);

  const [exerciseIndex, setExerciseIndex] = useState(0);
  const [correctCount, setCorrectCount] = useState(0);
  const [typedAnswer, setTypedAnswer] = useState('');
  const [selectedAnswer, setSelectedAnswer] = useState<string>();
  const [feedback, setFeedback] = useState<'correct' | 'incorrect'>();
  const [finishedScore, setFinishedScore] = useState<number>();

  useEffect(() => {
    if (lesson) {
      lesson.terms.forEach(term =>
        registerItem({
          id: term.id,
          type: 'foundation',
          italian: term.italian,
          english: term.english,
        }),
      );
    }
  }, [lesson, registerItem]);

  const exercises = lesson?.exercises ?? [];
  const exercise = exercises[exerciseIndex];
  const progressLabel = `${Math.min(exerciseIndex + 1, exercises.length)} / ${exercises.length}`;

  const choices = useMemo(() => exercise?.options ?? [], [exercise]);

  const speak = useCallback((): void => {
    if (exercise) {
      Tts.speak(exercise.answer);
    }
  }, [exercise]);

  useEffect(() => {
    if (exercise?.kind === 'listening' && !feedback) {
      speak();
    }
  }, [exercise, feedback, speak]);

  const submittedAnswer = exercise?.kind === 'fillBlank' ? typedAnswer : selectedAnswer ?? '';
  const canSubmit = normalizeAnswer(submittedAnswer).length > 0;

  const submitAnswer = useCallback((): void => {
    if (!lesson || !exercise) return;
    const correct = normalizeAnswer(submittedAnswer) === normalizeAnswer(exercise.answer);
    setFeedback(correct ? 'correct' : 'incorrect');
    if (correct) {
      setCorrectCount(current => current + 1);
    }
    const matchingTerm = lesson.terms.find(
      term => normalizeAnswer(term.italian) === normalizeAnswer(exercise.answer),
    );
    if (matchingTerm) {
      recordSrsAnswer(matchingTerm.id, correct);
    }
  }, [exercise, lesson, recordSrsAnswer, submittedAnswer]);

  const advance = useCallback((): void => {
    if (!lesson) return;
    const nextIndex = exerciseIndex + 1;
    setTypedAnswer('');
    setSelectedAnswer(undefined);
    setFeedback(undefined);

    if (nextIndex >= exercises.length) {
      const finalScore = percentageScore(correctCount, exercises.length);
      setFinishedScore(finalScore);
      recordFoundationScore(lesson.id, finalScore);
      return;
    }

    setExerciseIndex(nextIndex);
  }, [correctCount, exerciseIndex, exercises.length, lesson, recordFoundationScore]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (feedback) {
        if (e.key === 'Enter') advance();
        return;
      }

      if (e.key === 'Enter' && canSubmit) {
        submitAnswer();
      }

      if (exercise?.kind !== 'fillBlank' && !feedback) {
        if (e.key >= '1' && e.key <= '4') {
          const idx = parseInt(e.key) - 1;
          if (choices[idx]) {
            setSelectedAnswer(choices[idx]);
            const correct = normalizeAnswer(choices[idx]) === normalizeAnswer(exercise.answer);
            setFeedback(correct ? 'correct' : 'incorrect');
            if (correct) {
              setCorrectCount(current => current + 1);
            }
            const matchingTerm = lesson?.terms.find(
              term => normalizeAnswer(term.italian) === normalizeAnswer(exercise.answer),
            );
            if (matchingTerm) {
              recordSrsAnswer(matchingTerm.id, correct);
            }
          }
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [advance, canSubmit, choices, exercise, feedback, lesson, recordSrsAnswer, submitAnswer]);

  if (!lesson || !exercise) {
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <h1 style={{ color: colors.primary }}>Lesson not found</h1>
        <PrimaryButton label="Back to Foundations" onPress={() => navigate('/foundations')} />
      </Screen>
    );
  }

  if (finishedScore !== undefined) {
    const passed = finishedScore >= 90;
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{
          padding: spacing.xl,
          display: 'flex',
          flexDirection: 'column',
          gap: spacing.lg,
          textAlign: 'center',
          cursor: 'default'
        }}>
          <h1 style={{ color: colors.primary, margin: 0, fontSize: 32 }}>{lesson.title}</h1>
          <div style={{
            fontSize: 72,
            fontWeight: 900,
            color: passed ? colors.success : colors.error
          }}>
            {finishedScore}%
          </div>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>
            {passed
              ? 'Lesson passed! This score counts towards unlocking scenarios.'
              : 'Retry this lesson until you reach 90%.'}
          </p>
          <div style={{ backgroundColor: colors.chipBg, padding: spacing.md, borderRadius: 16, fontSize: 14, fontWeight: 800 }}>
             Best score: {Math.max(bestScore, finishedScore)}%
          </div>
          <PrimaryButton
            label={passed ? 'Back to Foundations' : 'Try Again'}
            onPress={() => {
              if (passed) {
                navigate('/foundations');
                return;
              }
              setExerciseIndex(0);
              setCorrectCount(0);
              setFinishedScore(undefined);
            }}
          />
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: spacing.lg }}>
        <div style={{ flex: 1 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
            <span style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1 }}>{lesson.title}</span>
            <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>{progressLabel}</span>
          </div>
          <div style={progressBar()}>
            <div style={progressFill((exerciseIndex + 1) / exercises.length)} />
          </div>
        </div>
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
        {feedback ? (
          <div className={feedback === 'correct' ? 'bounce' : 'shake'} style={feedbackCardStyle(feedback === 'correct' ? 'correct' : 'incorrect')}>
            <div style={{ fontSize: 48, marginBottom: 12 }}>
              {feedback === 'correct' ? '✅' : '❌'}
            </div>
            <div>
              {feedback === 'correct' ? 'Excellent!' : 'Ops! Not quite.'}
            </div>
            {feedback === 'incorrect' && (
              <div style={{ marginTop: 12, fontSize: 16, opacity: 0.9 }}>
                The correct answer is: <br/>
                <span style={{ fontSize: 24, textDecoration: 'underline' }}>{exercise.answer}</span>
              </div>
            )}
          </div>
        ) : (
          <div className="fade-in" key={exerciseIndex}>
            <div style={{ marginBottom: spacing.xl }}>
               <h2 style={{ color: colors.textSecondary, fontSize: 16, textTransform: 'uppercase', letterSpacing: 1.5, marginBottom: 8, fontWeight: 900 }}>
                {exercise.kind === 'listening' ? 'Listen and write' : 'Translate'}
              </h2>
              <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>{exercise.prompt}</h1>
            </div>

            {exercise.kind === 'listening' && (
              <div style={{ display: 'flex', justifyContent: 'center', marginBottom: spacing.xl }}>
                 <button 
                  onClick={speak}
                  className="card active"
                  style={{ 
                    width: 80, 
                    height: 80, 
                    borderRadius: 40, 
                    display: 'flex', 
                    alignItems: 'center', 
                    justifyContent: 'center',
                    borderWidth: 3,
                  }}
                >
                  <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
                  </svg>
                </button>
              </div>
            )}

            {exercise.kind === 'fillBlank' ? (
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
                {choices.map((choice, idx) => (
                  <button
                    key={choice}
                    onClick={() => {
                      setSelectedAnswer(choice);
                      const correct = normalizeAnswer(choice) === normalizeAnswer(exercise.answer);
                      setFeedback(correct ? 'correct' : 'incorrect');
                      if (correct) setCorrectCount(c => c + 1);
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
          <PrimaryButton label="Check" onPress={submitAnswer} disabled={!canSubmit} />
        ) : (
          <PrimaryButton label="Continue" onPress={advance} variant={feedback === 'incorrect' ? 'secondary' : 'primary'} />
        )}
      </div>
    </Screen>
  );
};
