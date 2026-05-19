import React, { useState, useMemo } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import grammarExpanded from '@shared/data/grammarExpanded.json';
import { useGrammarStore } from '@shared/store/grammarStore';
import { ProgressBar } from '../components/ProgressBar';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { ShortcutHelp } from '../components/ShortcutHelp';
import { getWrongAnswerExplanation } from '@shared/utils/feedbackExplanations';

export const GrammarLessonScreen: React.FC = () => {
  const { lessonId } = useParams<{ lessonId: string }>();
  const navigate = useNavigate();
  const markCompleted = useGrammarStore(state => state.markCompleted);
  
  const lesson = useMemo(() => grammarExpanded.find(l => l.id === lessonId), [lessonId]);
  
  const [phase, setPhase] = useState<'learn' | 'practice'>('learn');
  const [exIndex, setExIndex] = useState(0);
  const [typedAnswer, setTypedAnswer] = useState('');
  const [feedback, setFeedback] = useState<{ type: 'correct' | 'incorrect', explanation?: string } | null>(null);

  if (!lesson) return <Screen><p>Lesson not found.</p></Screen>;

  const handleStartPractice = () => setPhase('practice');

  const exercise = lesson.exercises[exIndex];

  const submitAnswer = (ans?: string) => {
    if (feedback) return;
    const submitted = ans ?? typedAnswer;
    if (!submitted.trim()) return;

    if (submitted.toLowerCase() === exercise.answer.toLowerCase()) {
      setFeedback({ type: 'correct' });
    } else {
      const explanation = getWrongAnswerExplanation({
        type: 'grammar',
        category: lesson.id,
        correctAnswer: exercise.answer
      });
      setFeedback({ type: 'incorrect', explanation });
    }
  };

  const advance = () => {
    setFeedback(null);
    setTypedAnswer('');
    if (exIndex + 1 < lesson.exercises.length) {
      setExIndex(i => i + 1);
    } else {
      markCompleted(lesson.id);
      navigate('/grammar');
    }
  };

  if (phase === 'learn') {
    return (
      <Screen style={{ backgroundColor: colors.surface }}>
        <header style={{ marginBottom: spacing.lg }}>
          <h1 style={{ color: colors.primary, fontSize: 28, margin: 0, fontWeight: 900 }}>{lesson.title}</h1>
        </header>

        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg, paddingBottom: 100 }}>
          <div className="card" style={{ padding: spacing.lg }}>
            <div style={{ color: colors.textSecondary, fontSize: 16, lineHeight: '1.6', whiteSpace: 'pre-line' }}>
              {lesson.explanation}
            </div>
            
            <h3 style={{ marginTop: spacing.xl, marginBottom: spacing.sm, color: colors.primary }}>Examples</h3>
            <div style={{ backgroundColor: 'rgba(78, 52, 46, 0.05)', padding: spacing.md, borderRadius: 12 }}>
              {lesson.examples.map((ex, i) => (
                <div key={i} style={{ marginBottom: i < lesson.examples.length - 1 ? spacing.sm : 0 }}>
                  <div style={{ fontWeight: 'bold', color: colors.primary }}>{ex.italian}</div>
                  <div style={{ color: colors.textSecondary, fontSize: 14 }}>{ex.english}</div>
                </div>
              ))}
            </div>
          </div>

          <PrimaryButton label="Start Practice" onPress={handleStartPractice} />
        </div>
      </Screen>
    );
  }

  // Practice Phase
  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.lg }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
          <span style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase', letterSpacing: 1, display: 'flex', alignItems: 'center' }}>
            Practice
            <ShortcutHelp />
          </span>
          <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>{exIndex + 1} / {lesson.exercises.length}</span>
        </div>
        <ProgressBar progress={((exIndex + 1) / lesson.exercises.length) * 100} />
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
        {!feedback ? (
          <div className="fade-in">
            <h1 style={{ color: colors.primary, fontSize: 24, margin: '0 0 24px', fontWeight: 900 }}>{exercise.question}</h1>
            
            {exercise.type === 'multiple-choice' ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
                {(exercise.options || []).map(opt => (
                  <button
                    key={opt}
                    onClick={() => submitAnswer(opt)}
                    className="card"
                    style={{
                      padding: spacing.lg,
                      textAlign: 'left',
                      fontSize: 18,
                      fontWeight: 700,
                      color: colors.primary,
                      border: `2px solid ${colors.border}`,
                      cursor: 'pointer'
                    }}
                  >
                    {opt}
                  </button>
                ))}
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg }}>
                <input
                  autoFocus
                  type="text"
                  value={typedAnswer}
                  onChange={e => setTypedAnswer(e.target.value)}
                  onKeyDown={e => e.key === 'Enter' && submitAnswer()}
                  placeholder="Type your answer..."
                  style={{
                    padding: spacing.lg,
                    borderRadius: 16,
                    border: `2px solid ${colors.border}`,
                    fontSize: 20,
                    outline: 'none',
                    backgroundColor: colors.bg,
                    color: colors.primary,
                    fontWeight: 700,
                    textAlign: 'center'
                  }}
                />
                <PrimaryButton label="Check" onPress={() => submitAnswer()} disabled={!typedAnswer.trim()} />
              </div>
            )}
            <p style={{ textAlign: 'center', color: colors.textSecondary, fontSize: 14, margin: '16px 0 0', fontWeight: 800 }}>
              Tip: Press 1-4 to select, Enter to submit
            </p>
          </div>
        ) : (
          <div className="fade-in" style={{ textAlign: 'center' }}>
            <FeedbackMessage 
              type={feedback.type} 
              message={
                feedback.type === 'correct' 
                  ? 'Correct!' 
                  : (
                    <>
                      <div>Not quite. The correct answer is: <br/><strong>{exercise.answer}</strong></div>
                      {feedback.explanation && (
                        <div style={{ marginTop: spacing.sm, fontSize: 14, fontWeight: 'normal', color: colors.textSecondary }}>
                          {feedback.explanation}
                        </div>
                      )}
                    </>
                  )
              } 
            />
          </div>
        )}
      </div>

      {feedback && (
        <div style={{ marginTop: 'auto', paddingTop: spacing.xl }}>
          <PrimaryButton label="Continue" onPress={advance} />
        </div>
      )}
    </Screen>
  );
};
