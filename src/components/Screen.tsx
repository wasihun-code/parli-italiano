import React from 'react';
import { useLocation } from 'react-router-dom';
import { Header } from './Header';
import { Sidebar } from './Sidebar';
import { NavSidebar } from './NavSidebar';
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
                    location.pathname.startsWith('/stories/'); // Keep list for reader, but not main stories list
  
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
      <div className={`layout-container ${showNav ? 'with-sidebars' : 'no-sidebars'}`}>
        {showNav && (
          <aside className="layout-nav-sidebar">
            <NavSidebar />
          </aside>
        )}
        <main className={`layout-main ${isTraining ? 'training-mode' : ''}`}>
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
