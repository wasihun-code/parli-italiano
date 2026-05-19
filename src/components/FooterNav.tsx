import React, { useState, useEffect, useRef } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

const NAV_ITEMS = [
  { label: 'Grammar', path: '/grammar', icon: '📚' },
  { label: 'Review', path: '/review', icon: '🃏' },
  { label: 'Games', path: '/games', icon: '🎮' },
];

export const FooterNav: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Hide on training screens and auth/onboarding
  const hideOn = ['/vocabulary', '/phrases', '/sentences', '/auth', '/onboarding', '/placement-test'];
  const shouldHide = hideOn.some(path => location.pathname.includes(path));

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  if (shouldHide) return null;

  return (
    <div style={{
      position: 'fixed',
      bottom: spacing.lg,
      right: spacing.lg,
      zIndex: 2000,
    }} ref={dropdownRef}>
      {isOpen && (
        <div className="card fade-in" style={{
          position: 'absolute',
          bottom: '100%',
          right: 0,
          marginBottom: spacing.md,
          width: 180,
          padding: spacing.xs,
          display: 'flex',
          flexDirection: 'column',
          gap: 4,
          boxShadow: '0 8px 24px rgba(0,0,0,0.15)',
          border: `1px solid ${colors.border}`,
          borderRadius: 20,
          backgroundColor: colors.surface,
        }}>
          {NAV_ITEMS.map(item => (
            <button
              key={item.path}
              onClick={() => {
                navigate(item.path);
                setIsOpen(false);
              }}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: spacing.sm,
                padding: `${spacing.sm}px ${spacing.md}px`,
                border: 'none',
                background: location.pathname === item.path ? 'rgba(78, 52, 46, 0.08)' : 'transparent',
                borderRadius: 14,
                cursor: 'pointer',
                textAlign: 'left',
                transition: 'background 0.2s',
              }}
              onMouseEnter={e => e.currentTarget.style.backgroundColor = 'rgba(78, 52, 46, 0.05)'}
              onMouseLeave={e => e.currentTarget.style.backgroundColor = location.pathname === item.path ? 'rgba(78, 52, 46, 0.08)' : 'transparent'}
            >
              <span style={{ fontSize: 18 }}>{item.icon}</span>
              <span style={{ 
                fontSize: 15, 
                fontWeight: 800, 
                color: colors.primary,
              }}>
                {item.label}
              </span>
            </button>
          ))}
        </div>
      )}
      <button
        onClick={() => setIsOpen(!isOpen)}
        style={{
          width: 56,
          height: 56,
          borderRadius: 28,
          backgroundColor: colors.primary,
          color: colors.onPrimary,
          border: 'none',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 4px 12px rgba(78, 52, 46, 0.3)',
          transition: 'all 0.2s',
          transform: isOpen ? 'rotate(45deg)' : 'rotate(0deg)',
        }}
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
          <line x1="12" y1="5" x2="12" y2="19"></line>
          <line x1="5" y1="12" x2="19" y2="12"></line>
        </svg>
      </button>
    </div>
  );
};
