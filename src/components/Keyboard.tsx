import React from 'react';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

interface KeyboardProps {
  onKeyPress: (key: string) => void;
}

const ACCENTED_CHARS = ['à', 'è', 'é', 'ì', 'ò', 'ù'];

export const Keyboard: React.FC<KeyboardProps> = ({ onKeyPress }) => {
  return (
    <div style={{
      display: 'flex',
      flexWrap: 'wrap',
      gap: spacing.sm,
      justifyContent: 'center',
      padding: spacing.md,
      backgroundColor: colors.chipBg,
      borderRadius: 16,
      border: `1px solid ${colors.border}`,
      boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.03)'
    }}>
      {ACCENTED_CHARS.map(char => (
        <button
          key={char}
          onClick={() => onKeyPress(char)}
          style={{
            width: 44,
            height: 44,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            backgroundColor: colors.surface,
            border: `2px solid ${colors.border}`,
            borderBottomWidth: 4,
            borderRadius: 10,
            fontSize: 18,
            fontWeight: 800,
            color: colors.primary,
            cursor: 'pointer',
            transition: 'all 0.1s',
            userSelect: 'none',
          }}
          onMouseDown={e => {
            e.currentTarget.style.transform = 'translateY(2px)';
            e.currentTarget.style.borderBottomWidth = '2px';
          }}
          onMouseUp={e => {
            e.currentTarget.style.transform = 'translateY(0)';
            e.currentTarget.style.borderBottomWidth = '4px';
          }}
        >
          {char}
        </button>
      ))}
    </div>
  );
};
