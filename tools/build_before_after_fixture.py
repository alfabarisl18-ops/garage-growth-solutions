from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "output" / "audit-fixtures"
BEFORE_DIR = FIXTURE_ROOT / "bay-beacon-before"
WALKTHROUGH_DIR = FIXTURE_ROOT / "walkthrough"


BEFORE_HTML = dedent(
    """\
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="robots" content="noindex, nofollow">
      <title>Bay &amp; Beacon Auto Care - Fictional Sample Before</title>
      <link rel="icon" href="../../../assets/favicon.png" type="image/png">
      <link rel="stylesheet" href="before.css">
    </head>
    <body>
      <aside class="sample-warning">
        <strong>FICTIONAL SAMPLE BEFORE</strong>
        Intentionally flawed website used only for an audit demonstration. Nothing here is a real business claim.
      </aside>

      <div class="page-frame">
        <header class="old-header">
          <div class="wordmark">BAY &amp; BEACON <span>AUTO CARE</span></div>
          <div class="tagline">QUALITY SERVICE AT A FAIR PRICE!</div>
          <nav aria-label="Sample before navigation">
            <a href="#top">HOME</a>
            <a href="#services">ABOUT US</a>
            <a href="#services">SERVICES</a>
            <a href="#services">COUPONS</a>
            <a href="#services">FAQ</a>
            <a href="#contact">DIRECTIONS</a>
            <a href="#contact">CONTACT</a>
          </nav>
        </header>

        <main id="top">
          <section class="old-hero">
            <img src="../../../assets/demo-garage.webp" alt="Mechanic working in a repair garage">
            <div class="hero-copy">
              <h1>WELCOME TO BAY &amp; BEACON AUTO CARE</h1>
              <p>Your trusted source for all of your automotive needs. We provide quality service and customer satisfaction. Browse our website to learn more about our company.</p>
              <a class="learn-button" href="#services">LEARN MORE</a>
            </div>
          </section>

          <div class="marquee" aria-label="Sample promotion">*** ASK ABOUT OUR SPECIALS *** QUALITY WORK *** FRIENDLY SERVICE ***</div>

          <section class="old-section" id="services">
            <h2>OUR AUTO REPAIR SERVICES</h2>
            <div class="service-columns">
              <ul>
                <li>Auto Repair</li>
                <li>Brake Service</li>
                <li>Oil Changes</li>
                <li>Engine Work</li>
              </ul>
              <ul>
                <li>Diagnostics</li>
                <li>Maintenance</li>
                <li>Heating and Cooling</li>
                <li>Other Services</li>
              </ul>
              <div class="coupon-box">
                <strong>SAVE TODAY!</strong>
                <p>Call for current offers and details.</p>
                <button type="button">PRINT COUPON</button>
              </div>
            </div>
            <p class="wall-copy">We work on many different makes and models and provide many types of automotive services. Our experienced team is committed to meeting your automotive needs. Contact us to learn more about pricing, scheduling, warranties, availability, and the services we can provide for your vehicle.</p>
          </section>

          <section class="old-section company-section">
            <h2>WHY CHOOSE OUR COMPANY?</h2>
            <table>
              <tr><td>Experienced</td><td>Professional</td><td>Dependable</td></tr>
              <tr><td>Affordable</td><td>Local</td><td>Friendly</td></tr>
            </table>
            <p>Our goal is to provide the best possible service. Please contact us for more information.</p>
          </section>

          <section class="old-section contact-section" id="contact">
            <h2>CONTACT US</h2>
            <div class="contact-layout">
              <form data-before-form>
                <p class="form-disclosure">Demonstration form - nothing entered here is transmitted.</p>
                <input aria-label="Name" placeholder="Name">
                <input aria-label="Email" placeholder="Email">
                <textarea aria-label="Message" placeholder="Message"></textarea>
                <button type="submit">SUBMIT</button>
                <p data-before-status role="status"></p>
              </form>
              <div class="buried-details">
                <h3>SHOP INFORMATION</h3>
                <p>125 Example Street<br>Boston, MA 02128</p>
                <p>Phone: (617) 555-0148</p>
                <p>Monday-Friday: 7:30 AM-6:00 PM<br>Saturday: Call for hours<br>Sunday: Closed</p>
                <small>Reserved fictional address and phone number.</small>
              </div>
            </div>
          </section>
        </main>

        <footer>
          <span>Copyright Bay &amp; Beacon Auto Care</span>
          <a href="#top">Home</a> | <a href="#services">Services</a> | <a href="#contact">Contact</a>
        </footer>
      </div>

      <script>
        document.querySelector('[data-before-form]').addEventListener('submit', function (event) {
          event.preventDefault();
          event.currentTarget.querySelector('[data-before-status]').textContent = 'Demonstration only - this form sends nothing.';
        });
      </script>
    </body>
    </html>
    """
)


