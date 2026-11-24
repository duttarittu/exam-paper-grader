// One-off generator: renders a synthetic handwritten-style exam paper
// (HTML + handwriting font) and screenshots it as a JPG, for Step 0
// transcription-accuracy testing. Not part of the eventual grading pipeline.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height: 920 } });
  const htmlPath = path.join(__dirname, '..', 'samples', 'sample1.html');
  await page.goto('file://' + htmlPath);
  await page.waitForTimeout(500); // let web font load
  await page.screenshot({ path: path.join(__dirname, '..', 'samples', 'sample1.jpg') });
  await browser.close();
  console.log('Generated samples/sample1.jpg');
})();
