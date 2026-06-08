import React, { useEffect } from 'react';
import { ExercisePayload, ValidationResult } from '../../../exercises/types';
import { mcqValidator } from '../../../exercises/validators';
import { colors } from '../../../theme/colors';
import { spacing } from '../../../theme/spacing';

interface MatchExerciseProps {
  payload: ExercisePayload;
  onComplete: (result: ValidationResult) => void;
}

export const MatchExercise: React.FC<MatchExerciseProps> = ({ payload, onComplete }) => {
  const options = payload.options || [];

  const handleSelect = (option: string) => {
    const result = mcqValidator(payload, option);
    onComplete(result);
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const key = e.key.toUpperCase();
      const selectionKeys = ['1', '2', '3', '4', 'A', 'B', 'C', 'D'];
      const index = selectionKeys.indexOf(key);
      if (index !== -1) {
        const actualIndex = index % 4;
        if (actualIndex < options.length) {
          handleSelect(options[actualIndex]);
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [options, payload]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xxl, padding: spacing.xxl, alignItems: 'center', justifyContent: 'center', flex: 1 }}>
      <h2 style={{ color: colors.primary, textAlign: 'center', fontSize: 24, margin: 0 }}>Translate this word:</h2>
      <div style={{ 
        fontSize: 48, 
        fontWeight: 900, 
        textAlign: 'center', 
        color: colors.accent,
        marginBottom: spacing.md 
      }}>
        {payload.english}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: spacing.lg, width: '100%', maxWidth: 800 }}>
        {options.map((option, index) => (
          <button
            key={index}
            onClick={() => handleSelect(option)}
            style={{
              padding: spacing.xxl,
              backgroundColor: colors.surface,
              border: `3px solid ${colors.border}`,
              borderRadius: 24,
              fontSize: 28,
              fontWeight: 800,
              color: colors.textPrimary,
              cursor: 'pointer',
              transition: 'all 0.2s',
              boxShadow: '0 8px 0 rgba(0,0,0,0.05)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              minHeight: 120
            }}
            onMouseDown={e => e.currentTarget.style.transform = 'translateY(8px)'}
            onMouseUp={e => e.currentTarget.style.transform = 'translateY(0)'}
          >
            {option}
          </button>
        ))}
      </div>
    </div>
  );
};
