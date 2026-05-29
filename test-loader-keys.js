import fs from 'fs';
import path from 'path';

const files = fs.readdirSync('src/data/exports/accommodation/apartment_key_pickup');
console.log(files);
