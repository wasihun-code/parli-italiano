import React, {useState} from 'react';
import {useNavigate} from 'react-router-dom';

import {PrimaryButton} from '../components/PrimaryButton';
import {Screen} from '../components/Screen';
import {useAuthStore} from '@shared/store/authStore';
import {colors} from '@shared/theme/colors';
import {spacing} from '@shared/theme/spacing';

export const AuthScreen: React.FC = () => {
  const navigate = useNavigate();
  const login = useAuthStore(state => state.login);
  const signup = useAuthStore(state => state.signup);
  const [mode, setMode] = useState<'login' | 'signup'>('login');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string>();

  const submit = (): void => {
    setError(undefined);
    const result =
      mode === 'login'
        ? login(email, password)
        : signup(name, email, password);

    if (result.ok === false) {
      setError((result as { error: string }).error);
      return;
    }

    navigate('/');
  };

  return (
    <Screen style={{ justifyContent: 'center' }}>
      <div
        className="fade-in"
        style={{
          width: '100%',
          maxWidth: 400,
          margin: '0 auto',
          display: 'flex',
          flexDirection: 'column',
          gap: spacing.lg,
          padding: spacing.md,
        }}
      >
        <div style={{ textAlign: 'center', marginBottom: spacing.md }}>
          <div style={{ fontSize: 48, marginBottom: spacing.sm }}>☕</div>
          <h1 style={{color: colors.primary, marginBottom: spacing.xs, fontSize: 32}}>
            {mode === 'login' ? 'Welcome Back' : 'Start Now'}
          </h1>
          <p style={{color: colors.textSecondary, margin: 0, fontSize: 16}}>
            Save your progress and conversation history.
          </p>
        </div>

        <div style={{
          display: 'flex', 
          gap: 4, 
          backgroundColor: 'rgba(78, 52, 46, 0.05)', 
          padding: 4, 
          borderRadius: 16,
          border: `1px solid ${colors.border}`
        }}>
          {(['login', 'signup'] as const).map(item => (
            <button
              key={item}
              onClick={() => {
                setMode(item);
                setError(undefined);
              }}
              style={{
                flex: 1,
                minHeight: 40,
                borderRadius: 12,
                border: 'none',
                backgroundColor: mode === item ? colors.primary : 'transparent',
                color: mode === item ? colors.onPrimary : colors.textSecondary,
                fontWeight: 800,
                fontSize: 14,
                cursor: 'pointer',
                transition: 'all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275)',
                boxShadow: mode === item ? '0 4px 12px rgba(78, 52, 46, 0.2)' : 'none',
              }}
            >
              {item === 'login' ? 'Login' : 'Sign Up'}
            </button>
          ))}
        </div>

        <div style={{display: 'flex', flexDirection: 'column', gap: spacing.md}}>
          {mode === 'signup' && (
            <div style={{ position: 'relative' }}>
              <input
                value={name}
                onChange={event => setName(event.target.value)}
                placeholder="Name"
                style={inputStyle}
              />
            </div>
          )}
          <input
            value={email}
            onChange={event => setEmail(event.target.value)}
            placeholder="Email"
            type="email"
            style={inputStyle}
          />
          <input
            value={password}
            onChange={event => setPassword(event.target.value)}
            onKeyDown={event => event.key === 'Enter' && submit()}
            placeholder="Password"
            type="password"
            style={inputStyle}
          />
        </div>

        {error && (
          <div className="shake" style={{
            color: colors.error, 
            fontWeight: 800, 
            fontSize: 14, 
            textAlign: 'center',
            backgroundColor: 'rgba(158, 42, 43, 0.05)',
            padding: 10,
            borderRadius: 8,
            border: `1px solid ${colors.error}`
          }}>
            {error}
          </div>
        )}

        <PrimaryButton
          label={mode === 'login' ? 'Login' : 'Sign Up'}
          onPress={submit}
          disabled={!email.trim() || !password.trim() || (mode === 'signup' && !name.trim())}
        />
        
        <p style={{ 
          textAlign: 'center', 
          fontSize: 14, 
          color: colors.textSecondary,
          marginTop: spacing.sm
        }}>
          {mode === 'login' ? "Don't have an account?" : "Already have an account?"} {' '}
          <span 
            onClick={() => setMode(mode === 'login' ? 'signup' : 'login')}
            style={{ color: colors.accent, fontWeight: 800, cursor: 'pointer' }}
          >
            {mode === 'login' ? "Sign Up" : "Login"}
          </span>
        </p>
      </div>
    </Screen>
  );
};

const inputStyle: React.CSSProperties = {
  width: '100%',
  minHeight: 52,
  borderRadius: 14,
  border: `2px solid ${colors.border}`,
  backgroundColor: colors.surface,
  padding: `0 ${spacing.md}px`,
  fontSize: 16,
  outline: 'none',
  transition: 'border-color 0.2s, box-shadow 0.2s',
  color: colors.textPrimary,
  boxShadow: '0 2px 4px rgba(0,0,0,0.02)',
};
