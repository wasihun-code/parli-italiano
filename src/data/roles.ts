import { ScenarioCategory } from './scenarios';

export type RolePair = {
  aiRole: string;
  userRole: string;
};

const categoryRoleMap: Record<ScenarioCategory, RolePair> = {
  Travel: { aiRole: "un impiegato dell'aeroporto o della stazione", userRole: 'un turista' },
  Accommodation: { aiRole: 'un receptionist di un hotel', userRole: 'un turista' },
  Dining: { aiRole: 'un cameriere di un ristorante italiano', userRole: 'un turista' },
  Shopping: { aiRole: 'un commesso di un negozio', userRole: 'un turista' },
  'Daily Life': { aiRole: 'una persona del posto', userRole: 'un turista' },
  WorkStudy: { aiRole: 'un collega o compagno di studi', userRole: 'un turista' },
  Social: { aiRole: 'un amico italiano', userRole: 'un turista' },
  Culture: { aiRole: 'una guida turistica', userRole: 'un turista' },
  Health: { aiRole: 'un dottore o farmacista', userRole: 'un turista' },
  Tech: { aiRole: 'un tecnico informatico', userRole: 'un turista' },
  Miscellaneous: { aiRole: 'una persona disponibile', userRole: 'un turista' },
  Animals: { aiRole: 'una guida in un parco', userRole: 'uno studente di italiano' },
  Verbs_ARE: { aiRole: 'un insegnante di italiano', userRole: 'uno studente di italiano' },
  Verbs_ERE: { aiRole: 'un insegnante di italiano', userRole: 'uno studente di italiano' },
  Verbs_IRE: { aiRole: 'un insegnante di italiano', userRole: 'uno studente di italiano' },
  Reflexive_Verbs: { aiRole: 'un insegnante di italiano', userRole: 'uno studente di italiano' },
  Adjectives: { aiRole: 'un insegnante di italiano', userRole: 'uno studente di italiano' },
};

const specificScenarioRoleMap: Record<number, RolePair> = {};

export function getScenarioRoles(scenarioId: number, category: ScenarioCategory): RolePair {
  return specificScenarioRoleMap[scenarioId] || categoryRoleMap[category];
}
