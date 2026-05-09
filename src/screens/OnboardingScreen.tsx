import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

const SLIDES = [
  {
    title: 'Welcome to Parla Italiano',
    description: 'The offline app to master Italian conversation at A1 level.',
    icon: '☕',
    color: colors.primary
  },
  {
    title: 'The Foundations',
    description: 'Learn essential grammar and verbs in 5 lessons to unlock scenarios.',
    icon: '🎓',
    color: colors.secondary
  },
  {
    title: 'Real-Life Situations',
    description: 'Practice in over 100 scenarios, from ordering a coffee to travel emergencies.',
    icon: '🇮🇹',
    color: colors.accent
  }
];

export const OnboardingScreen: React.FC = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  const navigate = useNavigate();

  const next = () => {
    if (currentSlide === SLIDES.length - 1) {
      localStorage.setItem('hasSeenOnboarding', 'true');
      navigate('/');
      return;
    }
    setCurrentSlide(s => s + 1);
  };

  const slide = SLIDES[currentSlide];

  return (
    <Screen style={{ justifyContent: 'center', textAlign: 'center' }}>
      <div className="fade-in" key={currentSlide} style={{
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        gap: spacing.lg,
        padding: spacing.xl
      }}>
        <div style={{ 
          width: 140, 
          height: 140, 
          borderRadius: 40, 
          backgroundColor: colors.surface,
          border: `4px solid ${slide.color}`,
          margin: '0 auto',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 64,
          boxShadow: `0 10px 30px rgba(0,0,0,0.08)`,
          transform: 'rotate(-5deg)'
        }}>
          {slide.icon}
        </div>
        
        <div style={{ marginTop: spacing.md }}>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, marginBottom: spacing.sm }}>{slide.title}</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, lineHeight: '1.6', maxWidth: 400, margin: '0 auto' }}>{slide.description}</p>
        </div>
        
        <div style={{ display: 'flex', gap: 10, justifyContent: 'center', marginTop: spacing.lg }}>
          {SLIDES.map((_, i) => (
            <div key={i} style={{
              width: i === currentSlide ? 24 : 8,
              height: 8,
              borderRadius: 4,
              backgroundColor: i === currentSlide ? slide.color : colors.border,
              transition: 'all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)'
            }} />
          ))}
        </div>
      </div>
      
      <div style={{ padding: spacing.xl, maxWidth: 400, width: '100%', margin: '0 auto' }}>
        <PrimaryButton 
          label={currentSlide === SLIDES.length - 1 ? 'Start Learning' : 'Next'} 
          onPress={next} 
          variant={currentSlide === SLIDES.length - 1 ? 'primary' : 'secondary'}
        />
        {currentSlide < SLIDES.length - 1 && (
          <button 
            onClick={() => {
              localStorage.setItem('hasSeenOnboarding', 'true');
              navigate('/');
            }}
            style={{
              background: 'none',
              border: 'none',
              color: colors.textSecondary,
              fontSize: 14,
              fontWeight: 700,
              marginTop: spacing.md,
              cursor: 'pointer',
              textDecoration: 'underline'
            }}
          >
            Skip Intro
          </button>
        )}
      </div>
    </Screen>
  );
};
