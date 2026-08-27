# Bay State Auto Growth

A lightweight static website for Bay State Auto Growth, founded by Alpha Barrie. It is designed to turn Greater Boston auto-shop prospects into free audit requests and showcase a complete fictional auto-shop website.

Intended custom domain: `baystateautogrowth.com` (connect only after the domain is purchased and the deployment is approved).

## Public pages

- `/` — focused sales page and free-audit form
- `/demo/` — fictional Bay & Beacon Auto Care homepage
- `/demo/services.html` — fictional shop services and repair process
- `/demo/contact.html` — fictional shop contact and non-submitting appointment preview
- `/privacy.html` — inquiry privacy notice

The main form submits to the existing Formspree endpoint. The demo form is intentionally local-only and never transmits data.

The public business call number is `(224) 944-4044` (`tel:+12249444044`). WhatsApp Business is intentionally deferred. The homepage links to a clearly disclosed fictional sample-audit PDF; the silent rehearsal video remains private until Alpha records and approves the narration.

## Local preview

From PowerShell in the repository folder:

```powershell
python -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## Before publishing

1. Submit a real test inquiry and confirm Formspree notification delivery.
2. Review all contact copy, prices, and available founding-shop spots.
3. Update social-image URLs when the custom domain is connected.
4. Run the validation checks described in `docs/launch-checklist.md`.

The initials-based founder card is approved for launch. An approved headshot can replace it later without delaying publishing or outreach.

Deployment is intentionally manual. The existing Cloudflare Pages project should not be changed without explicit approval.

Cloudflare Pages project: `garage-growth-solutions`. The production branch is `main`; pushes to other enabled branches create preview deployments.

## Project knowledge

Start with `docs/index.md` for the launch checklist, acquisition scripts, free-audit template, and client delivery system. Keep real prospect and client information in the ignored `private/` directory or another private system—never in this public repository.
