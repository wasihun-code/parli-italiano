import React, { useEffect } from 'react';
import { audioService } from '../lib/audioService';
import { useAudioStore } from '../store/audioStore';

export const FeedbackMessage: React.FC<{
  type: 'correct' | 'incorrect' | 'neutral';
  message: string | React.ReactNode;
}> = ({ type, message }) => {
  const soundEnabled = useAudioStore(state => state.soundEnabled);

  useEffect(() => {
    if (soundEnabled) {
      if (type === 'correct') audioService.playCorrect();
      else if (type === 'incorrect') audioService.playIncorrect();
    }
  }, [type, soundEnabled]);

  let bgColor = '#f5f5f5';
  let borderColor = '#9e9e9e';
  let color = '#333';

  if (type === 'correct') {
    bgColor = '#e6f4ea';
    borderColor = '#2e7d32';
    color = '#1b5e20';
  } else if (type === 'incorrect') {
    bgColor = '#fce8e6';
    borderColor = '#c5221f';
    color = '#b71c1c';
  }

  return (
    <div className="fade-in" style={{
      padding: '16px 24px',
      borderRadius: '20px',
      backgroundColor: bgColor,
      border: `2px solid ${borderColor}`,
      color: color,
      fontWeight: 'bold',
      textAlign: 'center',
      marginBottom: '16px',
      width: '100%'
    }}>
      {message}
    </div>
  );
};
