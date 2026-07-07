const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('/Users/chenruiyan/2026-project/thinking-notes/drafts/version2/social-card-ai-anxiety-cover/node_modules/playwright');

async function waitForAssets(page) {
  await page.waitForLoadState('networkidle').catch(() => {});
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
  await page.waitForTimeout(1200);
}

async function shot(page, selector, file) {
  await page.locator(selector).screenshot({ path: file });
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

  const targets = [
    ['#xhs-01', 'xhs-01-cover.png'],
    ['#xhs-02', 'xhs-02-problem.png'],
    ['#xhs-03', 'xhs-03-tool-thinking.png'],
    ['#xhs-04', 'xhs-04-system.png'],
    ['#xhs-05', 'xhs-05-real-task.png'],
    ['#xhs-06', 'xhs-06-closing.png'],
  ];

  for (const [selector, filename] of targets) {
    await shot(page, selector, path.join(outputDir, filename));
  }

  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
