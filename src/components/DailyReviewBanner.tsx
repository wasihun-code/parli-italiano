import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ReviewQueueService } from '../services/reviewQueueService';
import { colors } from '../theme/colors';
import { spacing } from '../theme/spacing';

export const DailyReviewBanner: React.FC = () => {
  const navigate = useNavigate();
  const [dueCount, setDueCount] = useState(0);

  useEffect(() => {
    async function fetchCount() {
      const queue = await ReviewQueueService.getDailyQueue();
      setDueCount(queue.length);
    }
    fetchCount();
  }, []);

  if (dueCount === 0) return null;

  return (
    <div 
      onClick={() => navigate('/daily-review')}
      style={{
        backgroundColor: colors.chipBg,
        border: `2px solid ${colors.accent}`,
        borderRadius: 16,
        padding: `${spacing.md}px ${spacing.lg}px`,
        display: 'flex',
        alignItems: 'center',
        gap: spacing.md,
        cursor: 'pointer',
        marginBottom: spacing.lg,
        transition: 'transform 0.2s',
      }}
      onMouseEnter={e => e.currentTarget.style.transform = 'scale(1.02)'}
      onMouseLeave={e => e.currentTarget.style.transform = 'scale(1)'}
    >
      <div style={{ fontSize: 24 }}>🧠</div>
      <div style={{ flex: 1 }}>
        <div style={{ fontWeight: 900, color: colors.primary, fontSize: 16 }}>
          {dueCount} Ripassi in scadenza
        </div>
        <div style={{ fontSize: 12, color: colors.textSecondary, fontWeight: 700 }}>
          Mantieni viva la memoria!
        </div>
      </div>
      <div style={{ color: colors.accent, fontWeight: 900, fontSize: 20 }}>→</div>
    </div>
  );
};
