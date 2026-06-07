import { db, LearningSession } from '../lib/db';
import { LearningStep } from '../types/learningPath';

/**
 * SessionPersistenceService
 * 
 * Handles the persistence of V3 learning sessions to Dexie IndexedDB.
 */
export class SessionPersistenceService {
  
  /**
   * Saves the current session state.
   */
  static async saveSession(scenarioId: number, index: number, steps: LearningStep[], isCompleted: boolean = false): Promise<void> {
    await db.learning_sessions.put({
      scenario_id: scenarioId,
      current_step_index: index,
      steps_json: JSON.stringify(steps),
      updated_at: new Date().toISOString(),
      is_completed: isCompleted
    });
  }

  /**
   * Loads a saved session for a specific scenario.
   */
  static async loadSession(scenarioId: number): Promise<LearningSession | undefined> {
    return await db.learning_sessions.get(scenarioId);
  }

  /**
   * Deletes a session (e.g., upon completion or reset).
   */
  static async clearSession(scenarioId: number): Promise<void> {
    await db.learning_sessions.delete(scenarioId);
  }
}
