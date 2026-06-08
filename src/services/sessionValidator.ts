import { LearningStep } from '../types/learningPath';
import { resolveExercise } from '../exercises/resolver';

export class SessionValidator {
  /**
   * Validates an entire generated session to ensure no deadlocks can occur.
   * Checks every step to see if its payload resolves correctly and has
   * all necessary data for rendering.
   * 
   * @param steps The proposed session sequence.
   * @param scenarioData The full scenario corpus.
   * @returns boolean True if the session is 100% valid and playable.
   */
  static validateSession(steps: LearningStep[], scenarioData: any): boolean {
    for (const step of steps) {
      try {
        const { definition, payload } = resolveExercise(step, scenarioData);
        
        if (!definition || !payload) {
          console.error(`[Validator] Step ${step.id} resolved to null definition or payload.`);
          return false;
        }

        // MCQ strict validation
        if (['Listen', 'Match', 'ListenChoose'].includes(step.exerciseType)) {
          const options = payload.options || payload.choicesItalian;
          if (!options || !Array.isArray(options) || options.length < 2) {
             console.error(`[Validator] Step ${step.id} MCQ missing options.`);
             return false;
          }
          if (!options.includes(payload.italian)) {
             console.error(`[Validator] Step ${step.id} MCQ correct answer missing from options.`);
             return false;
          }
        }

      } catch (e) {
        console.error(`[Validator] Step ${step.id} threw an error during resolution:`, e);
        return false;
      }
    }
    return true;
  }
}
