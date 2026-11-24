// One-off generator: renders synthetic handwritten-style exam papers
// (HTML + handwriting font) and screenshots them as JPGs, for Step 0
// transcription-accuracy testing. Not part of the eventual grading pipeline.
//
// Usage: node scripts/generate_sample.js <name> <height>
//   e.g. node scripts/generate_sample.js sample1 920
const { chromium } = require('playwright');
const path = require('path');

const name = process.argv[2] || 'sample1';
const height = parseInt(process.argv[3] || '920', 10);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1000, height } });
  const htmlPath = path.join(__dirname, '..', 'samples', `${name}.html`);
  await page.goto('file://' + htmlPath);
  await page.waitForTimeout(500); // let web font load
  await page.screenshot({ path: path.join(__dirname, '..', 'samples', `${name}.jpg`) });
  await browser.close();
  console.log(`Generated samples/${name}.jpg`);
})();
