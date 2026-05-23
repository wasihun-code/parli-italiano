import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { useProgressStore } from '@shared/store/progressStore';
import { useSubscriptionStore } from '@shared/store/subscriptionStore';
import { PrimaryButton } from './PrimaryButton';
import { apiClient } from '../lib/apiClient';

export const Sidebar: React.FC = () => {
  const { xp, streak } = useProgressStore();
  const { plan } = useSubscriptionStore();
  const navigate = useNavigate();
  const [leaderboard, setLeaderboard] = useState<any[]>([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    apiClient.getLeaderboard()
      .then(data => {
        setLeaderboard(data.slice(0, 3));
        setError(false);
      })
      .catch(() => {
        setError(true);
      });
  }, []);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl }}>
      {plan === 'free' && (
        <div className="card" style={{ padding: spacing.lg, background: `linear-gradient(135deg, ${colors.primary} 0%, ${colors.accent} 100%)`, border: 'none' }}>
          <h3 style={{ color: colors.onPrimary, marginBottom: spacing.sm, fontSize: 18 }}>Passa a Premium!</h3>
          <p style={{ color: colors.onPrimary, opacity: 0.9, fontSize: 14, marginBottom: spacing.md }}>
            Sblocca tutte le storie, lezioni di grammatica e la modalità offline.
          </p>
          <PrimaryButton 
            label="Migliora Ora" 
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
            <span style={{ fontSize: 12, color: colors.textSecondary, fontWeight: 800, textTransform: 'uppercase' }}>XP Totale</span>
          </div>
        </div>
      </div>

      <div className="card" style={{ padding: spacing.lg }}>
        <h3 style={{ marginBottom: spacing.md, color: colors.primary }}>Missioni Giornaliere</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <div style={{ display: 'flex', gap: spacing.sm, alignItems: 'center' }}>
            <div style={{ width: 40, height: 40, borderRadius: 20, backgroundColor: 'rgba(212, 163, 115, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 20 }}>📚</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 'bold', fontSize: 14, color: colors.primary }}>Completa 2 scenari</div>
              <div style={{ width: '100%', height: 8, backgroundColor: colors.border, borderRadius: 4, marginTop: 4 }}>
                <div style={{ width: '50%', height: '100%', backgroundColor: colors.accent, borderRadius: 4 }}></div>
              </div>
            </div>
          </div>
          <div style={{ display: 'flex', gap: spacing.sm, alignItems: 'center' }}>
            <div style={{ width: 40, height: 40, borderRadius: 20, backgroundColor: 'rgba(56, 102, 65, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 20 }}>🎯</div>
            <div style={{ flex: 1 }}>
              <div style={{ fontWeight: 'bold', fontSize: 14, color: colors.primary }}>Guadagna 50 XP</div>
              <div style={{ width: '100%', height: 8, backgroundColor: colors.border, borderRadius: 4, marginTop: 4 }}>
                <div style={{ width: '20%', height: '100%', backgroundColor: colors.success, borderRadius: 4 }}></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="card" style={{ padding: spacing.lg }}>
        <h3 style={{ marginBottom: spacing.md, color: colors.primary }}>Classifica</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.sm }}>
          {error ? (
            <div style={{ fontSize: 14, color: colors.error }}>Servizio momentaneamente non disponibile</div>
          ) : leaderboard.length > 0 ? leaderboard.map((user, idx) => (
            <div key={user.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 0', borderBottom: idx < leaderboard.length - 1 ? `1px solid ${colors.border}` : 'none' }}>
              <span style={{ fontWeight: 'bold', color: colors.primary }}>{idx + 1}. {user.username}</span>
              <span style={{ color: colors.textSecondary, fontSize: 14 }}>{user.total_xp} XP</span>
            </div>
          )) : (
            <div style={{ fontSize: 14, color: colors.textSecondary }}>Nessun dato disponibile</div>
          )}
          {!error && (
            <button 
              onClick={() => navigate('/leaderboard')}
              style={{ 
                background: 'none', 
                border: 'none', 
                color: colors.accent, 
                fontWeight: 800, 
                fontSize: 12, 
                marginTop: spacing.sm, 
                cursor: 'pointer',
                textAlign: 'left'
              }}
            >
              VEDI TUTTA LA CLASSIFICA
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
