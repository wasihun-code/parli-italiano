import React from 'react';
import { ExerciseDefinition, ExercisePayload, ValidationResult } from '../../exercises/types';
import { ListenExercise } from './exercises/ListenExercise';
import { MatchExercise } from './exercises/MatchExercise';
import { SpellingExercise } from './exercises/SpellingExercise';
import { PrimaryButton } from '../PrimaryButton';
import { colors } from '../../theme/colors';

interface ExerciseRendererProps {
  definition: ExerciseDefinition;
  payload: ExercisePayload;
  onComplete: (result: ValidationResult) => void;
}

/**
 * ExerciseRenderer
 * 
 * Determines which specific exercise component to render based on the 
 * ExerciseDefinition provided by the resolver. Includes fail-safe rendering.
 */
export const ExerciseRenderer: React.FC<ExerciseRendererProps> = ({ 
  definition, 
  payload, 
  onComplete 
}) => {
  const handleEmergencySkip = () => {
    console.warn(`[Fail-Safe] Emergency skip triggered for exercise: ${definition?.metadata?.id}`);
    onComplete({
      isValid: true,
      correctAnswer: "SKIPPED",
      feedback: "Esercizio saltato a causa di un errore tecnico."
    });
  };

  if (!definition || !payload) {
    return (
      <div style={{ padding: 20, textAlign: 'center', color: colors.error }}>
        <h2>Errore di Caricamento</h2>
        <p>I dati dell'esercizio sono corrotti o mancanti.</p>
        <PrimaryButton label="Salta Esercizio" onPress={handleEmergencySkip} />
      </div>
    );
  }

  const { id } = definition.metadata;

  // Pre-flight check for MCQ components
  if (['Listen', 'Match', 'ListenChoose'].includes(id)) {
    const options = payload.options || payload.choicesItalian;
    if (!options || !Array.isArray(options) || options.length === 0) {
      return (
        <div style={{ padding: 20, textAlign: 'center', color: colors.error }}>
          <h2>Errore Payload</h2>
          <p>Le opzioni di risposta per '{id}' sono vuote. L'esercizio non può essere completato.</p>
          <PrimaryButton label="Salta Esercizio" onPress={handleEmergencySkip} />
        </div>
      );
    }
  }

  try {
    switch (id) {
      case 'Listen':
        return <ListenExercise payload={payload} onComplete={onComplete} />;
      case 'Match':
        return <MatchExercise payload={payload} onComplete={onComplete} />;
      case 'Spelling':
        return <SpellingExercise payload={payload} onComplete={onComplete} />;
      default:
        return (
          <div style={{ padding: 20, textAlign: 'center', color: colors.error }}>
            <h2>Unsupported Exercise Type</h2>
            <p>The exercise type <strong>{id}</strong> is not yet implemented.</p>
            <PrimaryButton label="Continua" onPress={handleEmergencySkip} />
          </div>
        );
    }
  } catch (err: any) {
    return (
      <div style={{ padding: 20, textAlign: 'center', color: colors.error }}>
        <h2>Runtime Render Error</h2>
        <p>{err.message}</p>
        <PrimaryButton label="Salta Esercizio" onPress={handleEmergencySkip} />
      </div>
    );
  }
};
