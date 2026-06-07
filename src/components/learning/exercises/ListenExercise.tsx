import React, { useState, useEffect } from 'react';
import { ExercisePayload, ValidationResult } from '../../../exercises/types';
import { exactMatchValidator } from '../../../exercises/validators';
import { colors } from '../../../theme/colors';
import { spacing } from '../../../theme/spacing';
import { PrimaryButton } from '../../PrimaryButton';
import { Tts } from '../../../lib/tts';

interface ListenExerciseProps {
  payload: ExercisePayload;
  onComplete: (result: ValidationResult) => void;
}

export const ListenExercise: React.FC<ListenExerciseProps> = ({ payload, onComplete }) => {
  const [isRevealed, setIsRevealed] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);

  const playAudio = async () => {
    setIsPlaying(true);
    await Tts.speak(payload.italian, payload.audio);
    setIsPlaying(false);
  };

  useEffect(() => {
    playAudio();
  }, [payload.itemId]);

  const handleReveal = () => {
    setIsRevealed(true);
  };

  const handleContinue = () => {
    const result = exactMatchValidator(payload, payload.italian); 
    onComplete(result);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: spacing.xl, width: '100%', padding: spacing.lg }}>
      <h2 style={{ color: colors.textSecondary, fontSize: 16, fontWeight: 900, textTransform: 'uppercase', letterSpacing: 1 }}>
        Ascolta e comprendi
      </h2>

      <div style={{ position: 'relative', width: 140, height: 140 }}>
        {isPlaying && (
          <div style={{
            position: 'absolute',
            top: -10,
            left: -10,
            right: -10,
            bottom: -10,
            borderRadius: '50%',
            border: `4px solid ${colors.success}`,
            animation: 'pulse 1.5s infinite',
            opacity: 0.5
          }} />
        )}
        <button 
          onClick={playAudio}
          style={{ 
            width: 140, 
            height: 140, 
            borderRadius: 70, 
            backgroundColor: colors.chipBg, 
            border: `6px solid ${isPlaying ? colors.success : colors.accent}`,
            fontSize: 64,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: isPlaying ? `0 0 20px ${colors.success}80` : '0 4px 12px rgba(0,0,0,0.1)',
            transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
            transform: isPlaying ? 'scale(1.1)' : 'scale(1)',
            position: 'relative',
            zIndex: 2
          }}
        >
          {isPlaying ? '🔊' : '🔈'}
        </button>
      </div>

      <div style={{ minHeight: 120, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', width: '100%' }}>
        {isRevealed ? (
          <div className="fade-in" style={{ textAlign: 'center' }}>
            <div style={{ fontSize: 36, fontWeight: 900, color: colors.primary, marginBottom: spacing.xs }}>
              {payload.italian}
            </div>
            <div style={{ fontSize: 20, fontWeight: 700, color: colors.textSecondary }}>
              {payload.english}
            </div>
          </div>
        ) : (
          <div style={{ color: colors.textSecondary, fontStyle: 'italic', fontSize: 18 }}>
            Cosa hai sentito?
          </div>
        )}
      </div>

      <div style={{ width: '100%', marginTop: spacing.xl }}>
        {isRevealed ? (
          <PrimaryButton label="Continua" onPress={handleContinue} />
        ) : (
          <PrimaryButton label="Rivela Risposta" variant="secondary" onPress={handleReveal} />
        )}
      </div>
    </div>
  );
};