BEFORE_CSS = dedent(
    """\
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { margin: 0; color: #262626; background: #c7c7c7 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12'%3E%3Cpath d='M0 12L12 0' stroke='%23bdbdbd' stroke-width='1'/%3E%3C/svg%3E"); font-family: Arial, Helvetica, sans-serif; font-size: 12px; }
    .sample-warning { position: sticky; z-index: 20; top: 0; min-width: 1080px; padding: 8px 20px; color: #fff; background: #771d1d; border-bottom: 3px solid #ffcf4a; text-align: center; letter-spacing: .03em; }
    .sample-warning strong { margin-right: 18px; color: #ffdf72; }
    .page-frame { width: 1040px; margin: 18px auto 60px; border: 8px ridge #8a8a8a; background: #fff; box-shadow: 0 0 20px #0008; }
    .old-header { padding: 14px 18px 0; background: linear-gradient(#f7f7f7, #c8c8c8); border-bottom: 5px solid #123e72; }
    .wordmark { color: #173f70; font-family: Georgia, serif; font-size: 30px; font-weight: 700; text-shadow: 1px 1px #fff; }
    .wordmark span { color: #a72727; }
    .tagline { margin: 3px 0 12px; color: #777; font-size: 10px; letter-spacing: .22em; }
    nav { display: flex; width: 100%; border: 1px solid #555; background: linear-gradient(#335f91, #102f54); }
    nav a { flex: 1; padding: 8px 5px; border-right: 1px solid #778ca4; color: #fff; font-size: 10px; text-align: center; text-decoration: none; }
    nav a:last-child { border-right: 0; }
    .old-hero { height: 350px; display: grid; grid-template-columns: 55% 45%; padding: 18px; overflow: hidden; background: #e8e8e8; }
    .old-hero img { width: 100%; height: 314px; border: 6px solid #fff; object-fit: fill; box-shadow: 0 0 5px #555; filter: saturate(.65) contrast(.86); }
    .hero-copy { padding: 22px 18px; border: 1px solid #aaa; background: #f5f1df; }
    h1 { margin: 0 0 18px; color: #154779; font-family: Georgia, serif; font-size: 28px; line-height: 1.08; }
    .hero-copy p { line-height: 1.8; }
    .learn-button, button { display: inline-block; padding: 8px 13px; border: 3px outset #bbb; color: #fff; background: #b12727; font-size: 11px; font-weight: 700; text-decoration: none; }
    .marquee { padding: 8px; overflow: hidden; color: #ffed6b; background: #173e6f; font-weight: 700; text-align: center; word-spacing: 34px; }
    .old-section { padding: 24px 30px; border-top: 1px dotted #888; }
    .old-section h2 { margin: 0 0 20px; padding-bottom: 5px; border-bottom: 3px double #204e7e; color: #204e7e; font-family: Georgia, serif; font-size: 20px; }
    .service-columns { display: grid; grid-template-columns: 1fr 1fr 1.15fr; gap: 12px; }
    .service-columns ul { margin: 0; padding: 12px 12px 12px 30px; border: 1px solid #aaa; background: #f0f0f0; line-height: 2; }
    .coupon-box { padding: 15px; border: 4px dashed #d1a300; color: #5a4300; background: #fff3a6; text-align: center; transform: rotate(-1deg); }
    .coupon-box strong { display: block; color: #b12727; font-size: 22px; }
    .coupon-box button { color: #111; background: #e0e0e0; }
    .wall-copy { margin-top: 18px; color: #666; font-size: 11px; line-height: 1.65; text-align: justify; }
    .company-section { background: #e8eef5; }
    table { width: 100%; border-collapse: collapse; }
    td { padding: 8px; border: 1px solid #777; background: #fff; text-align: center; }
    .contact-section { padding-bottom: 35px; }
    .contact-layout { display: grid; grid-template-columns: 1.25fr .75fr; gap: 45px; }
    form { display: grid; gap: 7px; }
    input, textarea { width: 100%; padding: 6px; border: 1px inset #777; font: inherit; }
    textarea { min-height: 80px; }
    .form-disclosure { margin: 0 0 6px; color: #8b1f1f; font-weight: 700; }
    .buried-details { padding: 15px; border: 1px solid #aaa; background: #efefef; }
    footer { display: flex; justify-content: space-between; padding: 12px 18px; color: #ccc; background: #173e6f; font-size: 10px; }
    footer a { color: #fff; }

    /* Intentionally poor mobile behavior for this fictional audit fixture. */
    @media (max-width: 600px) {
      body { font-size: 11px; }
      .page-frame { margin-left: 12px; }
      .sample-warning { text-align: left; }
      nav a { padding-inline: 2px; font-size: 9px; }
    }
    """
)


