import React from 'react';
import { useNavigate } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useProgressStore } from '@shared/store/progressStore';
import { useSubscriptionStore } from '@shared/store/subscriptionStore';
import { PrimaryButton } from './PrimaryButton';

export const Sidebar: React.FC = () => {
  const { xp, streak } = useProgressStore();
  const { plan } = useSubscriptionStore();
  const navigate = useNavigate();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
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
        <div style={{ display: 'flex', alignItems: 'center', gap: spacing.xs }}>
          <span style={{ fontSize: 32 }}>🔥</span>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{ fontWeight: 900, color: colors.primary, fontSize: 24, lineHeight: 1 }}>{streak || 0}</span>
            <span style={{ fontSize: 12, color: colors.textSecondary, fontWeight: 800, textTransform: 'uppercase' }}>Streak</span>
          </div>
        </div>
        <div style={{ height: 40, width: 2, backgroundColor: colors.border }}></div>
        <div style={{ display: 'flex', alignItems: 'center', gap: spacing.xs }}>
          <span style={{ fontSize: 32 }}>⚡</span>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{ fontWeight: 900, color: colors.primary, fontSize: 24, lineHeight: 1 }}>{xp || 0}</span>
            <span style={{ fontSize: 12, color: colors.textSecondary, fontWeight: 800, textTransform: 'uppercase' }}>Total XP</span>
          </div>
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
