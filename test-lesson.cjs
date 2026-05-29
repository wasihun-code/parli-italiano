const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER:', msg.text()));
  
  await page.goto('http://localhost:5173/scenarios/22');
  await page.waitForLoadState('networkidle');
  
  // Wait for lessons to appear
  await page.waitForSelector('text=Lessons');
  
  const startButton = page.locator('text=Start Lesson');
  if (await startButton.count() > 0) {
      await startButton.first().click();
      console.log("Clicked Start Lesson from Scenario Screen");
  } else {
      const startBtn2 = page.locator('text=Start');
      if (await startBtn2.count() > 0) {
          await startBtn2.first().click();
          console.log("Clicked Start from Scenario Screen");
      } else {
          console.log("No start button found on scenario screen");
      }
  }

  await page.waitForLoadState('networkidle');
  await new Promise(r => setTimeout(r, 1000));
  
  console.log("URL is now:", page.url());
  
  const startIntroBtn = page.locator('text=Start Lesson');
  if (await startIntroBtn.count() > 0) {
      await startIntroBtn.first().click();
      console.log("Clicked Start Lesson from Intro Screen");
  }

  await page.waitForLoadState('networkidle');
  await new Promise(r => setTimeout(r, 1000));
  
  console.log("URL is now:", page.url());
  
  const textContent = await page.evaluate(() => document.body.innerText);
  console.log("PAGE CONTENT PREVIEW:");
  console.log(textContent.substring(0, 500));
  
  // Extract all the choices (buttons with class 'card')
  const buttons = await page.locator('button.card').allTextContents();
  console.log("CHOICES ON SCREEN:");
  console.log(buttons);

  const pill = await page.locator('span', { hasText: /LEARN THE WORDS|BUILD THE PHRASES|PRACTICE THE DIALOGUE/i }).first().textContent().catch(() => null);
  console.log("PILL TEXT:", pill);

  await browser.close();
})();
