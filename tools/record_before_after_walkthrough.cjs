const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');


async function main() {
  const baseUrl = process.argv[2];
  const outputPath = path.resolve(process.argv[3]);
  if (!baseUrl || !process.argv[3]) {
    throw new Error('Usage: node tools/record_before_after_walkthrough.cjs <controller-url> <output.webm>');
  }

  const temporaryVideoDir = path.resolve('output/playwright/audit-package/continuous-video');
  fs.mkdirSync(temporaryVideoDir, { recursive: true });
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  if (fs.existsSync(outputPath)) {
    fs.rmSync(outputPath);
  }

  const browserExecutable = process.env.BROWSER_EXECUTABLE || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
  if (!fs.existsSync(browserExecutable)) {
    throw new Error(`Browser executable not found: ${browserExecutable}`);
  }
  const browser = await chromium.launch({ headless: true, executablePath: browserExecutable });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    recordVideo: {
      dir: temporaryVideoDir,
      size: { width: 1280, height: 720 },
    },
  });
  const page = await context.newPage();

  try {
    await page.goto(baseUrl, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const video = page.video();
    await page.getByRole('button', { name: 'Start 4-minute walkthrough' }).click();

    let complete = false;
    for (let check = 1; check <= 26; check += 1) {
      await page.waitForTimeout(10_000);
      const status = await page.evaluate(() => ({
        time: document.querySelector('[data-time]')?.textContent,
        complete: document.body.dataset.walkthroughComplete === 'true',
      }));
      if (check % 3 === 0 || status.complete) {
        console.log(`recording ${status.time}`);
      }
      if (status.complete) {
        complete = true;
        break;
      }
    }

    if (!complete) {
      throw new Error('Walkthrough did not complete within 260 seconds');
    }

    await page.waitForTimeout(750);
    await context.close();
    await video.saveAs(outputPath);
    console.log(outputPath);
  } finally {
    if (browser.isConnected()) {
      await browser.close();
    }
  }
}


main().catch(error => {
  console.error(error.stack || error.message || String(error));
  process.exitCode = 1;
});
