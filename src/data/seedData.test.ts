import {foundationLessons} from './foundations';
import {scenarios} from './scenarios';

describe('seed data', () => {
  it('contains all expanded scenarios with complete phase training material', () => {
    expect(scenarios).toHaveLength(116);

    scenarios.forEach(scenario => {
      expect(scenario.vocabulary.length).toBeGreaterThanOrEqual(20);
      expect(scenario.vocabulary.length).toBeLessThanOrEqual(90);
      expect(scenario.phrases.length).toBeGreaterThanOrEqual(5);
      expect(scenario.phrases.length).toBeLessThanOrEqual(10);
      expect(scenario.sentences.length).toBeGreaterThanOrEqual(5);
      expect(scenario.sentences.length).toBeLessThanOrEqual(10);
    });
  });

  it('keeps required Italian accents in foundation lessons', () => {
    const allTerms = foundationLessons.flatMap(lesson =>
      lesson.terms.map(term => term.italian),
    );

    expect(allTerms).toContain('è');
    expect(allTerms).toContain('là');
    expect(allTerms).toContain('perché');
    expect(allTerms).toContain('lui/lei può');
  });

  it('includes the requested foundation lesson structure', () => {
    expect(foundationLessons).toHaveLength(5);
    expect(foundationLessons[0]?.terms.map(term => term.italian)).toContain('io');
    expect(foundationLessons[0]?.terms.map(term => term.italian)).toContain('sono');
    expect(foundationLessons[0]?.exercises.length).toBeGreaterThan(5);
  });
});
