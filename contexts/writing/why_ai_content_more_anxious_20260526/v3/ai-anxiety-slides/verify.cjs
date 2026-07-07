const { chromium } = require('/Users/chenruiyan/2026-project/thinking-notes/drafts/version2/social-card-ai-anxiety-cover/node_modules/playwright');
const { pathToFileURL } = require('url');
const path = require('path');

async function main() {
  const dir = __dirname;
  const htmlUrl = pathToFileURL(path.join(dir, 'index.html')).href;
  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const page = await browser.newPage({
    viewport: { width: 1720, height: 900 },
    deviceScaleFactor: 1,
  });

  await page.goto(htmlUrl);
  await page.waitForTimeout(800);

  const slideCount = await page.locator('.slide').count();
  const firstTitle = (await page.locator('.slide.active .title, .slide.active .slide-title').first().textContent()).trim();
  await page.screenshot({ path: path.join(dir, 'preview-slide-01.png'), fullPage: false });

  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(300);
  const currentIndex = await page.locator('#currentIndex').textContent();
  const secondTitle = (await page.locator('.slide.active .title, .slide.active .slide-title').first().textContent()).trim();

  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(htmlUrl);
  await page.waitForTimeout(500);
  const mobileSlideDisplay = await page.locator('.slide').first().evaluate((node) => getComputedStyle(node).position);

  await browser.close();
  console.log(JSON.stringify({ slideCount, firstTitle, currentIndex, secondTitle, mobileSlideDisplay }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
