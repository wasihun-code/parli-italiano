import React, { useState, useMemo } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useGameStore } from '@shared/store/gameStore';
import storiesData from '@shared/data/stories.json';
import distractorsData from '@shared/data/stories_distractors.json';
import { PrimaryButton } from '../components/PrimaryButton';
import { shuffle } from '@shared/utils/trainingUi';

export const StoryFinalQuizScreen: React.FC = () => {
  const { storyId } = useParams<{ storyId: string }>();
  const navigate = useNavigate();
  const storyTitle = decodeURIComponent(storyId || '');
  const story = useMemo(() => storiesData.stories.find(s => s.title === storyTitle), [storyTitle]);

  const { completeStory, unlockedStories, unlockStory } = useGameStore();

  const [currentQIdx, setCurrentQIdx] = useState(0);
  const [answers, setAnswers] = useState<Record<number, string>>({});
  const [quizComplete, setQuizComplete] = useState(false);
  const [score, setScore] = useState(0);

  if (!story) return <Screen><p>Story not found.</p></Screen>;

  const questions = story.overall_questions;
  const currentQ = questions[currentQIdx];

  const distractorKey = `${story.title}_overall_${currentQIdx}`;
  const distractors = (distractorsData as any)[distractorKey] || ["Distractor 1", "Distractor 2", "Distractor 3"];
  const options = useMemo(() => shuffle([currentQ.answer, ...distractors]), [currentQ.answer, distractors]);

  const handleSelect = (opt: string) => {
    setAnswers(prev => ({ ...prev, [currentQIdx]: opt }));
    if (currentQIdx + 1 < questions.length) {
      setCurrentQIdx(currentQIdx + 1);
    } else {
      // Calculate score
      let correct = 0;
      questions.forEach((q, i) => {
        if (answers[i] === q.answer || (i === currentQIdx && opt === q.answer)) correct++;
      });
      const finalScore = Math.round((correct / questions.length) * 100);
      setScore(finalScore);
      setQuizComplete(true);
    }
  };

  const handleFinish = () => {
    if (score >= 70) {
      completeStory(storyTitle, score);
      
      // Unlock next difficulty if applicable
      const currentStoryIdx = storiesData.stories.findIndex(s => s.title === storyTitle);
      const nextStory = storiesData.stories.find((s, i) => i > currentStoryIdx && s.difficulty > story.difficulty);
      if (nextStory && !unlockedStories.includes(nextStory.title)) {
        unlockStory(nextStory.title);
      } else {
        // Also unlock the very next story in the same difficulty if not unlocked
        const nextSameDiff = storiesData.stories.find((s, i) => i > currentStoryIdx && s.difficulty === story.difficulty);
        if (nextSameDiff && !unlockedStories.includes(nextSameDiff.title)) {
          unlockStory(nextSameDiff.title);
        } else if (!nextSameDiff) {
            // Unlock first of next difficulty
            const firstNextDiff = storiesData.stories.find(s => s.difficulty === story.difficulty + 1);
            if (firstNextDiff && !unlockedStories.includes(firstNextDiff.title)) {
                unlockStory(firstNextDiff.title);
            }
        }
      }
      navigate('/stories');
    } else {
      // Retry
      setCurrentQIdx(0);
      setAnswers({});
      setQuizComplete(false);
    }
  };

  if (quizComplete) {
    const passed = score >= 70;
    return (
      <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
        <div className="card fade-in" style={{ padding: spacing.xl, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h1 style={{ fontSize: 48 }}>{passed ? '🎉 Bravo!' : '😕 Riprova'}</h1>
          <p style={{ fontSize: 24, color: colors.textSecondary }}>Il tuo punteggio: {score}%</p>
          <p>{passed ? 'Hai completato la storia con successo!' : 'Ti serve almeno il 70% per passare.'}</p>
          <PrimaryButton label={passed ? "Back to Stories" : "Retry Quiz"} onPress={handleFinish} />
        </div>
      </Screen>
    );
  }

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.xl }}>
        <h1 style={{ color: colors.primary, fontSize: 24, fontWeight: 900, margin: 0 }}>Final Quiz: {story.title}</h1>
        <div style={{ marginTop: 8 }}>
          <div style={{ height: 6, backgroundColor: 'rgba(0,0,0,0.1)', borderRadius: 3 }}>
            <div style={{ 
              height: '100%', 
              backgroundColor: colors.accent, 
              borderRadius: 3, 
              width: `${((currentQIdx + 1) / questions.length) * 100}%`,
              transition: 'width 0.3s'
            }} />
          </div>
          <p style={{ textAlign: 'right', fontSize: 12, fontWeight: 'bold', color: colors.textSecondary, marginTop: 4 }}>
            Question {currentQIdx + 1} of {questions.length}
          </p>
        </div>
      </header>

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
        <div className="card" style={{ padding: spacing.xl, backgroundColor: '#fff', borderRadius: 24 }}>
          <h2 style={{ color: colors.primary, fontSize: 22, margin: 0 }}>{currentQ.question}</h2>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.md }}>
          {options.map(opt => (
            <button 
              key={opt}
              onClick={() => handleSelect(opt)}
              style={{ 
                padding: spacing.lg, 
                textAlign: 'left', 
                borderRadius: 16, 
                border: `2px solid ${colors.border}`, 
                backgroundColor: '#fff',
                fontWeight: 'bold',
                color: colors.primary,
                cursor: 'pointer',
                fontSize: 18,
                transition: 'all 0.2s'
              }}
            >
              {opt}
            </button>
          ))}
        </div>
      </div>
    </Screen>
  );
};
