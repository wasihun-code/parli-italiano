import React from 'react';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

interface WordChipProps {
  word: string;
  onPress: () => void;
  disabled?: boolean;
  selected?: boolean;
}

export const WordChip: React.FC<WordChipProps> = ({
  word,
  onPress,
  disabled,
  selected,
}) => {
  return (
    <button
      onClick={onPress}
      disabled={disabled}
      style={{
        backgroundColor: selected ? colors.accent : colors.chipBg,
        color: selected ? colors.onPrimary : colors.textPrimary,
        padding: `${spacing.sm}px ${spacing.md}px`,
        borderRadius: 12,
        border: 'none',
        borderBottom: `3px solid ${selected ? 'rgba(0,0,0,0.2)' : colors.border}`,
        fontSize: 16,
        fontWeight: 700,
        cursor: disabled ? 'not-allowed' : 'pointer',
        transition: 'all 0.1s ease',
        opacity: disabled ? 0.5 : 1,
        transform: selected ? 'translateY(1px)' : 'translateY(0)',
        boxShadow: selected ? 'none' : '0 2px 4px rgba(0,0,0,0.05)',
        margin: 4,
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        userSelect: 'none',
      }}
      onMouseDown={e => !disabled && (e.currentTarget.style.transform = 'translateY(1px)')}
      onMouseUp={e => !disabled && (e.currentTarget.style.transform = selected ? 'translateY(1px)' : 'translateY(0)')}
    >
      {word}
    </button>
  );
};
