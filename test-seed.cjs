const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  page.on('console', msg => {
    console.log('BROWSER:', msg.text());
  });

  await page.goto('http://localhost:5173/');
  
  // Clear the database to force re-seed
  await page.evaluate(async () => {
    return new Promise((resolve, reject) => {
        const req = indexedDB.deleteDatabase('ParlaItalianoDB');
        req.onsuccess = () => resolve();
        req.onerror = () => reject();
    });
  });
  
  console.log("Database deleted. Reloading...");
  
  await page.reload();
  
  // Wait for seeding logs
  await new Promise(r => setTimeout(r, 5000));
  
  await browser.close();
})();
