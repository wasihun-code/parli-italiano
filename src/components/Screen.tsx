import React from 'react';
import { useLocation } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { Header } from './Header';
import { BottomNav } from './BottomNav';

interface ScreenProps {
  children: React.ReactNode;
  style?: React.CSSProperties;
}

export const Screen: React.FC<ScreenProps> = ({ children, style }) => {
  const location = useLocation();
  const isTraining = location.pathname.includes('/vocabulary') || 
                    location.pathname.includes('/phrases') || 
                    location.pathname.includes('/sentences') ||
                    location.pathname.includes('/conversation') ||
                    location.pathname.includes('/placement-test') ||
                    location.pathname.includes('/foundations/') ||
                    location.pathname.includes('/stories/');
  
  const showNav = location.pathname !== '/onboarding' && 
                  location.pathname !== '/auth' && 
                  !isTraining;

  return (
    <div
      className="fade-in"
      style={{
        backgroundColor: colors.bg,
        display: 'flex',
        flexDirection: 'column',
        height: '100dvh',
        overflow: 'hidden',
        position: 'relative',
        ...style,
      }}
    >
      <Header />
      <main style={{ 
        flex: 1, 
        overflowY: 'auto',
        width: '100%', 
        maxWidth: 700,
        margin: '0 auto',
        padding: isTraining ? '72px 0 0 0' : `72px ${spacing.md}px ${spacing.md}px ${spacing.md}px`,
        paddingBottom: (showNav ? 100 : 0) + spacing.xl,
        boxSizing: 'border-box',
        display: 'flex',
        flexDirection: 'column',
      }}>
        {children}
      </main>
      {showNav && <BottomNav />}
    </div>
  );
};
