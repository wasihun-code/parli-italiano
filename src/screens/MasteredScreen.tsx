import React, { useState, useMemo } from 'react';
import { Screen } from '../components/Screen';
import { useSrsStore } from '@shared/store/srsStore';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

export const MasteredScreen: React.FC = () => {
  const items = useSrsStore(state => state.items);
  const unlearnItem = useSrsStore(state => state.unlearnItem);

  const [activeTab, setActiveTab] = useState<'vocabulary' | 'phrase' | 'sentence'>('vocabulary');
  const [searchTerm, setSearchTerm] = useState('');

  const masteredItems = useMemo(() => {
    return Object.values(items).filter(item => item.learned && item.type !== 'foundation');
  }, [items]);

  const filteredItems = useMemo(() => {
    return masteredItems
      .filter(item => item.type === activeTab)
      .filter(item => 
        item.italian.toLowerCase().includes(searchTerm.toLowerCase()) || 
        item.english.toLowerCase().includes(searchTerm.toLowerCase())
      )
      .sort((a, b) => a.italian.localeCompare(b.italian));
  }, [masteredItems, activeTab, searchTerm]);

  const counts = useMemo(() => {
    return {
      vocabulary: masteredItems.filter(i => i.type === 'vocabulary').length,
      phrase: masteredItems.filter(i => i.type === 'phrase').length,
      sentence: masteredItems.filter(i => i.type === 'sentence').length,
    };
  }, [masteredItems]);

  const handleUnlearn = (id: string) => {
    if (window.confirm('Are you sure you want to un-master this item? It will reappear in training.')) {
      unlearnItem(id);
    }
  };

  return (
    <Screen style={{ backgroundColor: colors.surface }}>
      <header style={{ marginBottom: spacing.lg }}>
        <h1 style={{ color: colors.primary, fontSize: 32, margin: 0, fontWeight: 900 }}>Words Learned</h1>
        <p style={{ color: colors.textSecondary, margin: '8px 0 0 0' }}>Total Mastered: {masteredItems.length}</p>
      </header>

      <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg, paddingBottom: 100 }}>
        
        <input
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={e => setSearchTerm(e.target.value)}
          style={{
            padding: spacing.md,
            borderRadius: 12,
            border: `2px solid ${colors.border}`,
            fontSize: 16,
            backgroundColor: colors.bg,
          }}
        />

        <div style={{ display: 'flex', gap: spacing.sm, borderBottom: `2px solid ${colors.border}`, paddingBottom: spacing.sm }}>
          {(['vocabulary', 'phrase', 'sentence'] as const).map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              style={{
                padding: '8px 16px',
                borderRadius: 20,
                border: 'none',
                backgroundColor: activeTab === tab ? colors.primary : 'transparent',
                color: activeTab === tab ? colors.onPrimary : colors.textSecondary,
                fontWeight: 'bold',
                cursor: 'pointer',
                textTransform: 'capitalize'
              }}
            >
              {tab === 'vocabulary' ? 'Words' : tab + 's'} ({counts[tab]})
            </button>
          ))}
        </div>

        {filteredItems.length === 0 ? (
          <p style={{ color: colors.textSecondary, textAlign: 'center', marginTop: spacing.xl }}>
            No mastered {activeTab === 'vocabulary' ? 'words' : activeTab + 's'} found.
          </p>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.md }}>
            {filteredItems.map(item => (
              <div key={item.id} className="card" style={{ padding: spacing.md, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <div style={{ fontWeight: 'bold', color: colors.primary, fontSize: 18 }}>{item.italian}</div>
                  <div style={{ color: colors.textSecondary, fontSize: 14 }}>{item.english}</div>
                </div>
                <button
                  onClick={() => handleUnlearn(item.id)}
                  title="Un-master this item"
                  style={{
                    background: 'none',
                    border: 'none',
                    color: colors.error,
                    cursor: 'pointer',
                    fontSize: 20,
                    opacity: 0.7,
                    transition: 'opacity 0.2s',
                  }}
                  onMouseEnter={e => e.currentTarget.style.opacity = '1'}
                  onMouseLeave={e => e.currentTarget.style.opacity = '0.7'}
                >
                  ✖
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </Screen>
  );
};
