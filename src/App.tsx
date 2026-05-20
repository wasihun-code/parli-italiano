import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route, useNavigate, useLocation } from 'react-router-dom';
import { HomeScreen } from './screens/HomeScreen';
import { FoundationsScreen } from './screens/FoundationsScreen';
import { FoundationLessonScreen } from './screens/FoundationLessonScreen';
import { ScenarioSelectionScreen } from './screens/ScenarioSelectionScreen';
import { VocabularyTrainingScreen } from './screens/VocabularyTrainingScreen';
import { PhraseTrainingScreen } from './screens/PhraseTrainingScreen';
import { SentenceTrainingScreen } from './screens/SentenceTrainingScreen';
import { ConversationScreen } from './screens/ConversationScreen';
import { ReviewScreen } from './screens/ReviewScreen';
import { ConversationHistoryScreen } from './screens/ConversationHistoryScreen';
import { OnboardingScreen } from './screens/OnboardingScreen';
import { PlacementTestScreen } from './screens/PlacementTestScreen';
import { AuthScreen } from './screens/AuthScreen';
import { ProfileScreen } from './screens/ProfileScreen';
import { MasteredScreen } from './screens/MasteredScreen';
import { GrammarListScreen } from './screens/GrammarListScreen';
import { GrammarLessonScreen } from './screens/GrammarLessonScreen';
import { GamesScreen } from './screens/GamesScreen';
import { GenderGame } from './screens/GenderGame';
import { TranslationGame } from './screens/TranslationGame';
import { PrepositionGame } from './screens/PrepositionGame';
import { IdiomsGame } from './screens/IdiomsGame';
import { OppositesGame } from './screens/OppositesGame';
import { NumbersGame } from './screens/NumbersGame';
import { StoriesScreen } from './screens/StoriesScreen';
import { StoryReaderScreen } from './screens/StoryReaderScreen';
import { StoryFinalQuizScreen } from './screens/StoryFinalQuizScreen';
import { useCurrentUser } from '@shared/store/authStore';
import { FooterNav } from './components/FooterNav';

const OnboardingGuard: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const navigate = useNavigate();
  const location = useLocation();
  
  useEffect(() => {
    const hasSeen = localStorage.getItem('hasSeenOnboarding');
    if (!hasSeen && location.pathname !== '/onboarding' && location.pathname !== '/auth') {
      navigate('/onboarding');
    }
  }, [navigate, location]);

  return <>{children}</>;
};

const AuthGuard: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const currentUser = useCurrentUser();

  useEffect(() => {
    if (!currentUser && location.pathname !== '/auth') {
      navigate('/auth');
      return;
    }
    if (currentUser && location.pathname === '/auth') {
      navigate('/');
    }
  }, [currentUser, location.pathname, navigate]);

  return <>{children}</>;
};

export const App: React.FC = () => {
  return (
    <BrowserRouter>
      <AuthGuard>
        <OnboardingGuard>
          <Routes>
            <Route path="/auth" element={<AuthScreen />} />
            <Route path="/profile" element={<ProfileScreen />} />
            <Route path="/mastered" element={<MasteredScreen />} />
            <Route path="/grammar" element={<GrammarListScreen />} />
            <Route path="/grammar/:lessonId" element={<GrammarLessonScreen />} />
            <Route path="/games" element={<GamesScreen />} />
            <Route path="/games/gender" element={<GenderGame />} />
            <Route path="/games/translation" element={<TranslationGame />} />
            <Route path="/games/prepositions" element={<PrepositionGame />} />
            <Route path="/games/idioms" element={<IdiomsGame />} />
            <Route path="/games/opposites" element={<OppositesGame />} />
            <Route path="/games/numbers" element={<NumbersGame />} />
            <Route path="/stories" element={<StoriesScreen />} />
            <Route path="/stories/:storyId" element={<StoryReaderScreen />} />
            <Route path="/stories/:storyId/quiz" element={<StoryFinalQuizScreen />} />
            <Route path="/" element={<HomeScreen />} />
            <Route path="/onboarding" element={<OnboardingScreen />} />
            <Route path="/placement-test" element={<PlacementTestScreen />} />
            <Route path="/foundations" element={<FoundationsScreen />} />
            <Route path="/foundations/:lessonId" element={<FoundationLessonScreen />} />
            <Route path="/scenarios" element={<ScenarioSelectionScreen />} />
            <Route path="/scenarios/:scenarioId/vocabulary" element={<VocabularyTrainingScreen />} />
            <Route path="/scenarios/:scenarioId/phrases" element={<PhraseTrainingScreen />} />
            <Route path="/scenarios/:scenarioId/sentences" element={<SentenceTrainingScreen />} />
            <Route path="/scenarios/:scenarioId/conversation" element={<ConversationScreen />} />
            <Route path="/review" element={<ReviewScreen />} />
            <Route path="/history" element={<ConversationHistoryScreen />} />
          </Routes>
          <FooterNav />
        </OnboardingGuard>
      </AuthGuard>
    </BrowserRouter>
  );
};
