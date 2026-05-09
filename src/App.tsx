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
import { useCurrentUser } from '@shared/store/authStore';

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
        </OnboardingGuard>
      </AuthGuard>
    </BrowserRouter>
  );
};
