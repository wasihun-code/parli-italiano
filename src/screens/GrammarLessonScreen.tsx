import React, { useState, useMemo } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { grammarLessons } from '@shared/data/grammarLessons';
import { useGrammarStore } from '@shared/store/grammarStore';

export const GrammarLessonScreen: React.FC = () => {
  const { lessonId } = useParams<{ lessonId: string }>();
  const navigate = useNavigate();
  const markCompleted = useGrammarStore(state => state.markCompleted);
  
  const lesson = useMemo(() => grammarLessons.find(l => l.id === lessonId), [lessonId]);
  
  const [phase, setPhase] = useState<'learn' | 'practice'>('learn');
  const [exIndex, setExIndex] = useState(0);
  const [typedAnswer, setTypedAnswer] = useState('');
  const [feedback, setFeedback] = useState<'correct' | 'incorrect' | null>(null);

  if (!lesson) return <Screen><p>Lesson not found.</p></Screen>;

  const handleStartPractice = () => setPhase('practice');

  const exercise = lesson.exercises[exIndex];

  const submitAnswer = (ans?: string) => {
    if (feedback) return;
    const submitted = ans ?? typedAnswer;
    if (!submitted.trim()) return;

    if (submitted.toLowerCase() === exercise.answer.toLowerCase()) {
      setFeedback('correct');
    } else {
      setFeedback('incorrect');
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
          {lesson.explanation.map((block, idx) => (
            <div key={idx} className="card" style={{ padding: spacing.lg }}>
              <p style={{ color: colors.textSecondary, fontSize: 16, lineHeight: '1.5', marginTop: 0 }}>
                {block.text}
              </p>
              <div style={{ backgroundColor: 'rgba(78, 52, 46, 0.05)', padding: spacing.md, borderRadius: 12 }}>
                {block.examples.map((ex, i) => (
                  <div key={i} style={{ marginBottom: i < block.examples.length - 1 ? spacing.sm : 0 }}>
                    <div style={{ fontWeight: 'bold', color: colors.primary }}>{ex.it}</div>
                    <div style={{ color: colors.textSecondary, fontSize: 14 }}>{ex.en}</div>
                  </div>
                ))}
              </div>
            </div>
          ))}

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
          <span style={{ color: colors.textSecondary, fontWeight: '900', fontSize: 12, textTransform: 'uppercase' }}>Practice</span>
          <span style={{ color: colors.accent, fontWeight: 900, fontSize: 12 }}>{exIndex + 1} / {lesson.exercises.length}</span>
        </div>
        <div style={{ height: 8, backgroundColor: 'rgba(78, 52, 46, 0.1)', borderRadius: 4 }}>
          <div style={{ height: '100%', width: `${((exIndex + 1) / lesson.exercises.length) * 100}%`, backgroundColor: colors.accent, borderRadius: 4 }} />
        </div>
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
        {!feedback ? (
          <div className="fade-in">
            <h1 style={{ color: colors.primary, fontSize: 24, margin: '0 0 24px', fontWeight: 900 }}>{exercise.prompt}</h1>
            
            {exercise.kind === 'multipleChoice' ? (
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
          </div>
        ) : (
          <div className={feedback === 'correct' ? 'bounce' : 'shake'} style={{
            backgroundColor: feedback === 'correct' ? colors.success : colors.error,
            color: colors.onPrimary,
            padding: spacing.xl,
            borderRadius: 24,
            textAlign: 'center',
            display: 'flex',
            flexDirection: 'column',
            gap: spacing.md
          }}>
            <div style={{ fontSize: 48 }}>{feedback === 'correct' ? '✅' : '❌'}</div>
            <div style={{ fontSize: 24, fontWeight: 900 }}>{feedback === 'correct' ? 'Correct!' : 'Not quite'}</div>
            {feedback === 'incorrect' && (
              <div style={{ marginTop: spacing.md }}>
                <div style={{ fontSize: 16, opacity: 0.9, marginBottom: 4 }}>The correct answer is:</div>
                <div style={{ fontSize: 22, fontWeight: 'bold' }}>{exercise.answer}</div>
              </div>
            )}
          </div>
        )}
      </div>

      {feedback && (
        <div style={{ marginTop: 'auto', paddingTop: spacing.xl }}>
          <PrimaryButton label="Continue" onPress={advance} variant={feedback === 'incorrect' ? 'secondary' : 'primary'} />
        </div>
      )}
    </Screen>
  );
};
