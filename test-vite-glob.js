import { build } from 'vite';
import fs from 'fs';

const code = `
const files = import.meta.glob('./src/data/exports/accommodation/apartment_key_pickup/mini_lessons.json', { eager: true });
console.log("GLOB RESULT:", Object.keys(files));
console.log("MODULE TYPE:", typeof files[Object.keys(files)[0]]);
console.log("MODULE KEYS:", Object.keys(files[Object.keys(files)[0]]));
`;

fs.writeFileSync('test-entry.js', code);

build({
  build: {
    rollupOptions: { input: 'test-entry.js' },
    write: false,
    minify: false
  }
}).then(res => {
  const chunk = res.output.find(o => o.type === 'chunk');
  console.log("COMPILED:");
  console.log(chunk.code);
});