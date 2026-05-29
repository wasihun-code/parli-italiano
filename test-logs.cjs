const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => {
    if(msg.text().includes('DIAGNOSTICS')) {
        console.log(msg.text());
        // Also get the next few messages since I didn't prefix them all
    }
    console.log(msg.text());
  });
  await page.goto('http://localhost:5173/scenarios/22'); // assuming vite runs on 5173
  await new Promise(r => setTimeout(r, 2000));
  await browser.close();
})();
