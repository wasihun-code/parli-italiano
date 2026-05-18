import { foundationLessons } from './src/data/foundations';

const placementExercises = foundationLessons.flatMap(lesson =>
  lesson.exercises
    .flatMap(exercise => {
      if (exercise.kind === 'listening') {
        return [];
      }

      const kind = exercise.kind === 'flashcard' ? 'multipleChoice' : exercise.kind;
      return {
        ...exercise,
        kind,
        lessonId: lesson.id,
      };
    })
).slice(0, 20); // Just take the first 20 for the "JSON object" requested

const output = {
  foundations: foundationLessons,
  placementTest: placementExercises
};

console.log(JSON.stringify(output, null, 2));
