import React from 'react';
import { colors } from '../../theme/colors';
import { spacing } from '../../theme/spacing';
import { PrimaryButton } from '../PrimaryButton';
import { ValidationResult } from '../../exercises/types';

interface FeedbackOverlayProps {
  result: ValidationResult;
  onContinue: () => void;
}

export const FeedbackOverlay: React.FC<FeedbackOverlayProps> = ({ result, onContinue }) => {
  const isCorrect = result.isValid;

  return (
    <div style={{
      position: 'absolute',
      bottom: 0,
      left: 0,
      right: 0,
      padding: spacing.xl,
      backgroundColor: isCorrect ? 'rgba(46, 125, 50, 0.95)' : 'rgba(158, 42, 43, 0.95)',
      color: 'white',
      borderTopLeftRadius: 24,
      borderTopRightRadius: 24,
      display: 'flex',
      flexDirection: 'column',
      gap: spacing.md,
      zIndex: 100,
      boxShadow: '0 -4px 12px rgba(0,0,0,0.1)'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: spacing.md }}>
        <span style={{ fontSize: 32 }}>{isCorrect ? '✅' : '❌'}</span>
        <h2 style={{ margin: 0, fontSize: 24, fontWeight: 900 }}>
          {isCorrect ? 'Esatto!' : 'Sbagliato'}
        </h2>
      </div>

      {!isCorrect && result.correctAnswer && (
        <div style={{ marginTop: spacing.md, backgroundColor: 'rgba(255,255,255,0.15)', padding: spacing.lg, borderRadius: 16 }}>
          <div style={{ fontSize: 16, fontWeight: 800, textTransform: 'uppercase', opacity: 0.9, marginBottom: 4 }}>Risposta Corretta:</div>
          <div style={{ fontSize: 28, fontWeight: 900 }}>{result.correctAnswer}</div>
        </div>
      )}

      {result.feedback && (
        <div style={{ fontSize: 18, fontStyle: 'italic', opacity: 0.9, backgroundColor: 'rgba(0,0,0,0.2)', padding: spacing.lg, borderRadius: 16, marginTop: spacing.sm }}>
          {result.feedback}
        </div>
      )}

      {/* Contextual Relevancy / Recommendation */}
      {isCorrect ? (
        <div style={{ fontSize: 16, opacity: 0.9, fontWeight: 600, marginTop: spacing.sm }}>
          Ottimo! Questo ti aiuterà nella conversazione reale.
        </div>
      ) : (
        <div style={{ fontSize: 16, opacity: 0.9, fontWeight: 600, marginTop: spacing.sm }}>
          Non preoccuparti. Lo rivedremo presto per aiutarti a memorizzarlo.
        </div>
      )}

      <div style={{ marginTop: spacing.md }}>
        <PrimaryButton 
          label="Continua (Enter)" 
          onPress={onContinue} 
          variant="secondary"
          style={{ backgroundColor: 'white', color: isCorrect ? colors.success : colors.error }}
        />
      </div>
    </div>
  );
};
