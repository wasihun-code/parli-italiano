import React from 'react';
import { ExerciseDefinition, ExercisePayload, ValidationResult } from '../../exercises/types';
import { ListenExercise } from './exercises/ListenExercise';
import { MatchExercise } from './exercises/MatchExercise';
import { SpellingExercise } from './exercises/SpellingExercise';

interface ExerciseRendererProps {
  definition: ExerciseDefinition;
  payload: ExercisePayload;
  onComplete: (result: ValidationResult) => void;
}

/**
 * ExerciseRenderer
 * 
 * Determines which specific exercise component to render based on the 
 * ExerciseDefinition provided by the resolver.
 */
export const ExerciseRenderer: React.FC<ExerciseRendererProps> = ({ 
  definition, 
  payload, 
  onComplete 
}) => {
  const { id } = definition.metadata;

  switch (id) {
    case 'Listen':
      return <ListenExercise payload={payload} onComplete={onComplete} />;
    case 'Match':
      return <MatchExercise payload={payload} onComplete={onComplete} />;
    case 'Spelling':
      return <SpellingExercise payload={payload} onComplete={onComplete} />;
    default:
      return (
        <div style={{ padding: 20, textAlign: 'center', color: 'red' }}>
          <h2>Unsupported Exercise Type</h2>
          <p>The exercise type <strong>{id}</strong> is not yet implemented in the Pilot UI.</p>
        </div>
      );
  }
};
