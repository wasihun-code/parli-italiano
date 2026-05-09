import React from 'react';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

interface PrimaryButtonProps {
  label: string;
  onPress: () => void;
  disabled?: boolean;
  style?: React.CSSProperties;
  variant?: 'primary' | 'secondary' | 'accent';
  icon?: React.ReactNode;
}

export const PrimaryButton: React.FC<PrimaryButtonProps> = ({
  label,
  onPress,
  disabled,
  style,
  variant = 'primary',
  icon,
}) => {
  const getBgColor = () => {
    if (disabled) return colors.border;
    if (variant === 'secondary') return colors.secondary;
    if (variant === 'accent') return colors.accent;
    return colors.primary;
  };

  const getBorderColor = () => {
    if (disabled) return 'rgba(0,0,0,0.1)';
    if (variant === 'secondary') return 'rgba(0,0,0,0.2)';
    if (variant === 'accent') return 'rgba(0,0,0,0.2)';
    return 'rgba(0,0,0,0.3)';
  };

  return (
    <button
      onClick={onPress}
      disabled={disabled}
      className="primary-button"
      style={{
        backgroundColor: getBgColor(),
        color: colors.onPrimary,
        padding: `${spacing.md}px ${spacing.lg}px`,
        borderRadius: 16,
        border: 'none',
        borderBottom: `4px solid ${getBorderColor()}`,
        fontSize: 18,
        fontWeight: 900,
        cursor: disabled ? 'not-allowed' : 'pointer',
        width: '100%',
        transition: 'all 0.1s ease',
        transform: 'translateY(0)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: spacing.sm,
        textTransform: 'uppercase',
        letterSpacing: 1.2,
        userSelect: 'none',
        ...style,
      }}
      onMouseDown={e => {
        if (!disabled) {
          e.currentTarget.style.transform = 'translateY(2px)';
          e.currentTarget.style.borderBottomWidth = '2px';
        }
      }}
      onMouseUp={e => {
        if (!disabled) {
          e.currentTarget.style.transform = 'translateY(0)';
          e.currentTarget.style.borderBottomWidth = '4px';
        }
      }}
      onMouseLeave={e => {
        if (!disabled) {
          e.currentTarget.style.transform = 'translateY(0)';
          e.currentTarget.style.borderBottomWidth = '4px';
        }
      }}
    >
      {icon}
      {label}
    </button>
  );
};
