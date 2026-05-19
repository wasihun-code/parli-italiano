import React from 'react';
import { colors } from '@shared/theme/colors';

export const ProgressBar: React.FC<{ progress: number }> = ({ progress }) => {
  const safeProgress = Math.max(0, Math.min(100, progress));
  return (
    <div style={{
      width: '100%',
      height: '12px',
      backgroundColor: colors.border,
      borderRadius: '6px',
      overflow: 'hidden',
      marginBottom: '16px'
    }}>
      <div style={{
        height: '100%',
        width: `${safeProgress}%`,
        backgroundColor: colors.success,
        transition: 'width 0.3s ease-out'
      }} />
    </div>
  );
};
