import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

const NAV_ITEMS = [
  { 
    path: '/', 
    label: 'Home', 
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
        <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>
      </svg>
    )
  },
  { 
    path: '/scenarios', 
    label: 'Scenarios', 
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
        <polygon points="12 2 2 7 12 12 22 7 12 2"/>
        <polyline points="2 17 12 22 22 17"/>
        <polyline points="2 12 12 17 22 12"/>
      </svg>
    )
  },
  { 
    path: '/review', 
    label: 'Review', 
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
        <path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/>
        <polyline points="21 3 21 8 16 8"/>
      </svg>
    )
  },
  { 
    path: '/history', 
    label: 'Chats', 
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
      </svg>
    )
  },
  { 
    path: '/foundations', 
    label: 'Foundations', 
    icon: (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
      </svg>
    )
  },
];

export const BottomNav: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <nav className="mobile-only" style={{
      position: 'fixed',
      bottom: 0,
      left: 0,
      right: 0,
      width: '100%',
      maxWidth: 900,
      margin: '0 auto',
      height: 80,
      backgroundColor: colors.surface,
      borderTop: `2px solid ${colors.border}`,
      display: 'flex',
      justifyContent: 'space-around',
      alignItems: 'center',
      zIndex: 1000,
      paddingBottom: 'env(safe-area-inset-bottom)',
      paddingTop: 8,
    }}>
      {NAV_ITEMS.map(item => {
        const active = location.pathname === item.path || 
                      (item.path !== '/' && location.pathname.startsWith(item.path));
        return (
          <button
            key={item.path}
            onClick={() => navigate(item.path)}
            style={{
              background: 'none',
              border: 'none',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: 6,
              color: active ? colors.primary : colors.textSecondary,
              cursor: 'pointer',
              transition: 'all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275)',
              padding: `${spacing.xs}px ${spacing.sm}px`,
              borderRadius: '16px',
              backgroundColor: active ? 'rgba(78, 52, 46, 0.08)' : 'transparent',
              transform: active ? 'translateY(-4px)' : 'translateY(0)',
            }}
          >
            <div style={{ 
              transform: active ? 'scale(1.1)' : 'scale(1)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}>
              {item.icon}
            </div>
            <span style={{ 
              fontSize: 12, 
              fontWeight: 900, 
              textTransform: 'uppercase',
              letterSpacing: 0.5,
              opacity: active ? 1 : 0.8
            }}>
              {item.label}
            </span>
          </button>
        );
      })}
    </nav>
  );
};
