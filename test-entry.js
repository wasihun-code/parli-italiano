
const files = import.meta.glob('./src/data/exports/accommodation/apartment_key_pickup/mini_lessons.json', { eager: true });
console.log("GLOB RESULT:", Object.keys(files));
console.log("MODULE TYPE:", typeof files[Object.keys(files)[0]]);
console.log("MODULE KEYS:", Object.keys(files[Object.keys(files)[0]]));
