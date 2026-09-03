# Project log

## [2026-08-28] launch | Two-page website approved for production

- Alpha approved publishing the two-page Audit & Trust and Websites & Growth redesign.
- Rechecked the release locally at phone, tablet, and desktop widths with no horizontal overflow or browser-console errors.
- Confirmed the fictional demo remains excluded from search indexing and returns visitors to the Website Services section.
- Published the approved source through the existing `main` branch and Cloudflare Pages Git deployment workflow.

## [2026-08-27] website | Two-page audit and growth service system

- Kept the main page focused on the free audit and Local Trust & Calls Setup while moving separately scoped work to a dedicated Websites & Growth page.
- Added introductory website and SEO pricing, clear project boundaries, an expanded Bay & Beacon demo showcase, and a separate project-consultation form using the verified Formspree endpoint.
- Reorganized the setup deliverables into four customer-friendly categories and rebuilt the Alpha Barrie section around direct support, approvals, scope, and client ownership.
- Preserved the fictional three-page demo itself while changing its return path to the new website-services section.
- Kept the narrated audit video unpublished, preserved the existing social image, and left production publishing pending Alpha's local review.
- Confirmed both real Formspree inquiry types returned success using clearly labeled reserved QA data; browser checks also covered success, error, reset, mobile menu, focus, responsive overflow, internal routes, and clean console behavior.

## [2026-08-26] website | Three-page demo and direct-call path

- Kept the Bay State homepage as a focused sales funnel while adding a clear free-audit versus $297 implementation comparison.
- Added the public business call number, a one-click mobile call action, and a disclosed sample-audit PDF preview; left WhatsApp and the unapproved silent video unpublished.
- Split the fictional Bay & Beacon website into Home, Services, and Contact pages with a consistent demo banner and non-submitting appointment preview.
- Defined the owner-approved, manual website-testimonial workflow and preserved permanent sample labels on fictional reviews.
- Confirmed the redesigned Formspree path with one clearly labeled QA submission using reserved test information; the endpoint returned success and the page displayed its success message.
- Alpha approved the completed local preview for production publishing; final live verification follows the deployment.

## [2026-08-26] sales asset | Fictional sample audit package

- Created a local-only, intentionally flawed Bay & Beacon Auto Care website for an honest fictional before-and-after demonstration.
- Updated the one-page audit with real browser screenshots from the sample before and improved demo.
- Recorded a continuous 4:01 browser walkthrough covering desktop, mobile, trust, contact, and appointment-path differences, with a word-for-word voice script for Alpha.
- Kept the generated fixture, PDF, video, and temporary browser evidence out of source control while retaining reusable build and recording scripts.
- Left the final outreach-video checkbox open until Alpha re-records and approves the video in his own voice.

## [2026-08-25] launch | Production site published

- Published the approved redesign at `https://garage-growth-solutions.pages.dev/` through the existing Cloudflare Pages project.
- Confirmed the production deployment is active from `main` and that the public homepage, demo, privacy page, imagery, Formspree endpoint, and demo navigation are available.
- Left the existing Pages domain and hosting account unchanged; future approved pushes to `main` now trigger production deployments.

## [2026-08-25] operations | Cloudflare production branch corrected

- Found that Cloudflare Pages still treated `old-version` as the production branch, causing the approved `main` release to build only as a preview.
- Changed the existing `garage-growth-solutions` project production branch to `main` while preserving its domain, Git connection, and automatic production deployments.
- Documented the production branch so future approved pushes publish through the expected path.

## [2026-08-25] launch | Site approved and production preflight passed

- Alpha approved the redesigned main site and fictional demo for publishing.
- Completed responsive checks at phone, tablet, desktop, and wide-desktop sizes with no horizontal overflow or broken images.
- Confirmed local page responses, navigation targets, JavaScript syntax, the $297 founding-shop price, demo disclosures, and Formspree delivery.

## [2026-08-25] validation | Formspree delivery fully confirmed

