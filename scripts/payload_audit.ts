import { loadProductionScenarioData } from '../src/data/corpusLoader';
import { LearningPathGenerator } from '../src/services/learningPathGenerator';
import { SessionGenerator } from '../src/services/sessionGenerator';
import { resolveExercise } from '../src/exercises/resolver';
import { ExerciseRegistry } from '../src/exercises/registry';
import * as fs from 'fs';

async function audit() {
  console.log("Starting Payload Audit...");
  const data = await loadProductionScenarioData(22);
  
  const input = {
    scenarioId: 22,
    scenarioData: data,
    globalMastery: {},
    reviewQueue: []
  };
  
  const fullPathResult = LearningPathGenerator.generatePath(input);
  const pilotTypes = ['Listen', 'Match', 'Spelling'];
  const filteredSteps = fullPathResult.path.steps.filter(s => pilotTypes.includes(s.exerciseType));
  const sessionSteps = SessionGenerator.generateSession({ ...fullPathResult.path, steps: filteredSteps });
  
  const report = {
    total: sessionSteps.length,
    failures: 0,
    details: [] as string[]
  };
  
  for (const step of sessionSteps) {
    try {
      const { definition, payload } = resolveExercise(step, data);
      
      let error = null;
      if (!payload) error = "Payload is null";
      else if (!definition.validator) error = "Missing validator";
      else if (!definition.completionHandler) error = "Missing completion contract";
      else if (['Listen', 'Match'].includes(step.exerciseType)) {
        const options = payload.options || payload.choicesItalian;
        if (!options || !Array.isArray(options) || options.length < 2) {
          error = `Missing or insufficient options. Options found: ${options?.length || 0}`;
        } else if (!options.includes(payload.italian)) {
          error = `Correct answer (${payload.italian}) missing from options. Options: ${options.join(', ')}`;
        }
      }
      
      if (error) {
        report.failures++;
        report.details.push(`[${step.exerciseType}] Step ${step.id}: ${error}`);
      }
    } catch (e: any) {
      report.failures++;
      report.details.push(`[${step.exerciseType}] Step ${step.id}: Exception - ${e.message}`);
    }
  }
  
  let md = `# Phase 9.6c: Payload Audit\n\n`;
  md += `## 1. Audit Target\nApartment Key Pickup (Scenario 22) - Generated V3 Pilot Session\n\n`;
  md += `## 2. Summary\n- Total Exercises Audited: ${report.total}\n- Payload Failures: ${report.failures}\n\n`;
  
  if (report.failures > 0) {
    md += `## 3. Failure Details\n`;
    report.details.forEach(d => md += `- ${d}\n`);
  } else {
    md += `## 3. Conclusion\nAll payloads conform to their contracts.\n`;
  }
  
  fs.writeFileSync('reports/phase96c_payload_audit.md', md);
  console.log(`Audit complete. Failures: ${report.failures}`);
}

audit().catch(console.error);