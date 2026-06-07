import React, { useState } from 'react';
import { ExercisePayload, ValidationResult } from '../../../exercises/types';
import { exactMatchValidator } from '../../../exercises/validators';
import { colors } from '../../../theme/colors';
import { spacing } from '../../../theme/spacing';
import { PrimaryButton } from '../../PrimaryButton';

interface SpellingExerciseProps {
  payload: ExercisePayload;
  onComplete: (result: ValidationResult) => void;
}

export const SpellingExercise: React.FC<SpellingExerciseProps> = ({ payload, onComplete }) => {
  const [input, setInput] = useState('');

  const handleSubmit = () => {
    const result = exactMatchValidator(payload, input);
    onComplete(result);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.lg, padding: spacing.xl }}>
      <h2 style={{ color: colors.primary, textAlign: 'center' }}>Type the Italian word:</h2>
      <div style={{ 
        fontSize: 32, 
        fontWeight: 900, 
        textAlign: 'center', 
        color: colors.accent,
        marginBottom: spacing.xl 
      }}>
        {payload.english}
      </div>

      <input
        autoFocus
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
        style={{
          width: '100%',
          maxWidth: 400,
          padding: spacing.xl,
          fontSize: 32,
          fontWeight: 800,
          textAlign: 'center',
          borderRadius: 24,
          border: `3px solid ${colors.border}`,
          backgroundColor: colors.surface,
          color: colors.textPrimary,
          outline: 'none',
          boxShadow: 'inset 0 2px 8px rgba(0,0,0,0.05)'
        }}
        placeholder="Scrivi qui..."
      />

      <div style={{ marginTop: spacing.xl }}>
        <PrimaryButton label="Check Answer" onPress={handleSubmit} />
      </div>
    </div>
  );
};
