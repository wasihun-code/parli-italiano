import React, { useMemo, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Tts } from '../lib/tts';
import { PrimaryButton } from '../components/PrimaryButton';
import { Screen } from '../components/Screen';
import { useSrsStore } from '@shared/store/srsStore';
import { useUserSettingsStore } from '../store/userSettingsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

export const ReviewScreen: React.FC = () => {
  const navigate = useNavigate();
  const items = useSrsStore(state => state.items);
  const { flashcardDirection } = useUserSettingsStore();
  const isItFirst = flashcardDirection === 'it-en';

  const [activeTab, setActiveTab] = useState<'all' | 'vocabulary' | 'phrase' | 'sentence'>('all');
  const [showOnlyDue, setShowOnlyDue] = useState(true);

  const filteredItems = useMemo(() => {
    const now = new Date();
    return Object.values(items).filter(item => {
      const typeMatch = activeTab === 'all' || item.type === activeTab;
      const dueMatch = !showOnlyDue || new Date(item.dueAt) <= now;
      return typeMatch && dueMatch && item.learned;
    });
  }, [items, activeTab, showOnlyDue]);

  const recordAnswer = useSrsStore(state => state.recordAnswer);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  
  const stats = useMemo(() => {
    const now = new Date();
    const all = Object.values(items);
    return {
      total: all.length,
      learned: all.filter(i => i.learned).length,
      due: all.filter(i => i.learned && new Date(i.dueAt) <= now).length
    };
  }, [items]);
  
  const currentItem = filteredItems[currentIndex] ?? filteredItems[0];

  const playAudio = (): void => {
    if (currentItem) {
      void Tts.speak(currentItem.italian, currentItem.audio);
    }
  };

  const answerCard = (correct: boolean): void => {
    if (!currentItem) return;

    recordAnswer(currentItem.id, correct);
    setCurrentIndex(index => (index + 1) % Math.max(1, filteredItems.length));
    setRevealed(false);
  };

  if (!currentItem) {
    return (
      <Screen style={{ justifyContent: 'center' }}>
        <div className="card fade-in" style={{
          textAlign: 'center',
          padding: spacing.xl,
          display: 'flex',
          flexDirection: 'column',
          gap: spacing.lg,
          cursor: 'default'
        }}>
          <div style={{ fontSize: 64 }}>☕</div>
          <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Ripasso completato</h1>
          <p style={{ color: colors.textSecondary, fontSize: 18, margin: 0 }}>
            {showOnlyDue ? 'Niente da ripassare al momento - torna più tardi!' : 'Non ci sono elementi in questa categoria.'}
          </p>
          {showOnlyDue && (
            <PrimaryButton 
              label="Ripassa tutto il vocabolario" 
              onPress={() => {
                setShowOnlyDue(false);
                setActiveTab('all');
              }} 
              variant="secondary"
            />
          )}
          <div style={{ 
            backgroundColor: colors.chipBg, 
            padding: spacing.md, 
            borderRadius: 16,
            fontSize: 14,
            fontWeight: 800,
            color: colors.primary
          }}>
            {stats.learned} imparati / {stats.total} totali
          </div>
          <PrimaryButton label="Torna alla Home" onPress={() => navigate('/')} />
        </div>
      </Screen>
    );
  }

  return (
    <Screen>
      <header style={{ marginBottom: spacing.lg }}>
        <h1 style={{ color: colors.primary, fontSize: 32, fontWeight: 900, margin: 0 }}>Ripassa 🔁</h1>
        <p style={{ color: colors.textSecondary, fontSize: 16, marginTop: spacing.xxs, fontWeight: 700 }}>
          {stats.due} in scadenza • {stats.learned} imparati
        </p>
      </header>

      {/* Tabs */}
      <div style={{ 
        display: 'flex', 
        gap: spacing.sm, 
        marginBottom: spacing.md,
        overflowX: 'auto',
        paddingBottom: 4
      }}>
        {(['all', 'vocabulary', 'phrase', 'sentence'] as const).map(tab => (
          <button
            key={tab}
            onClick={() => {
              setActiveTab(tab);
              setCurrentIndex(0);
              setRevealed(false);
            }}
            style={{
              padding: '8px 16px',
              borderRadius: 20,
              border: 'none',
              backgroundColor: activeTab === tab ? colors.primary : colors.chipBg,
              color: activeTab === tab ? colors.onPrimary : colors.textSecondary,
              fontWeight: 800,
              fontSize: 12,
              textTransform: 'uppercase',
              cursor: 'pointer',
              whiteSpace: 'nowrap'
            }}
          >
            {tab === 'all' ? 'Tutti' : tab === 'vocabulary' ? 'Parole' : tab === 'phrase' ? 'Frasi' : 'Testi'}
          </button>
        ))}
      </div>

      <div style={{ marginBottom: spacing.xl, display: 'flex', alignItems: 'center', gap: 8 }}>
        <input 
          type="checkbox" 
          id="showOnlyDue" 
          checked={showOnlyDue} 
          onChange={() => {
            setShowOnlyDue(!showOnlyDue);
            setCurrentIndex(0);
          }} 
        />
        <label htmlFor="showOnlyDue" style={{ fontSize: 14, fontWeight: 700, color: colors.textSecondary }}>
          Mostra solo elementi in scadenza
        </label>
      </div>

      <div
        onClick={() => {
          setRevealed(current => !current);
          if (!revealed) playAudio();
        }}
        className="card fade-in"
        style={{
          alignItems: 'center',
          minHeight: 300,
          justifyContent: 'center',
          padding: spacing.xl,
          textAlign: 'center',
          perspective: '1000px',
          borderWidth: 3,
          backgroundColor: revealed ? colors.surface : colors.chipBg,
          borderColor: revealed ? colors.accent : colors.border,
          boxShadow: `0 12px 30px rgba(78, 52, 46, 0.08)`
        }}
      >
        <div style={{ 
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: spacing.md
        }}>
          <span style={{ color: colors.accent, fontSize: 12, fontWeight: 900, textTransform: 'uppercase', letterSpacing: 2 }}>
            {revealed ? (isItFirst ? 'Inglese' : 'Italiano') : (isItFirst ? 'Italiano' : 'Inglese')}
          </span>
          <span style={{ 
            color: colors.primary, 
            fontSize: revealed ? 32 : 42, 
            fontWeight: 900, 
            lineHeight: '1.2',
            wordBreak: 'break-word'
          }}>
            {revealed ? (isItFirst ? currentItem.english : currentItem.italian) : (isItFirst ? currentItem.italian : currentItem.english)}
          </span>
          <div style={{ 
            marginTop: spacing.lg,
            color: colors.textSecondary, 
            fontSize: 13, 
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            gap: 6
          }}>
             <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21 12V7a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h7"/><path d="m16 20 2 2 4-4"/>
            </svg>
            Tocca per girare
          </div>
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md, marginTop: spacing.xl }}>
        {revealed ? (
          <div className="fade-in" style={{ display: 'flex', gap: spacing.md }}>
            <button
              onClick={() => answerCard(false)}
              style={{
                flex: 1,
                backgroundColor: colors.surface,
                color: colors.error,
                border: `3px solid ${colors.error}`,
                borderRadius: 16,
                minHeight: 60,
                fontWeight: 900,
                fontSize: 16,
                cursor: 'pointer',
                transition: 'all 0.1s'
              }}
              onMouseDown={e => e.currentTarget.style.transform = 'scale(0.95)'}
              onMouseUp={e => e.currentTarget.style.transform = 'scale(1)'}
            >
              DIMENTICATO
            </button>
            <button
              onClick={() => answerCard(true)}
              style={{
                flex: 1,
                backgroundColor: colors.success,
                color: colors.onPrimary,
                border: 'none',
                borderBottom: '4px solid rgba(0,0,0,0.2)',
                borderRadius: 16,
                minHeight: 60,
                fontWeight: 900,
                fontSize: 16,
                cursor: 'pointer',
                transition: 'all 0.1s'
              }}
              onMouseDown={e => e.currentTarget.style.transform = 'scale(0.95)'}
              onMouseUp={e => e.currentTarget.style.transform = 'scale(1)'}
            >
              RICORDATO
            </button>
          </div>
        ) : (
          <PrimaryButton label="Ascolta Audio" onPress={playAudio} variant="secondary" icon={
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
              <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
            </svg>
          } />
        )}
        <button 
          onClick={() => navigate('/')}
          style={{ 
            background: 'none', 
            border: 'none', 
            color: colors.textSecondary, 
            fontWeight: 800, 
            marginTop: spacing.md,
            cursor: 'pointer',
            textDecoration: 'underline'
          }}
        >
          Torna alla Home
        </button>
      </div>
    </Screen>
  );
};