WALKTHROUGH_HTML = dedent(
    """\
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="robots" content="noindex, nofollow">
      <title>Bay &amp; Beacon Before-and-After Walkthrough</title>
      <link rel="icon" href="../../../assets/favicon.png" type="image/png">
      <style>
        :root { color-scheme: dark; font-family: Arial, Helvetica, sans-serif; }
        * { box-sizing: border-box; }
        html, body { width: 100%; height: 100%; margin: 0; overflow: hidden; background: #0f100e; }
        body { display: grid; grid-template-rows: 66px 1fr 86px; color: #fffdf8; }
        header { display: flex; align-items: center; justify-content: space-between; padding: 0 34px; border-bottom: 1px solid #383934; background: #171815; }
        .brand { font-weight: 900; letter-spacing: .08em; }
        .brand span { color: #f15a24; }
        .disclosure { color: #b7b8b0; font-size: 13px; }
        .stage { position: relative; display: grid; place-items: center; overflow: hidden; background: radial-gradient(circle at center, #292a25, #11120f 72%); }
        .device { position: relative; overflow: hidden; border: 1px solid #55564f; border-radius: 9px; background: #fff; box-shadow: 0 22px 80px #000a; transform-origin: center; transition: width .7s ease, height .7s ease; }
        .device.desktop { width: 1160px; height: 548px; }
        .device.mobile { width: 375px; height: 548px; border-width: 8px; border-color: #30312d; border-radius: 24px; }
        .browser-bar { height: 30px; display: flex; align-items: center; gap: 7px; padding: 0 12px; border-bottom: 1px solid #cacaca; color: #555; background: #ededed; font-size: 11px; }
        .browser-bar i { width: 8px; height: 8px; border-radius: 50%; background: #b0b0b0; }
        .browser-bar span { flex: 1; overflow: hidden; text-align: center; text-overflow: ellipsis; white-space: nowrap; }
        iframe { width: 100%; height: calc(100% - 30px); border: 0; background: #fff; }
        .state-label { position: absolute; z-index: 5; top: 14px; left: 18px; padding: 10px 15px; border-radius: 3px; color: #fff; background: #9d2925; box-shadow: 0 6px 25px #0006; font-size: 13px; font-weight: 900; letter-spacing: .1em; }
        .state-label.after { color: #171815; background: #f15a24; }
        .callout { position: absolute; z-index: 6; max-width: 360px; padding: 12px 15px; border-left: 5px solid #f15a24; color: #24251f; background: #fffdf8; box-shadow: 0 10px 35px #0007; font-size: 14px; font-weight: 700; line-height: 1.35; opacity: 0; transform: translateY(8px); transition: opacity .25s ease, transform .25s ease; }
        .callout.visible { opacity: 1; transform: none; }
        .callout.top-right { top: 70px; right: 38px; }
        .callout.bottom-right { right: 38px; bottom: 28px; }
        .callout.bottom-left { bottom: 28px; left: 38px; }
        footer { display: grid; grid-template-columns: 1fr 360px; align-items: center; gap: 30px; padding: 13px 34px; border-top: 1px solid #383934; background: #171815; }
        .scene-copy small { display: block; margin-bottom: 4px; color: #f15a24; font-size: 11px; font-weight: 900; letter-spacing: .12em; }
        .scene-copy strong { display: block; margin-bottom: 3px; font-size: 18px; }
        .scene-copy p { margin: 0; color: #babbb3; font-size: 13px; }
        .controls { display: grid; grid-template-columns: auto 1fr; gap: 10px 14px; align-items: center; }
        button { min-height: 42px; padding: 8px 14px; border: 0; border-radius: 3px; color: #171815; background: #f15a24; font-weight: 900; cursor: pointer; }
        button:disabled { opacity: .55; cursor: default; }
        .time { color: #d2d2ca; font-variant-numeric: tabular-nums; text-align: right; }
        .progress { grid-column: 1 / -1; height: 5px; overflow: hidden; background: #383934; }
        .progress span { display: block; width: 0; height: 100%; background: #f15a24; }
        @media (prefers-reduced-motion: reduce) { *, *::before, *::after { scroll-behavior: auto !important; transition: none !important; } }
      </style>
    </head>
    <body>
      <header>
        <div class="brand">BAY STATE <span>AUTO GROWTH</span></div>
        <div class="disclosure">Fictional before-and-after demonstration - not an actual client result</div>
      </header>

      <main class="stage">
        <div class="state-label" data-state-label>SAMPLE BEFORE</div>
        <div class="device desktop" data-device>
          <div class="browser-bar"><i></i><i></i><i></i><span data-address>bayandbeacon.sample/before</span></div>
          <iframe title="Bay and Beacon website state" data-site src="../bay-beacon-before/index.html"></iframe>
        </div>
        <div class="callout top-right" data-callout></div>
      </main>

      <footer>
        <div class="scene-copy">
          <small data-kicker>FICTIONAL AUDIT</small>
          <strong data-title>Bay &amp; Beacon Auto Care</strong>
          <p data-note>Press start when your screen recorder and microphone are ready.</p>
        </div>
        <div class="controls">
          <button type="button" data-start>Start 4-minute walkthrough</button>
          <span class="time" data-time>0:00 / 4:00</span>
          <span class="progress" aria-hidden="true"><span data-progress></span></span>
        </div>
      </footer>

      <script>
        const BEFORE = '../bay-beacon-before/index.html';
        const AFTER = '../../../demo/index.html';
        const TOTAL = 240;
        const speed = Math.max(0.25, Number(new URLSearchParams(location.search).get('speed')) || 1);
        const scenes = [
          { at: 0, state: 'before', mode: 'desktop', target: '#top', kicker: 'FICTIONAL AUDIT', title: 'Sample before: what a customer sees first', note: 'This is an intentionally flawed version of the fictional Bay & Beacon site.', callout: 'Start with the customer experience, not technical jargon.', position: 'top-right' },
          { at: 15, state: 'before', mode: 'desktop', target: '#top', kicker: 'PRIORITY 01', title: 'The first impression is generic', note: 'The opening does not state East Boston, explain the repair experience, or present a strong next action.', callout: 'Generic promise + weak Learn more button', position: 'bottom-right' },
          { at: 50, state: 'before', mode: 'desktop', target: '#services', kicker: 'PRIORITY 02', title: 'Services are listed without helpful context', note: 'Customers see broad labels, clutter, and no trust proof to reduce uncertainty.', callout: 'No reviews, warranty, certification, or clear repair process', position: 'top-right' },
          { at: 82, state: 'before', mode: 'desktop', target: '#contact', kicker: 'PRIORITY 03', title: 'The contact path is buried', note: 'The phone, hours, and form appear near the bottom after the customer has done unnecessary searching.', callout: 'Contact details arrive too late', position: 'bottom-left' },
          { at: 110, state: 'before', mode: 'mobile', target: '#top', kicker: 'MOBILE CHECK', title: 'The layout does not adapt to a phone', note: 'The fixed-width page forces horizontal scrolling and keeps the call action out of view.', callout: 'No visible mobile call button', position: 'top-right' },
          { at: 140, state: 'after', mode: 'desktop', target: '#top', kicker: 'IMPROVED DEMO', title: 'The first screen now answers the important questions', note: 'Location, service promise, hours, trust proof, call, and request-service actions are immediately visible.', callout: 'Specific message + two obvious actions', position: 'bottom-right' },
          { at: 170, state: 'after', mode: 'desktop', target: '#services', kicker: 'CLEAR SERVICES', title: 'Service information is easier to scan', note: 'Each service explains the customer problem it covers, supported by ratings, warranty, and certification signals.', callout: 'Useful descriptions replace vague labels', position: 'top-right' },
          { at: 197, state: 'after', mode: 'desktop', target: '#why-us', kicker: 'VISIBLE TRUST', title: 'The repair process reduces uncertainty', note: 'Customers can see how approval works, then review clearly labeled sample testimonials.', callout: 'Process, proof, and expectations work together', position: 'bottom-left' },
          { at: 217, state: 'after', mode: 'mobile', target: '#top', kicker: 'MOBILE IMPROVEMENT', title: 'The phone experience supports immediate action', note: 'The layout fits the screen and the Call the shop action remains visible.', callout: 'Mobile call action stays within reach', position: 'top-right' },
          { at: 234, state: 'after', mode: 'desktop', target: '#appointment', offset: 170, kicker: 'NEXT STEP', title: 'A complete path from trust to request', note: 'The improved demo ends with clear contact details and a safe appointment preview. Request your free audit at garage-growth-solutions.pages.dev.', callout: 'Local Trust & Calls Setup - $297 for the first three shops', position: 'bottom-left' }
        ];

        const frame = document.querySelector('[data-site]');
        const device = document.querySelector('[data-device]');
        const stateLabel = document.querySelector('[data-state-label]');
        const address = document.querySelector('[data-address]');
        const callout = document.querySelector('[data-callout]');
        const kicker = document.querySelector('[data-kicker]');
        const title = document.querySelector('[data-title]');
        const note = document.querySelector('[data-note]');
        const time = document.querySelector('[data-time]');
        const progress = document.querySelector('[data-progress]');
        const start = document.querySelector('[data-start]');
        let startedAt = null;
        let sceneIndex = -1;
        let playing = false;

        function formatTime(seconds) {
          const safe = Math.max(0, Math.min(TOTAL, Math.floor(seconds)));
          return `${Math.floor(safe / 60)}:${String(safe % 60).padStart(2, '0')}`;
        }

        function waitForFrame() {
          return new Promise(resolve => {
            if (frame.contentDocument && frame.contentDocument.readyState === 'complete') resolve();
            else frame.addEventListener('load', resolve, { once: true });
          });
        }

        async function applyScene(nextIndex) {
          const scene = scenes[nextIndex];
          const source = scene.state === 'before' ? BEFORE : AFTER;
          const currentSource = frame.getAttribute('src');
          if (currentSource !== source) {
            frame.setAttribute('src', source);
            await waitForFrame();
          }
          const previousMode = device.classList.contains('mobile') ? 'mobile' : 'desktop';
          device.className = `device ${scene.mode}`;
          if (previousMode !== scene.mode) {
            await new Promise(resolve => setTimeout(resolve, 850));
          }
          stateLabel.textContent = scene.state === 'before' ? 'SAMPLE BEFORE' : 'IMPROVED DEMO';
          stateLabel.className = `state-label ${scene.state === 'after' ? 'after' : ''}`;
          address.textContent = scene.state === 'before' ? 'bayandbeacon.sample/before' : 'garage-growth-solutions.pages.dev/demo/';
          kicker.textContent = scene.kicker;
          title.textContent = scene.title;
          note.textContent = scene.note;
          callout.textContent = scene.callout;
          callout.className = `callout ${scene.position}`;
          requestAnimationFrame(() => callout.classList.add('visible'));
          const doc = frame.contentDocument;
          const target = doc ? doc.querySelector(scene.target) : null;
          const top = target && scene.mode === 'desktop' ? target.getBoundingClientRect().top + frame.contentWindow.scrollY - (scene.offset || 0) : 0;
          frame.contentWindow.scrollTo({ top, behavior: 'smooth' });
        }

        async function tick(timestamp) {
          if (!playing) return;
          if (startedAt === null) startedAt = timestamp;
          const elapsed = Math.min(TOTAL, ((timestamp - startedAt) / 1000) * speed);
          const nextIndex = scenes.findLastIndex(scene => elapsed >= scene.at);
          if (nextIndex !== sceneIndex) {
            sceneIndex = nextIndex;
            await applyScene(sceneIndex);
          }
          time.textContent = `${formatTime(elapsed)} / 4:00`;
          progress.style.width = `${(elapsed / TOTAL) * 100}%`;
          if (elapsed >= TOTAL) {
            playing = false;
            start.textContent = 'Replay walkthrough';
            start.disabled = false;
            document.body.dataset.walkthroughComplete = 'true';
            return;
          }
          requestAnimationFrame(tick);
        }

        start.addEventListener('click', async () => {
          start.disabled = true;
          document.body.dataset.walkthroughComplete = 'false';
          startedAt = null;
          sceneIndex = -1;
          playing = true;
          frame.setAttribute('src', BEFORE);
          await waitForFrame();
          requestAnimationFrame(tick);
        });
      </script>
    </body>
    </html>
    """
)


def write_text(path: Path, value: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def main():
    write_text(BEFORE_DIR / "index.html", BEFORE_HTML)
    write_text(BEFORE_DIR / "before.css", BEFORE_CSS)
    write_text(WALKTHROUGH_DIR / "index.html", WALKTHROUGH_HTML)
    print(BEFORE_DIR / "index.html")
    print(WALKTHROUGH_DIR / "index.html")


if __name__ == "__main__":
    main()
