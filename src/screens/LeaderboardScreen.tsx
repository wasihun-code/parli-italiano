import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';
import { apiClient } from '../lib/apiClient';

export const LeaderboardScreen: React.FC = () => {
  const navigate = useNavigate();
  const [users, setUsers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    apiClient.getLeaderboard()
      .then(data => {
        setUsers(data);
        setError(false);
      })
      .catch(() => {
        setError(true);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <Screen style={{ backgroundColor: colors.bg }}>
      <div style={{ maxWidth: 600, margin: '0 auto', width: '100%' }}>
        <header style={{ marginBottom: spacing.xl }}>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Classifica 🏆</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18 }}>I migliori studenti della settimana</p>
        </header>

        {loading ? (
          <div style={{ textAlign: 'center', padding: spacing.xl }}>Caricamento classifica...</div>
        ) : error ? (
          <div className="card" style={{ padding: spacing.xl, textAlign: 'center' }}>
            <div style={{ fontSize: 48, marginBottom: spacing.md }}>🔌</div>
            <h3 style={{ color: colors.error, marginBottom: spacing.sm }}>Connessione Fallita</h3>
            <p style={{ color: colors.textSecondary }}>Non è stato possibile caricare la classifica. Assicurati che il server sia attivo.</p>
            <PrimaryButton label="Riprova" onPress={() => window.location.reload()} style={{ marginTop: spacing.md }} />
          </div>
        ) : users.length === 0 ? (
          <div className="card" style={{ padding: spacing.xl, textAlign: 'center' }}>
             <div style={{ fontSize: 48, marginBottom: spacing.md }}>🏆</div>
             <p style={{ color: colors.textSecondary }}>Sii il primo a scalare la classifica! Inizia ad imparare per guadagnare XP.</p>
          </div>
        ) : (
          <div className="card" style={{ padding: 0, overflow: 'hidden' }}>
            {users.map((user, idx) => (
              <div key={user.id} style={{ 
                display: 'flex', 
                justifyContent: 'space-between', 
                alignItems: 'center', 
                padding: '20px 24px', 
                borderBottom: idx < users.length - 1 ? `1px solid ${colors.border}` : 'none',
                backgroundColor: idx === 0 ? 'rgba(212, 163, 115, 0.1)' : 'transparent'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md }}>
                  <div style={{ 
                    width: 32, 
                    height: 32, 
                    borderRadius: 16, 
                    backgroundColor: idx === 0 ? colors.accent : idx === 1 ? '#C0C0C0' : idx === 2 ? '#CD7F32' : colors.chipBg,
                    color: idx < 3 ? 'white' : colors.textSecondary,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 900,
                    fontSize: 14
                  }}>
                    {idx + 1}
                  </div>
                  <span style={{ fontWeight: 800, color: colors.primary, fontSize: 18 }}>{user.username}</span>
                </div>
                <div style={{ fontWeight: 900, color: colors.primary }}>{user.total_xp} XP</div>
              </div>
            ))}
          </div>
        )}

        <div style={{ marginTop: spacing.xl, marginBottom: spacing.xxl }}>
          <PrimaryButton label="Torna alla Home" onPress={() => navigate('/')} variant="secondary" />
        </div>
      </div>
    </Screen>
  );
};
