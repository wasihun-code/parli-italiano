import { build } from 'vite';

build({
  build: {
    rollupOptions: { input: 'src/data/corpusLoader.ts' },
    write: false,
    minify: false
  }
}).then(res => {
  const chunk = res.output.find(o => o.type === 'chunk');
  const code = chunk.code;
  const match = code.match(/mini_lessons\.json/g);
  console.log("Found mini_lessons.json mentions:", match ? match.length : 0);
});