- Alpha confirmed the labeled test appeared in Formspree and the notification reached the configured email inbox.
- Closed the remaining Formspree delivery check; the earlier confusion came from checking a different email account.

## [2026-08-25] validation | Formspree accepted a live delivery test

- Submitted one clearly labeled test using reserved dummy information and the existing Formspree endpoint.
- Confirmed the endpoint returned success, the website displayed its success message, and the form reset.
- Left dashboard appearance and notification-email delivery pending for Alpha to confirm; SMS notifications are not part of the current setup.

## [2026-08-25] fix | Explicit demo navigation paths

- Replaced directory-style demo links with explicit `demo/index.html` paths so local Windows previews do not open a filesystem folder.
- Replaced demo return links with explicit `../index.html` paths while preserving the founder and audit section targets.

## [2026-08-25] decision | Launch with initials-based founder card

- Approved the finished `AB` founder card for launch and deferred the optional founder headshot.
- Removed the headshot from the publishing and outreach blockers.
- Changed the visible founder-card label from placeholder language to Alpha Barrie's name and role.

## [2026-08-25] planning | Immediate launch order and future growth guides

- Added an ordered list of the next launch actions, beginning with the founder headshot and ending with the first outreach cycle.
- Recorded a post-launch Shop Growth Guides backlog with three cornerstone articles and free-audit calls to action.
- Kept the guides outside the first-client launch gate so content production does not delay sales activity.

## [2026-08-25] refinement | Clear service scope and demo return paths

- Added plain-English explanations for every item in the Local Trust & Calls Setup, including the homepage copy pack and website trust review.
- Opened the main headline letter and line spacing while preserving the bold industrial design.
- Added a clear demo-banner button back to the main site and changed the Alpha Barrie creator link to open the founder section.
- Synchronized the detailed service scope with the client delivery kit.

## [2026-08-25] redesign | Focused sales site and fictional shop demo

- Repositioned the public brand as Bay State Auto Growth, founded by Alpha Barrie.
- Replaced the broad services page with a free-audit funnel and $297 Local Trust & Calls Setup.
- Added the fictional Bay & Beacon Auto Care demo at `/demo/`.
- Preserved the verified Formspree endpoint and removed the invalid nested form and submission-blocking placeholder behavior.
- Added the privacy notice, original generated imagery, responsive styling, accessible interaction states, and launch operating documents.
- Kept deployment manual and excluded real prospect/client data from source control.

## [2026-08-31] refinement | Consistent themes and centered service-switch light

- Standardized light and dark surfaces across the main site and fictional demo so cards, forms, headers, footers, and supporting sections follow the active appearance without leftover opposite-theme panels.
- Replaced hard-coded supporting-text colors with semantic theme colors and a dedicated readable orange text accent while preserving the brighter Bay State orange for light effects and large decorative elements.
- Reworked the selected service switch so its concealed orange light is centered behind the active lettering, removed the remaining lower-edge orange seam, and enlarged the switch to 400 × 58 px on wide desktops without changing mobile touch targets.
- Verified all six pages in light and dark modes at 320, 375, 768, 1024, and 1440 px with no horizontal overflow or console errors; also confirmed keyboard theme switching, saved state, 44 px theme controls, and reduced-motion behavior.
- Kept all changes local; no production deployment was performed.

## [2026-08-31] fix | Complete theme contrast and glass-switch parity

- Added semantic contrast tokens in `style.css` and `demo/demo.css`, then applied them to adaptive cards, forms, price options, process content, supporting text, and status messages across the main site and fictional demo.
- Explicitly themed the “02 · Complete presence” price card and corrected inherited light-mode consultation and offer-list colors so every rendered text audit passes in both appearances.
- Made the light-mode service switch match the dark-mode interaction: a borderless recessed track, subtle glass edge, centered black-orange active lettering, and the same restrained orange inactive hover/focus light.
- Versioned shared CSS and JavaScript references with `?v=20260831-3` on all six pages so browsers fetch the corrected theme assets instead of stale copies.
- Verified all six pages at the required responsive widths with no overflow or console errors, and completed a rendered contrast audit with no failures in either theme.

