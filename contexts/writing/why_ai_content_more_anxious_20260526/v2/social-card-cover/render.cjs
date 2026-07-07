const { chromium } = require('playwright');
const path = require('path');
const { pathToFileURL } = require('url');

async function waitForAssets(page) {
  await page.waitForLoadState('networkidle');
  await page.evaluate(async () => {
    const fontsReady = document.fonts ? document.fonts.ready : Promise.resolve();
    const images = Array.from(document.images).map((img) => {
      if (img.complete) return Promise.resolve();
      return new Promise((resolve) => {
        img.addEventListener('load', resolve, { once: true });
        img.addEventListener('error', resolve, { once: true });
      });
    });
    await Promise.all([fontsReady, ...images]);
  });
  await page.waitForTimeout(900);
}

async function shot(page, selector, outPath) {
  const node = page.locator(selector);
  await node.screenshot({ path: outPath });
}

async function main() {
  const taskDir = __dirname;
  const htmlUrl = pathToFileURL(path.join(taskDir, 'index.html')).href;
  const outputDir = path.join(taskDir, 'output');

  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const page = await browser.newPage({
    viewport: { width: 3600, height: 2000 },
    deviceScaleFactor: 1,
  });

  await page.goto(htmlUrl);
  await waitForAssets(page);

  await shot(page, '#wechat-21x9', path.join(outputDir, 'wechat-21x9-cover.png'));
  await shot(page, '#wechat-1x1', path.join(outputDir, 'wechat-1x1-cover.png'));

  await page.reload();
  await waitForAssets(page);
  await shot(page, '#wechat-pair-preview', path.join(outputDir, 'wechat-cover-pair-preview.png'));

  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
