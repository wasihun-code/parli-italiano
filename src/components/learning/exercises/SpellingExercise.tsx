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
    <div style={{ display: 'flex', flexDirection: 'column', gap: spacing.xxl, padding: spacing.xxl, alignItems: 'center', justifyContent: 'center', flex: 1 }}>
      <h2 style={{ color: colors.primary, textAlign: 'center', fontSize: 24, margin: 0 }}>Type the Italian word:</h2>
      <div style={{ 
        fontSize: 48, 
        fontWeight: 900, 
        textAlign: 'center', 
        color: colors.accent,
        marginBottom: spacing.md 
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
          maxWidth: 600,
          padding: spacing.xxl,
          fontSize: 40,
          fontWeight: 800,
          textAlign: 'center',
          borderRadius: 32,
          border: `4px solid ${colors.border}`,
          backgroundColor: colors.surface,
          color: colors.textPrimary,
          outline: 'none',
          boxShadow: 'inset 0 4px 16px rgba(0,0,0,0.05)'
        }}
        placeholder="Scrivi qui..."
      />

      <div style={{ width: '100%', maxWidth: 400, marginTop: spacing.xxl }}>
        <PrimaryButton label="Check Answer" onPress={handleSubmit} />
      </div>
    </div>
  );
};
