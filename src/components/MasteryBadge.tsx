import React from 'react';
import { colors } from '@shared/theme/colors';

export type MasteryState = 'UNKNOWN' | 'LEARNING' | 'LEARNED' | 'ADVANCED' | 'MASTERED' | 'LAPSED' | 'RELEARNING';

interface MasteryBadgeProps {
  state: MasteryState;
  showLabel?: boolean;
}

export const MasteryBadge: React.FC<MasteryBadgeProps> = ({ state, showLabel = true }) => {
  let color = colors.textSecondary;
  let label = 'Unknown';
  let icon = '❓';

  switch (state) {
    case 'LEARNING':
    case 'RELEARNING':
      color = colors.accent;
      label = 'Learning';
      icon = '🔄';
      break;
    case 'LEARNED':
      color = colors.success;
      label = 'Learned';
      icon = '✓';
      break;
    case 'ADVANCED':
      color = '#8b5cf6'; // purple
      label = 'Advanced';
      icon = '⭐';
      break;
    case 'MASTERED':
      color = '#f59e0b'; // gold
      label = 'Mastered';
      icon = '👑';
      break;
    case 'LAPSED':
      color = colors.error;
      label = 'Lapsed';
      icon = '⚠️';
      break;
    case 'UNKNOWN':
    default:
      color = colors.textSecondary;
      label = 'New';
      icon = '✨';
      break;
  }

  return (
    <div style={{
      display: 'inline-flex',
      alignItems: 'center',
      gap: 4,
      padding: '4px 8px',
      borderRadius: 12,
      backgroundColor: `${color}15`,
      border: `1px solid ${color}30`,
      color: color,
      fontSize: 12,
      fontWeight: 800,
      textTransform: 'uppercase',
      letterSpacing: 0.5
    }}>
      <span style={{ fontSize: 14 }}>{icon}</span>
      {showLabel && <span>{label}</span>}
    </div>
  );
};
