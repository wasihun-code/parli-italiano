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

  const options = payload.options || payload.choicesItalian || [];

  const handleSelect = (option: string) => {
    const result = {
      isValid: option === payload.italian,
      correctAnswer: payload.italian,
      feedback: option === payload.italian 
        ? "Corretto! Hai riconosciuto la parola." 
        : `Hai scelto '${option}', ma l'audio diceva '${payload.italian}'.`
    };
    onComplete(result);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: spacing.xxl, width: '100%', padding: spacing.xxl, flex: 1 }}>
      <h2 style={{ color: colors.textSecondary, fontSize: 24, fontWeight: 900, textTransform: 'uppercase', letterSpacing: 1, margin: 0 }}>
        Ascolta e seleziona
      </h2>

      <div style={{ position: 'relative', width: 180, height: 180 }}>
        {isPlaying && (
          <div style={{
            position: 'absolute',
            top: -10,
            left: -10,
            right: -10,
            bottom: -10,
            borderRadius: '50%',
            border: `6px solid ${colors.success}`,
            animation: 'pulse 1.5s infinite',
            opacity: 0.5
          }} />
        )}
        <button 
          onClick={playAudio}
          style={{ 
            width: 180, 
            height: 180, 
            borderRadius: 90, 
            backgroundColor: colors.chipBg, 
            border: `8px solid ${isPlaying ? colors.success : colors.accent}`,
            fontSize: 80,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: isPlaying ? `0 0 30px ${colors.success}80` : '0 8px 24px rgba(0,0,0,0.1)',
            transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
            transform: isPlaying ? 'scale(1.1)' : 'scale(1)',
            position: 'relative',
            zIndex: 2
          }}
        >
          {isPlaying ? '🔊' : '🔈'}
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: spacing.lg, width: '100%', maxWidth: 800, marginTop: spacing.xl }}>
        {options.map((option, index) => (
          <button
            key={index}
            onClick={() => handleSelect(option)}
            style={{
              padding: spacing.xxl,
              backgroundColor: colors.surface,
              border: `3px solid ${colors.border}`,
              borderRadius: 24,
              fontSize: 24,
              fontWeight: 800,
              color: colors.textPrimary,
              cursor: 'pointer',
              transition: 'all 0.2s',
              boxShadow: '0 8px 0 rgba(0,0,0,0.05)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              minHeight: 100
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
