import React from 'react';
import { useLocation } from 'react-router-dom';
import { spacing } from '@shared/theme/spacing';
import { Header } from './Header';
import { BottomNav } from './BottomNav';
import { Sidebar } from './Sidebar';

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
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100dvh',
        position: 'relative',
        ...style,
      }}
    >
      <Header />
      <div className="layout-container">
        <main className="layout-main" style={{ 
          padding: isTraining ? '72px 0 0 0' : `72px 0 0 0`,
          paddingBottom: (showNav ? 100 : 0) + spacing.xl,
        }}>
          {children}
        </main>
        {showNav && (
          <aside className="layout-sidebar">
            <Sidebar />
          </aside>
        )}
      </div>
      {showNav && <BottomNav />}
    </div>
  );
};
