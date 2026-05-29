const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => {
    if(msg.text().includes('DIAGNOSTICS')) {
        console.log(msg.text());
    }
    console.log(msg.text());
  });
  await page.goto('http://localhost:5173/scenarios/22');
  await new Promise(r => setTimeout(r, 2000));
  await browser.close();
})();
