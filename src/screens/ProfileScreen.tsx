import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Screen } from '../components/Screen';
import { PrimaryButton } from '../components/PrimaryButton';
import { useAuthStore, useCurrentUser } from '@shared/store/authStore';
import { useProfileStore } from '@shared/store/profileStore';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

const AVATARS = ['👤', '👨‍🎓', '👩‍🎓', '🍕', '☕', '🏛️'];

export const ProfileScreen: React.FC = () => {
  const navigate = useNavigate();
  const currentUser = useCurrentUser();
  const logout = useAuthStore(state => state.logout);
  const { name, email, avatar, updateProfile, resetAllProgress } = useProfileStore();

  const [editName, setEditName] = useState(name);
  const [editEmail, setEditEmail] = useState(email);
  const [showResetConfirm, setShowResetConfirm] = useState(false);

  // Sync with auth user on first load if profile is default
  useEffect(() => {
    if (currentUser && name === 'Learner') {
      updateProfile({ name: currentUser.name, email: currentUser.email });
      setEditName(currentUser.name);
      setEditEmail(currentUser.email);
    }
  }, [currentUser, name, updateProfile]);

  const handleSave = () => {
    updateProfile({ name: editName, email: editEmail });
    alert('Profile saved!');
  };

  const handleReset = () => {
    resetAllProgress();
    setShowResetConfirm(false);
    alert('All progress has been reset.');
  };

  const handleLogout = () => {
    logout();
    navigate('/auth');
  };

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.lg }}>
        <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Profile</h1>
      </header>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xl, paddingBottom: 100 }}>
        
        {/* Avatar Selection */}
        <div className="card" style={{ padding: spacing.lg }}>
          <h2 style={{ fontSize: 18, color: colors.textSecondary, marginBottom: spacing.md, marginTop: 0 }}>Avatar</h2>
          <div style={{ display: 'flex', gap: spacing.md, flexWrap: 'wrap' }}>
            {AVATARS.map(a => (
              <button
                key={a}
                onClick={() => updateProfile({ avatar: a })}
                style={{
                  fontSize: 32,
                  width: 60,
                  height: 60,
                  borderRadius: 30,
                  border: `2px solid ${avatar === a ? colors.primary : 'transparent'}`,
                  backgroundColor: avatar === a ? 'rgba(78, 52, 46, 0.1)' : colors.bg,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  transition: 'all 0.2s',
                }}
              >
                {a}
              </button>
            ))}
          </div>
        </div>

        {/* Profile Details */}
        <div className="card" style={{ padding: spacing.lg, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h2 style={{ fontSize: 18, color: colors.textSecondary, margin: 0 }}>Details</h2>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
            <label style={{ fontSize: 14, fontWeight: 'bold', color: colors.primary }}>Display Name</label>
            <input
              type="text"
              value={editName}
              onChange={e => setEditName(e.target.value)}
              style={{
                padding: spacing.md,
                borderRadius: 12,
                border: `2px solid ${colors.border}`,
                fontSize: 16,
                backgroundColor: colors.bg,
              }}
            />
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
            <label style={{ fontSize: 14, fontWeight: 'bold', color: colors.primary }}>Email</label>
            <input
              type="email"
              value={editEmail}
              onChange={e => setEditEmail(e.target.value)}
              style={{
                padding: spacing.md,
                borderRadius: 12,
                border: `2px solid ${colors.border}`,
                fontSize: 16,
                backgroundColor: colors.bg,
              }}
            />
          </div>

          <PrimaryButton label="Save Changes" onPress={handleSave} />
        </div>

        {/* Settings */}
        <div className="card" style={{ padding: spacing.lg, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h2 style={{ fontSize: 18, color: colors.textSecondary, margin: 0 }}>Settings</h2>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 16, fontWeight: 'bold', color: colors.primary }}>Sound Effects</span>
            <button 
              onClick={useUserSettingsStore.getState().toggleSound}
              style={{
                width: 60, height: 32, borderRadius: 16, 
                backgroundColor: useUserSettingsStore(s => s.soundEnabled) ? colors.success : colors.border,
                border: 'none', position: 'relative', cursor: 'pointer',
                transition: 'background-color 0.2s'
              }}
            >
              <div style={{
                width: 24, height: 24, borderRadius: 12, backgroundColor: '#fff',
                position: 'absolute', top: 4, 
                left: useUserSettingsStore(s => s.soundEnabled) ? 32 : 4,
                transition: 'left 0.2s'
              }} />
            </button>
          </div>
        </div>

        {/* Navigation */}
        <div className="card" style={{ padding: spacing.lg, display: 'flex', flexDirection: 'column', gap: spacing.md }}>
          <h2 style={{ fontSize: 18, color: colors.textSecondary, margin: 0 }}>Progress</h2>
          <PrimaryButton label="View Words Learned" onPress={() => navigate('/mastered')} variant="primary" />
        </div>

        {/* Danger Zone */}
        <div className="card" style={{ padding: spacing.lg, border: `2px solid ${colors.error}33` }}>
          <h2 style={{ fontSize: 18, color: colors.error, marginTop: 0 }}>Danger Zone</h2>
          {!showResetConfirm ? (
            <PrimaryButton 
              label="Reset All Progress" 
              onPress={() => setShowResetConfirm(true)} 
              variant="secondary"
            />
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
              <p style={{ color: colors.error, fontWeight: 'bold', margin: 0 }}>Are you absolutely sure? This cannot be undone.</p>
              <div style={{ display: 'flex', gap: spacing.md }}>
                <button 
                  onClick={handleReset}
                  style={{ flex: 1, padding: spacing.md, borderRadius: 12, backgroundColor: colors.error, color: 'white', border: 'none', fontWeight: 800, cursor: 'pointer' }}
                >
                  Yes, Reset Everything
                </button>
                <button 
                  onClick={() => setShowResetConfirm(false)}
                  style={{ flex: 1, padding: spacing.md, borderRadius: 12, backgroundColor: colors.border, color: colors.primary, border: 'none', fontWeight: 800, cursor: 'pointer' }}
                >
                  Cancel
                </button>
              </div>
            </div>
          )}
          
          <div style={{ marginTop: spacing.xl }}>
            <button 
              onClick={handleLogout}
              style={{ width: '100%', padding: spacing.md, borderRadius: 12, backgroundColor: 'transparent', color: colors.error, border: `2px solid ${colors.error}`, fontWeight: 800, cursor: 'pointer' }}
            >
              Log Out
            </button>
          </div>
        </div>
      </div>
    </Screen>
  );
};
