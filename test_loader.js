import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const scenarioMapping = {
  22: 'exports/accommodation/apartment_key_pickup'
};

const relPath = scenarioMapping[22];
const miniLessonsPath = `./${relPath}/mini_lessons.json`;
console.log('Constructed path:', miniLessonsPath);

const fullPath = path.resolve(__dirname, 'src/data', miniLessonsPath);
console.log('Full path:', fullPath);
console.log('File exists?', fs.existsSync(fullPath));

if (fs.existsSync(fullPath)) {
  const content = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
  console.log('Has lessons array?', Array.isArray(content.lessons));
  console.log('Lessons length:', content.lessons.length);
}