## [2026-09-02] refinement | Clearer small typography and warmer light mode

- Sources: `S-20260902-READABILITY` and `S-20260902-CSS` in `docs/sources.md`. Pages affected: this log and the source ledger; the index now links to the ledger.
- Established 14px small text, 15px form labels/supporting notes, and 16px body copy/list defaults using shared typography tokens in both stylesheets. Preserved brand marks, existing font families, large headings, and large price sizes; opened smaller bold labels and condensed subheadings with more letter/line spacing.
- Applied the approved cream, warm-gray panel, darker supporting-text, and border palette only to light mode. Corrected pale light-mode eyebrow inheritance and used the existing darker Bay State orange for headline accents to meet contrast on cream.
- Increased service-switch labels to 14px with mobile wrapping; preserved glass, lighting, focus, and selection behavior. Widened the main desktop header and prevented awkward phone/navigation wrapping. Adjusted demo metric-card padding and column sizing at narrow widths.
- Updated theme metadata and shared asset references to `?v=20260902-1` on all six pages; no JavaScript behavior or production dependencies changed.
- Passed 84 page/theme/viewport layout cases at 320, 375, 720, 768, 1024, 1280, and 1440px, with no content below 14px outside preserved brand marks, no text overflow, no header overlap, and no page errors. The 720px case checks the layout equivalent of 200% zoom on a 1440px screen; native browser toolbar zoom was unavailable in the headless test browser.
- Completed 1,236 rendered text/symbol contrast checks with no remaining failures after opening FAQ answers and allowing theme styles to settle; glass/photographic overlays require visual review rather than a flat-background calculation. Rating stars use the 3:1 graphical contrast threshold.
- Verified matching inactive hover light in both themes, 3px keyboard focus, service-page navigation and theme persistence, 44px appearance targets, mobile menu bounds, and reduced-motion transitions. `node --check theme.js` and `git diff --check` passed. Changes remain local; no deployment performed.
- Visually reviewed desktop/mobile screenshots of the switch/header, pricing cards, demo hero overlays, sample form, and privacy content in both appearances. Rechecked the privacy header after theme styles settled; its audit link remains readable. Native 200% toolbar zoom remains a manual verification item.

## [2026-09-03] release | Theme and readability production verification

- Sources: `S-20260903-RELEASE` in `docs/sources.md`. Alpha approved production publication with the September 2 "Merge/ deploy" request.
- Committed the approved website work on the existing `main` branch as `9e2f43d5fa1bbf769735208f7030ed8f369011f9`; no separate branch needed merging. Unrelated client-sales documents and generation tools remain local and uncommitted.
- Cloudflare Git deployment `f48ad291-7b14-4ad9-9591-0848cb45b4f5` completed successfully on September 2 at 21:56:44 UTC; confirmed it remains the production deployment on September 3. Live site: https://garage-growth-solutions.pages.dev/.
- All six public HTML pages and six CSS/JavaScript files returned HTTP 200 and matched the approved local source after normalizing line endings. All pages reference the refreshed theme assets.
- Passed 24 live page/theme/viewport checks (six pages, two themes, 375px and 1440px): no horizontal overflow, theme-state mismatches, page errors, or console errors. Service-page navigation and theme persistence across navigation/reload also passed. No live forms were submitted.
- Syntax checks passed for `theme.js`, `script.js`, and `demo/demo.js`. Corrected a Windows line ending in the documentation index detected by the staged whitespace check. Native 200% browser zoom remains a manual check; production metrics were not monitored continuously.
- Rollback target: previous successful Pages deployment `e23e9eea-a4f0-4d9b-ac55-2ec636930a65`, source `e2a640414a05fe143cd7026cc6c2e03ba1727d05`. Use it if page loading, theme initialization, or navigation regresses.
- This documentation-only follow-up uses Cloudflare's documented deployment-skip commit prefix; it does not change website files or replace the verified production release.
