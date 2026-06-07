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
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg, padding: spacing.xl }}>
      <h2 style={{ color: colors.primary, textAlign: 'center' }}>Translate this word:</h2>
      <div style={{ 
        fontSize: 32, 
        fontWeight: 900, 
        textAlign: 'center', 
        color: colors.accent,
        marginBottom: spacing.xl 
      }}>
        {payload.english}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: spacing.md, width: '100%', maxWidth: 500 }}>
        {options.map((option, index) => (
          <button
            key={index}
            onClick={() => handleSelect(option)}
            style={{
              padding: spacing.xl,
              backgroundColor: colors.surface,
              border: `3px solid ${colors.border}`,
              borderRadius: 24,
              fontSize: 22,
              fontWeight: 800,
              color: colors.textPrimary,
              cursor: 'pointer',
              transition: 'all 0.2s',
              boxShadow: '0 4px 0 rgba(0,0,0,0.05)'
            }}
            onMouseDown={e => e.currentTarget.style.transform = 'translateY(4px)'}
            onMouseUp={e => e.currentTarget.style.transform = 'translateY(0)'}
          >
            {option}
          </button>
        ))}
      </div>
    </div>
  );
};
