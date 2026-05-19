import React, { useState } from 'react';
import { colors } from '@shared/theme/colors';
import { spacing } from '@shared/theme/spacing';

export const ShortcutHelp: React.FC = () => {
  const [showTooltip, setShowTooltip] = useState(false);

  return (
    <div style={{ position: 'relative', display: 'inline-block', marginLeft: spacing.sm }}>
      <button
        onClick={() => setShowTooltip(!showTooltip)}
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
        style={{
          width: 28,
          height: 28,
          borderRadius: 14,
          border: `1px solid ${colors.border}`,
          backgroundColor: colors.surface,
          color: colors.primary,
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 16,
          fontWeight: 'bold',
          padding: 0,
        }}
      >
        ⌨️
      </button>
      {showTooltip && (
        <div style={{
          position: 'absolute',
          top: '100%',
          left: '50%',
          transform: 'translateX(-50%)',
          marginTop: spacing.xs,
          width: 200,
          backgroundColor: '#333',
          color: '#fff',
          padding: spacing.md,
          borderRadius: 8,
          fontSize: 13,
          zIndex: 100,
          boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
          textAlign: 'center',
          pointerEvents: 'none',
        }}>
          <strong>Shortcuts:</strong><br />
          1-4: Select an option<br />
          Enter: Submit answer
        </div>
      )}
    </div>
  );
};
