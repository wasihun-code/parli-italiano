import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useProgressStore } from '@shared/store/progressStore';
import { useSubscriptionStore } from '@shared/store/subscriptionStore';
import { PrimaryButton } from './PrimaryButton';

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

export const Sidebar: React.FC = () => {
  const { xp, streak } = useProgressStore();
  const { plan } = useSubscriptionStore();
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
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

      {plan === 'free' && (
        <div className="card" style={{ padding: spacing.lg, background: `linear-gradient(135deg, ${colors.primary} 0%, ${colors.accent} 100%)`, border: 'none' }}>
          <h3 style={{ color: colors.onPrimary, marginBottom: spacing.sm, fontSize: 18 }}>Go Premium!</h3>
          <p style={{ color: colors.onPrimary, opacity: 0.9, fontSize: 14, marginBottom: spacing.md }}>
            Unlock all stories, grammar lessons, and offline mode.
          </p>
          <PrimaryButton 
            label="Upgrade" 
            onPress={() => navigate('/premium')}
            variant="accent"
            style={{ fontSize: 14, padding: spacing.sm }}
          />
        </div>
      )}

      <div className="card" style={{ padding: spacing.lg, display: 'flex', justifyContent: 'space-around', alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <span style={{ fontSize: 24 }}>🔥</span>
          <span style={{ fontWeight: 900, color: colors.primary }}>{streak || 0}</span>
          <span style={{ fontSize: 12, color: colors.textSecondary }}>Streak</span>
        </div>
        <div style={{ height: 40, width: 2, backgroundColor: colors.border }}></div>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <span style={{ fontSize: 24 }}>⚡</span>
          <span style={{ fontWeight: 900, color: colors.primary }}>{xp || 0}</span>
          <span style={{ fontSize: 12, color: colors.textSecondary }}>Total XP</span>
        </div>
      </div>

      <div className="card" style={{ padding: spacing.lg }}>
        <h3 style={{ marginBottom: spacing.md, color: colors.primary }}>Daily Quests</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <div style={{ display: 'flex', gap: spacing.sm, alignItems: 'center' }}>
            <div style={{ width: 40, height: 40, borderRadius: 20, backgroundColor: 'rgba(212, 163, 115, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 20 }}>📚</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 'bold', fontSize: 14, color: colors.primary }}>Complete 2 scenarios</div>
              <div style={{ width: '100%', height: 8, backgroundColor: colors.border, borderRadius: 4, marginTop: 4 }}>
                <div style={{ width: '50%', height: '100%', backgroundColor: colors.accent, borderRadius: 4 }}></div>
              </div>
            </div>
          </div>
          <div style={{ display: 'flex', gap: spacing.sm, alignItems: 'center' }}>
            <div style={{ width: 40, height: 40, borderRadius: 20, backgroundColor: 'rgba(56, 102, 65, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 20 }}>🎯</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 'bold', fontSize: 14, color: colors.primary }}>Earn 50 XP</div>
              <div style={{ width: '100%', height: 8, backgroundColor: colors.border, borderRadius: 4, marginTop: 4 }}>
                <div style={{ width: '20%', height: '100%', backgroundColor: colors.success, borderRadius: 4 }}></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="card" style={{ padding: spacing.lg }}>
        <h3 style={{ marginBottom: spacing.md, color: colors.primary }}>Leaderboard</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0', borderBottom: `1px solid ${colors.border}` }}>
            <span style={{ fontWeight: 'bold', color: colors.primary }}>1. Marco</span>
            <span style={{ color: colors.textSecondary, fontSize: 14 }}>1200 XP</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0', borderBottom: `1px solid ${colors.border}` }}>
            <span style={{ fontWeight: 'bold', color: colors.primary }}>2. You</span>
            <span style={{ color: colors.textSecondary, fontSize: 14 }}>{xp || 0} XP</span>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0' }}>
            <span style={{ fontWeight: 'bold', color: colors.primary }}>3. Giulia</span>
            <span style={{ color: colors.textSecondary, fontSize: 14 }}>850 XP</span>
          </div>
        </div>
      </div>
    </div>
  );
};
