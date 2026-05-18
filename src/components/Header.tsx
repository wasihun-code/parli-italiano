import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useCurrentUser } from '@shared/store/authStore';
import { useProfileStore } from '@shared/store/profileStore';

export const Header: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const currentUser = useCurrentUser();
  const avatar = useProfileStore(state => state.avatar);

  const showBack = location.pathname !== '/' && location.pathname !== '/onboarding' && location.pathname !== '/auth';

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      height: 64,
      backgroundColor: 'rgba(250, 249, 246, 0.95)',
      backdropFilter: 'blur(8px)',
      borderBottom: `1px solid ${colors.border}`,
      display: 'flex',
      alignItems: 'center',
      padding: `0 ${spacing.md}px`,
      zIndex: 1000,
      gap: spacing.md
    }}>
      {showBack && (
        <button
          aria-label="Back"
          onClick={() => navigate(-1)}
          style={{
            background: colors.surface,
            border: `2px solid ${colors.border}`,
            borderRadius: '12px',
            width: 40,
            height: 40,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: colors.primary,
            transition: 'all 0.2s',
            boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
          }}
          onMouseDown={e => e.currentTarget.style.transform = 'scale(0.95)'}
          onMouseUp={e => e.currentTarget.style.transform = 'scale(1)'}
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
        </button>
      )}
      <div style={{ 
        flex: 1, 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: showBack ? 'flex-start' : 'center',
        gap: spacing.sm
      }}>
        <span style={{ fontSize: 24 }}>☕</span>
        <span style={{ 
          fontSize: 20, 
          fontWeight: 900, 
          color: colors.primary,
          letterSpacing: -0.5,
          fontFamily: 'Nunito, sans-serif'
        }}>
          Parla Italiano
        </span>
      </div>
      {currentUser ? (
        <button
          onClick={() => navigate('/profile')}
          title="Profile"
          style={{
            border: `2px solid ${colors.border}`,
            borderRadius: '20px',
            backgroundColor: colors.surface,
            width: 40,
            height: 40,
            fontSize: 20,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer',
            transition: 'all 0.2s',
            boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
          }}
          onMouseEnter={e => {
            e.currentTarget.style.borderColor = colors.accent;
            e.currentTarget.style.transform = 'scale(1.05)';
          }}
          onMouseLeave={e => {
            e.currentTarget.style.borderColor = colors.border;
            e.currentTarget.style.transform = 'scale(1)';
          }}
        >
          {avatar}
        </button>
      ) : (
        <div style={{ width: 40 }} />
      )}
    </div>
  );
};
