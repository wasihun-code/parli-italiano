import { useProgressStore } from './src/store/progressStore';
useProgressStore.getState().completeMiniLesson(22, 'l1', 6);
console.log(useProgressStore.getState().scenarioProgress[22]);
