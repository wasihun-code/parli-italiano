import React, { useState, useMemo, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useGameStore } from '@shared/store/gameStore';
import storiesData from '@shared/data/stories.json';
import distractorsData from '@shared/data/stories_distractors.json';
import { PrimaryButton } from '../components/PrimaryButton';
import { FeedbackMessage } from '../components/FeedbackMessage';
import { normalizeString, levenshteinDistance } from '@shared/utils/string';
import { shuffle } from '@shared/utils/trainingUi';

interface ComprehensionQuestionProps {
  q: any;
  index: number;
  storyTitle: string;
  partIdx: number;
  pageIdx: number;
  feedback: Record<string, any>;
  validateComp: (opt: string, answer: string, index: number) => void;
}

const ComprehensionQuestion: React.FC<ComprehensionQuestionProps> = ({ 
  q, index, storyTitle, partIdx, pageIdx, feedback, validateComp 
}) => {
  const key = `comprehension_${index}`;
  const f = feedback[key];
  const distractorKey = `${storyTitle}_${partIdx + 1}_${pageIdx + 1}_${index}`;
  const distractors = (distractorsData as any)[distractorKey] || ["Distractor 1", "Distractor 2", "Distractor 3"];
  const options = useMemo(() => shuffle([q.answer, ...distractors]), [q.answer, distractors]);

  return (
    <div style={{ marginBottom: spacing.lg }}>
      <p style={{ fontWeight: 'bold', marginBottom: 12 }}>{q.question}</p>
      {f ? (
        <FeedbackMessage type={f.type} message={f.type === 'correct' ? 'Correct!' : f.message} />
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: spacing.sm }}>
          {options.map(opt => (
            <button 
              key={opt}
              onClick={() => validateComp(opt, q.answer, index)}
              style={{ 
                padding: spacing.md, 
                textAlign: 'left', 
                borderRadius: 12, 
                border: `2px solid ${colors.border}`, 
                backgroundColor: '#fff',
                fontWeight: 'bold',
                color: colors.primary,
                cursor: 'pointer'
              }}
            >
              {opt}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export const StoryReaderScreen: React.FC = () => {
  const { storyId } = useParams<{ storyId: string }>();
  const navigate = useNavigate();
  const storyTitle = decodeURIComponent(storyId || '');
  const story = useMemo(() => storiesData.stories.find(s => s.title === storyTitle), [storyTitle]);

  const { storyProgress, updateStoryProgress } = useGameStore();
  const progress = storyProgress[storyTitle] || {
    currentPart: 0,
    currentPage: 0,
    currentSubPage: 0,
    completedPages: [],
    completedParts: [],
    translateUsesRemaining: 10
  };

  const [partIdx, setPartIndex] = useState(progress.currentPart);
  const [pageIdx, setPageIndex] = useState(progress.currentPage);
  const [subPageIdx, setSubPageIdx] = useState(progress.currentSubPage || 0);
  const [showEnglish, setShowEnglish] = useState(false);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [feedback, setFeedback] = useState<Record<string, { type: 'correct' | 'incorrect', message?: string }>>({});

  const currentPart = story?.parts[partIdx];
  const currentPage = currentPart?.pages[pageIdx];

  const totalParts = story?.parts.length || 0;
  const totalPagesInPart = currentPart?.pages.length || 0;

  const splitIntoSubPages = (text: string) => {
    if (!text) return [];
    // Split by punctuation followed by space or end of string
    const sentences = text.match(/[^.!?]+[.!?]+(?:\s+|$)|[^.!?]+$/g) || [text];
    const subPages: string[] = [];
    for (let i = 0; i < sentences.length; i += 2) {
      subPages.push(sentences.slice(i, i + 2).join('').trim());
    }
    return subPages;
  };

  const italianSubPages = useMemo(() => splitIntoSubPages(currentPage?.italian_text || ''), [currentPage]);
  const englishSubPages = useMemo(() => splitIntoSubPages(currentPage?.english_text || ''), [currentPage]);

  useEffect(() => {
    // Sync store on change
    updateStoryProgress(storyTitle, { currentPart: partIdx, currentPage: pageIdx, currentSubPage: subPageIdx });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [partIdx, pageIdx, subPageIdx, storyTitle, updateStoryProgress]);

  // Reset subPageIdx when page changes from outside (e.g. restoration)
  useEffect(() => {
    if (progress.currentPage !== pageIdx) {
       // Only reset if it's a different page than what's in progress
       // but wait, progress is also updated by us.
    }
  }, [pageIdx]);

  // Reset page-specific state when moving pages
  useEffect(() => {
    const pageKey = `${partIdx}_${pageIdx}`;
    const isCompleted = progress.completedPages.includes(pageKey);
    
    setShowEnglish(false);
    setAnswers({});
    
    if (isCompleted) {
      // Pre-fill feedback as correct if already passed
      const newFeedback: Record<string, { type: 'correct' | 'incorrect', message?: string }> = {};
      currentPage?.questions.vocabulary.forEach((_, i) => newFeedback[`vocabulary_${i}`] = { type: 'correct' });
      currentPage?.questions.translation.forEach((_, i) => newFeedback[`translation_${i}`] = { type: 'correct' });
      currentPage?.questions.comprehension.forEach((_, i) => newFeedback[`comprehension_${i}`] = { type: 'correct' });
      setFeedback(newFeedback);
    } else {
      setFeedback({});
    }
  }, [partIdx, pageIdx, currentPage, progress.completedPages]);

  if (!story || !currentPage) return <Screen><p>Story not found.</p></Screen>;

  const handleTranslate = () => {
    if (showEnglish) {
      setShowEnglish(false);
      return;
    }

    if (story.difficulty === 1 || progress.translateUsesRemaining > 0) {
      setShowEnglish(true);
      if (story.difficulty > 1) {
        updateStoryProgress(storyTitle, { translateUsesRemaining: progress.translateUsesRemaining - 1 });
      }
    }
  };

  const validateTyped = (submitted: string, expected: string, type: 'vocabulary' | 'translation', qIndex: number) => {
    const normSubmitted = normalizeString(submitted);
    const normExpected = normalizeString(expected);
    const isCorrect = normSubmitted === normExpected || (normExpected.length >= 4 && levenshteinDistance(normSubmitted, normExpected) <= 1);
    
    const qKey = `${type}_${qIndex}`;
    if (isCorrect) {
      setFeedback(prev => ({ ...prev, [qKey]: { type: 'correct' } }));
    } else {
      setFeedback(prev => ({ ...prev, [qKey]: { type: 'incorrect', message: 'Incorrect. Try again!' } }));
    }
  };

  const validateComp = (submitted: string, expected: string, qIndex: number) => {
    const isCorrect = submitted === expected;
    const qKey = `comprehension_${qIndex}`;
    if (isCorrect) {
      setFeedback(prev => ({ ...prev, [qKey]: { type: 'correct' } }));
    } else {
      setFeedback(prev => ({ ...prev, [qKey]: { type: 'incorrect', message: `Incorrect. The correct answer is: ${expected}` } }));
    }
  };

  const isPageComplete = () => {
    const pageKey = `${partIdx}_${pageIdx}`;
    if (progress.completedPages.includes(pageKey)) return true;

    const totalQuestions = currentPage.questions.vocabulary.length + currentPage.questions.translation.length + currentPage.questions.comprehension.length;
    const correctCount = Object.values(feedback).filter(f => f.type === 'correct').length;
    return correctCount === totalQuestions;
  };

  const isLastSubPage = subPageIdx === italianSubPages.length - 1;

  const handleNext = () => {
    if (subPageIdx < italianSubPages.length - 1) {
      setSubPageIdx(subPageIdx + 1);
      return;
    }

    if (!isPageComplete()) return;

    // Save page completion
    const pageKey = `${partIdx}_${pageIdx}`;
    if (!progress.completedPages.includes(pageKey)) {
      updateStoryProgress(storyTitle, { completedPages: [...progress.completedPages, pageKey] });
    }

    if (pageIdx + 1 < totalPagesInPart) {
      setPageIndex(pageIdx + 1);
      setSubPageIdx(0);
    } else if (partIdx + 1 < totalParts) {
      // Mark part as complete
      if (!progress.completedParts.includes(partIdx)) {
        updateStoryProgress(storyTitle, { completedParts: [...progress.completedParts, partIdx] });
      }
      setPartIndex(partIdx + 1);
      setPageIndex(0);
      setSubPageIdx(0);
    } else {
      // Final quiz
      navigate(`/stories/${encodeURIComponent(storyTitle)}/quiz`);
    }
  };

  const handleBack = () => {
    if (subPageIdx > 0) {
      setSubPageIdx(subPageIdx - 1);
    } else if (pageIdx > 0) {
      const prevPageIndex = pageIdx - 1;
      const prevPage = currentPart?.pages[prevPageIndex];
      const prevItalianSubPages = splitIntoSubPages(prevPage?.italian_text || '');
      setPageIndex(prevPageIndex);
      setSubPageIdx(prevItalianSubPages.length - 1);
    } else if (partIdx > 0) {
      const prevPartIndex = partIdx - 1;
      const prevPart = story.parts[prevPartIndex];
      const prevPageIndex = prevPart.pages.length - 1;
      const prevPage = prevPart.pages[prevPageIndex];
      const prevItalianSubPages = splitIntoSubPages(prevPage?.italian_text || '');
      setPartIndex(prevPartIndex);
      setPageIndex(prevPageIndex);
      setSubPageIdx(prevItalianSubPages.length - 1);
    } else {
      navigate('/stories');
    }
  };

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.lg }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1 style={{ color: colors.primary, fontSize: 24, fontWeight: 900, margin: 0 }}>{story.title}</h1>
          <span style={{ fontSize: 14, fontWeight: 'bold', color: colors.textSecondary }}>
            Part {partIdx + 1}/{totalParts}, Page {pageIdx + 1}/{totalPagesInPart}
          </span>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 8 }}>
          <div style={{ flex: 1, height: 6, backgroundColor: 'rgba(0,0,0,0.1)', borderRadius: 3, marginRight: 16 }}>
            <div style={{ 
              height: '100%', 
              backgroundColor: colors.success, 
              borderRadius: 3, 
              width: `${((pageIdx + 1) / totalPagesInPart) * 100}%`,
              transition: 'width 0.3s'
            }} />
          </div>
          {story.difficulty > 1 && (
            <span style={{ fontSize: 12, fontWeight: '900', color: progress.translateUsesRemaining > 3 ? colors.accent : colors.error }}>
              🔍 {progress.translateUsesRemaining} hints left
            </span>
          )}
        </div>
        <div style={{ marginTop: 8, fontSize: 12, color: colors.textSecondary, textAlign: 'right' }}>
          Section {subPageIdx + 1} of {italianSubPages.length}
        </div>
      </header>

      <div className="story-reader-layout">
        <div className="story-reader-text coffee-card">
          <p style={{ fontSize: 20, lineHeight: '1.6', color: colors.primary, margin: 0, whiteSpace: 'pre-wrap' }}>
            {italianSubPages[subPageIdx]}
          </p>
          
          {showEnglish && (
            <div className="fade-in" style={{ marginTop: spacing.lg, paddingTop: spacing.lg, borderTop: `1px solid ${colors.border}`, color: colors.textSecondary, fontStyle: 'italic' }}>
              {englishSubPages[subPageIdx] || englishSubPages[englishSubPages.length - 1]}
            </div>
          )}

          <button 
            onClick={handleTranslate}
            disabled={!showEnglish && story.difficulty > 1 && progress.translateUsesRemaining <= 0}
            style={{
              marginTop: spacing.lg,
              background: 'none',
              border: `1px dashed ${colors.primary}`,
              color: colors.primary,
              padding: '8px 16px',
              borderRadius: 8,
              cursor: 'pointer',
              fontSize: 14,
              fontWeight: 'bold',
              opacity: (!showEnglish && story.difficulty > 1 && progress.translateUsesRemaining <= 0) ? 0.5 : 1
            }}
          >
            {showEnglish ? 'Undo Translation' : (story.difficulty === 1 ? 'Show Translation' : 'Use Hint (Show Translation)')}
          </button>
        </div>

        {isLastSubPage && (
          <div className="story-reader-questions" style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl, marginTop: spacing.xl }}>
            {/* Vocabulary Questions */}
            {currentPage.questions.vocabulary.length > 0 && (
              <section>
                <h3 style={{ color: colors.accent, textTransform: 'uppercase', fontSize: 14, letterSpacing: 1.2, marginBottom: spacing.md }}>Vocabulary</h3>
                {currentPage.questions.vocabulary.map((q, i) => {
                  const key = `vocabulary_${i}`;
                  const f = feedback[key];
                  return (
                    <div key={key} style={{ marginBottom: spacing.lg }}>
                      <p style={{ fontWeight: 'bold', marginBottom: 8 }}>{q.question}</p>
                      {f && f.type === 'correct' ? (
                        <FeedbackMessage type="correct" message="Ottimo!" />
                      ) : (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
                          <div style={{ display: 'flex', gap: spacing.sm }}>
                            <input 
                              type="text" 
                              placeholder="Type answer..." 
                              value={answers[key] || ''}
                              onChange={e => {
                                setAnswers(prev => ({ ...prev, [key]: e.target.value }));
                                if (f?.type === 'incorrect') {
                                  setFeedback(prev => {
                                    const next = { ...prev };
                                    delete next[key];
                                    return next;
                                  });
                                }
                              }}
                              style={{ flex: 1, padding: spacing.md, borderRadius: 12, border: `2px solid ${colors.border}`, outline: 'none' }}
                            />
                            <button 
                              onClick={() => validateTyped(answers[key] || '', q.answer, 'vocabulary', i)}
                              style={{ padding: '0 20px', borderRadius: 12, backgroundColor: colors.primary, color: '#fff', border: 'none', fontWeight: 'bold', cursor: 'pointer' }}
                            >
                              Check
                            </button>
                          </div>
                          {f?.type === 'incorrect' && (
                            <div style={{ color: colors.error, fontSize: 14, fontWeight: 'bold', marginLeft: 4 }}>{f.message}</div>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
              </section>
            )}

            {/* Translation Questions */}
            {currentPage.questions.translation.length > 0 && (
              <section>
                <h3 style={{ color: colors.accent, textTransform: 'uppercase', fontSize: 14, letterSpacing: 1.2, marginBottom: spacing.md }}>Translation</h3>
                {currentPage.questions.translation.map((q, i) => {
                  const key = `translation_${i}`;
                  const f = feedback[key];
                  return (
                    <div key={key} style={{ marginBottom: spacing.lg }}>
                      <p style={{ fontWeight: 'bold', marginBottom: 8 }}>{q.question}</p>
                      {f && f.type === 'correct' ? (
                        <FeedbackMessage type="correct" message="Ottimo!" />
                      ) : (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
                          <textarea 
                            placeholder="Type translation..." 
                            value={answers[key] || ''}
                            onChange={e => {
                              setAnswers(prev => ({ ...prev, [key]: e.target.value }));
                              if (f?.type === 'incorrect') {
                                setFeedback(prev => {
                                  const next = { ...prev };
                                  delete next[key];
                                  return next;
                                });
                              }
                            }}
                            style={{ padding: spacing.md, borderRadius: 12, border: `2px solid ${colors.border}`, outline: 'none', minHeight: 80, resize: 'none' }}
                          />
                          <PrimaryButton label="Check" onPress={() => validateTyped(answers[key] || '', q.answer, 'translation', i)} disabled={!(answers[key] || '').trim()} />
                          {f?.type === 'incorrect' && (
                            <div style={{ color: colors.error, fontSize: 14, fontWeight: 'bold', marginTop: 4, textAlign: 'center' }}>{f.message}</div>
                          )}
                        </div>
                      )}
                    </div>
                  );
                })}
              </section>
            )}

            {/* Comprehension Questions */}
            {currentPage.questions.comprehension.length > 0 && (
              <section>
                <h3 style={{ color: colors.accent, textTransform: 'uppercase', fontSize: 14, letterSpacing: 1.2, marginBottom: spacing.md }}>Comprehension</h3>
                {currentPage.questions.comprehension.map((q, i) => (
                  <ComprehensionQuestion 
                    key={`comp_${i}`}
                    q={q}
                    index={i}
                    storyTitle={story.title}
                    partIdx={partIdx}
                    pageIdx={pageIdx}
                    feedback={feedback}
                    validateComp={validateComp}
                  />
                ))}
              </section>
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
            display: 'flex',
            gap: spacing.md,
            maxWidth: 700,
            margin: '0 auto',
            zIndex: 50
            }}>
            <PrimaryButton
            label={subPageIdx > 0 ? "Previous Section" : "Back"}
            variant="secondary"
            onPress={handleBack}
            />
            <PrimaryButton
            label={
            subPageIdx < italianSubPages.length - 1
              ? "Next Section"
              : (partIdx === totalParts - 1 && pageIdx === totalPagesInPart - 1 ? "Finish Story" : "Next Page")
            }
            onPress={handleNext}
            disabled={isLastSubPage && !isPageComplete()}
            />
            </div>

    </Screen>
  );
};
