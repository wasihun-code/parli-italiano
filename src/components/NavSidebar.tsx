import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

const NAV_ITEMS = [
  { path: '/', label: 'Home', icon: '🏠' },
  { path: '/scenarios', label: 'Scenarios', icon: '🗺️' },
  { path: '/foundations', label: 'Foundations', icon: '🧱' },
  { path: '/review', label: 'Review', icon: '🃏' },
  { path: '/games', label: 'Games', icon: '🎮' },
  { path: '/stories', label: 'Stories', icon: '📖' },
  { path: '/grammar', label: 'Grammar', icon: '📚' },
  { path: '/history', label: 'AI Tutor', icon: '🤖' },
  { path: '/friends', label: 'Friends', icon: '👥' },
];

export const NavSidebar: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
      <div className="card" style={{ padding: spacing.md }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xs }}>
          {NAV_ITEMS.map(item => {
            const active = location.pathname === item.path || (item.path !== '/' && location.pathname.startsWith(item.path));
            return (
              <button
                key={item.path}
                onClick={() => navigate(item.path)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: spacing.md,
                  padding: spacing.md,
                  border: 'none',
                  background: active ? 'rgba(78, 52, 46, 0.08)' : 'transparent',
                  borderRadius: 14,
                  cursor: 'pointer',
                  textAlign: 'left',
                  transition: 'background 0.2s',
                  color: active ? colors.primary : colors.textSecondary,
                }}
                onMouseEnter={e => { if (!active) e.currentTarget.style.backgroundColor = 'rgba(78, 52, 46, 0.05)'; }}
                onMouseLeave={e => { if (!active) e.currentTarget.style.backgroundColor = 'transparent'; }}
              >
                <span style={{ fontSize: 20 }}>{item.icon}</span>
                <span style={{ fontSize: 16, fontWeight: 900 }}>{item.label}</span>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};
