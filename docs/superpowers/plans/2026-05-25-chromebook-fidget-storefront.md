# Chromebook Fidget Storefront Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Chromebook-friendly fidget-toy storefront with a browse page and individual product pages using only HTML, CSS, JSON, and JavaScript.

**Architecture:** Keep the site fully static and dependency-free. Use `index.html` for the storefront grid, `product.html` for a reusable detail page keyed by `?id=...`, a single shared stylesheet, and small JavaScript modules that fetch product data from JSON and render the UI.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, JSON, optional local static server via `python3 -m http.server`

---

## File Structure

- Create: `index.html` - storefront landing page with featured intro and product grid mount point
- Create: `product.html` - reusable product detail page with gallery, specs, and CTA mount point
- Create: `styles/site.css` - shared responsive styling tuned for Chromebook screens
- Create: `scripts/app.js` - landing page render logic
- Create: `scripts/product.js` - product detail page render logic
- Create: `scripts/data.js` - shared product fetch and lookup helpers
- Create: `data/products.json` - product catalog content
- Create: `assets/icons/cart.svg` - simple decorative cart icon
- Create: `assets/icons/spark.svg` - simple decorative sparkle icon
- Create: `README.md` - run instructions and content editing notes

## Implementation Notes

- Keep JavaScript as ES modules to avoid bundlers.
- Use `fetch('./data/products.json')` from both pages, so local testing should be done with a simple static server instead of opening files directly.
- Keep images optional for v1. Use gradients, badges, and emoji-safe text fallbacks instead of real product photography.
- Keep layout light: one CSS file, one JSON file, two page scripts, one shared data helper.
- Product pages should use query strings instead of generating many HTML files. This is still “product pages” but much easier to maintain.
- Avoid third-party assets in v1 so the site stays easy to host offline or on simple static hosts.

### Task 1: Scaffold the static site structure

**Files:**
- Create: `index.html`
- Create: `product.html`
- Create: `styles/site.css`
- Create: `scripts/app.js`
- Create: `scripts/product.js`
- Create: `scripts/data.js`
- Create: `data/products.json`
- Create: `assets/icons/cart.svg`
- Create: `assets/icons/spark.svg`

- [ ] **Step 1: Create the base landing page shell**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Fidget Orbit</title>
    <link rel="stylesheet" href="./styles/site.css" />
    <script type="module" src="./scripts/app.js" defer></script>
  </head>
  <body data-page="home">
    <header class="site-header">
      <a class="brand" href="./index.html">Fidget Orbit</a>
      <nav class="site-nav" aria-label="Primary">
        <a href="#catalog">Shop</a>
        <a href="#why">Why it works</a>
      </nav>
    </header>

    <main>
      <section class="hero">
        <p class="eyebrow">Quiet focus tools for school bags and desk trays</p>
        <h1>Small fidgets. Big calm.</h1>
        <p class="hero-copy">
          Lightweight toys chosen for Chromebook users, classroom breaks, and
          easy browsing on smaller screens.
        </p>
        <a class="button button-primary" href="#catalog">Browse toys</a>
      </section>

      <section class="why-strip" id="why" aria-label="Store benefits">
        <article>
          <h2>Fast pages</h2>
          <p>No heavy framework. Just quick static files.</p>
        </article>
        <article>
          <h2>Easy browsing</h2>
          <p>Large buttons, simple copy, and card-first navigation.</p>
        </article>
        <article>
          <h2>Kid-safe info</h2>
          <p>Each item includes age notes, feel, and quietness level.</p>
        </article>
      </section>

      <section class="catalog-section" id="catalog">
        <div class="section-heading">
          <p class="eyebrow">Catalog</p>
          <h2>Pick a fidget by feel</h2>
        </div>
        <div id="product-grid" class="product-grid" aria-live="polite"></div>
      </section>
    </main>
  </body>
</html>
```

- [ ] **Step 2: Create the reusable product page shell**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Product Details | Fidget Orbit</title>
    <link rel="stylesheet" href="./styles/site.css" />
    <script type="module" src="./scripts/product.js" defer></script>
  </head>
  <body data-page="product">
    <header class="site-header">
      <a class="brand" href="./index.html">Fidget Orbit</a>
      <nav class="site-nav" aria-label="Primary">
        <a href="./index.html#catalog">Back to shop</a>
      </nav>
    </header>

    <main id="product-detail" class="product-detail" aria-live="polite"></main>
  </body>
</html>
```

- [ ] **Step 3: Create the shared stylesheet placeholder**

```css
:root {
  --bg: #f7f3e8;
  --surface: #fffaf0;
  --surface-strong: #fff;
  --text: #1f2933;
  --muted: #52606d;
  --line: #d9cbb3;
  --accent: #f05d23;
  --accent-deep: #b23a11;
  --accent-soft: #ffd166;
  --shadow: 0 18px 50px rgba(31, 41, 51, 0.12);
  --radius-lg: 24px;
  --radius-md: 18px;
  --radius-sm: 12px;
  --max-width: 1100px;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Trebuchet MS", "Segoe UI", sans-serif;
  color: var(--text);
  background:
    radial-gradient(circle at top left, rgba(255, 209, 102, 0.5), transparent 32%),
    linear-gradient(180deg, #fff8ec 0%, #f7f3e8 100%);
}
```

- [ ] **Step 4: Create the shared data helper**

```js
const DATA_URL = "./data/products.json";

export async function loadProducts() {
  const response = await fetch(DATA_URL);

  if (!response.ok) {
    throw new Error(`Failed to load products: ${response.status}`);
  }

  return response.json();
}

export async function loadProductById(productId) {
  const products = await loadProducts();
  return products.find((product) => product.id === productId) ?? null;
}
```

- [ ] **Step 5: Stub the page modules so the browser loads cleanly**

```js
// scripts/app.js
console.log("Home page ready");
```

```js
// scripts/product.js
console.log("Product page ready");
```

- [ ] **Step 6: Seed the initial product JSON**

```json
[
  {
    "id": "nebula-loop",
    "name": "Nebula Loop",
    "price": 12,
    "quietLevel": "quiet",
    "ageRange": "8+",
    "category": "ring",
    "tagline": "A smooth rolling ring for under-desk focus.",
    "description": "Soft silicone beads glide around a flexible loop for low-noise movement during homework or class breaks.",
    "colors": ["Citrus", "Sky", "Graphite"],
    "features": ["Silent rolling motion", "Pocket-friendly size", "Washable silicone"],
    "gradient": "sunrise"
  },
  {
    "id": "pixel-pop-pad",
    "name": "Pixel Pop Pad",
    "price": 16,
    "quietLevel": "medium",
    "ageRange": "6+",
    "category": "popper",
    "tagline": "Bright pops with a sturdy square shape.",
    "description": "A compact silicone grid that gives tactile feedback without taking over a Chromebook tray table.",
    "colors": ["Lime", "Berry", "Ocean"],
    "features": ["Easy wipe-clean surface", "Thumb-sized bubbles", "Travel-ready shape"],
    "gradient": "arcade"
  },
  {
    "id": "comet-click-chain",
    "name": "Comet Click Chain",
    "price": 10,
    "quietLevel": "medium",
    "ageRange": "10+",
    "category": "chain",
    "tagline": "A linked click toy with just enough texture.",
    "description": "Rotating links provide repeatable motion for busy hands and quick reset between tasks.",
    "colors": ["Steel", "Coral"],
    "features": ["Textured grip", "Clip-on loop", "Built for backpacks"],
    "gradient": "ember"
  }
]
```

- [ ] **Step 7: Add simple inline SVG icons**

```svg
<!-- assets/icons/cart.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <path d="M10 14h8l6 24h24l8-18H22" stroke="#1f2933" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="28" cy="50" r="4" fill="#f05d23"/>
  <circle cx="48" cy="50" r="4" fill="#f05d23"/>
</svg>
```

```svg
<!-- assets/icons/spark.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <path d="M32 8l4 20 20 4-20 4-4 20-4-20-20-4 20-4 4-20Z" fill="#ffd166" stroke="#1f2933" stroke-width="3"/>
</svg>
```

- [ ] **Step 8: Verify files exist**

Run: `rtk find . -maxdepth 3 -type f | sort`
Expected: file list includes `index.html`, `product.html`, `styles/site.css`, `scripts/app.js`, `scripts/product.js`, `scripts/data.js`, `data/products.json`, `assets/icons/cart.svg`, and `assets/icons/spark.svg`

- [ ] **Step 9: Commit the scaffold**

```bash
rtk git add index.html product.html styles/site.css scripts/app.js scripts/product.js scripts/data.js data/products.json assets/icons/cart.svg assets/icons/spark.svg
rtk git commit -m "Create static storefront scaffold

Constraint: No framework or build tooling for v1
Rejected: Separate HTML file per product | higher maintenance than query-driven page
Confidence: high
Scope-risk: narrow
Directive: Keep first version dependency-free and easy to host
Tested: Verified scaffold files exist
Not-tested: Browser rendering"
```

### Task 2: Render the storefront landing page from JSON

**Files:**
- Modify: `scripts/app.js`
- Modify: `styles/site.css`
- Modify: `index.html`
- Test: `index.html` via local static server

- [ ] **Step 1: Replace the landing page stub with render logic**

```js
import { loadProducts } from "./data.js";

const productGrid = document.querySelector("#product-grid");

function getGradientClass(name) {
  return `theme-${name}`;
}

function renderProductCard(product) {
  return `
    <article class="product-card ${getGradientClass(product.gradient)}">
      <p class="product-meta">${product.category} · ${product.quietLevel}</p>
      <h3>${product.name}</h3>
      <p class="product-tagline">${product.tagline}</p>
      <p class="product-price">$${product.price}</p>
      <ul class="chip-list" aria-label="${product.name} quick details">
        <li>${product.ageRange}</li>
        <li>${product.colors.length} colors</li>
        <li>${product.features[0]}</li>
      </ul>
      <a class="button button-secondary" href="./product.html?id=${product.id}">
        View details
      </a>
    </article>
  `;
}

async function initHomePage() {
  try {
    const products = await loadProducts();
    productGrid.innerHTML = products.map(renderProductCard).join("");
  } catch (error) {
    productGrid.innerHTML = `
      <p class="status-card" role="alert">
        We could not load the catalog right now. Try refreshing the page.
      </p>
    `;
    console.error(error);
  }
}

initHomePage();
```

- [ ] **Step 2: Add a loading fallback in the landing page markup**

```html
<div id="product-grid" class="product-grid" aria-live="polite" aria-busy="true">
  <p class="status-card">Loading catalog...</p>
</div>
```

- [ ] **Step 3: Extend the stylesheet for layout and cards**

```css
.site-header,
.hero,
.why-strip,
.catalog-section,
.product-detail {
  width: min(calc(100% - 2rem), var(--max-width));
  margin: 0 auto;
}

.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0;
}

.brand,
.site-nav a {
  color: var(--text);
  text-decoration: none;
  font-weight: 700;
}

.site-nav {
  display: flex;
  gap: 1rem;
}

.hero {
  padding: 3rem 0 2rem;
}

.hero h1,
.section-heading h2 {
  margin: 0;
  line-height: 0.95;
  font-size: clamp(2.5rem, 5vw, 4.5rem);
}

.hero-copy,
.product-tagline,
.status-card,
.why-strip p {
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.6;
}

.eyebrow,
.product-meta {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.78rem;
  color: var(--accent-deep);
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.85rem 1.2rem;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 700;
}

.button-primary {
  color: white;
  background: var(--accent);
}

.button-secondary {
  color: var(--text);
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(31, 41, 51, 0.12);
}

.why-strip {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  margin-top: 1rem;
}

.why-strip article,
.product-card,
.status-card {
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(31, 41, 51, 0.08);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow);
}

.why-strip article,
.status-card {
  padding: 1rem 1.1rem;
}

.catalog-section {
  padding: 3rem 0 4rem;
}

.product-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  margin-top: 1.5rem;
}

.product-card {
  padding: 1.2rem;
}

.product-card h3,
.product-price {
  margin: 0.5rem 0;
}

.chip-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 0;
  margin: 1rem 0 1.2rem;
  list-style: none;
}

.chip-list li {
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(31, 41, 51, 0.08);
  font-size: 0.9rem;
}

.theme-sunrise {
  background: linear-gradient(180deg, #fff8de 0%, #fff 100%);
}

.theme-arcade {
  background: linear-gradient(180deg, #dcfff7 0%, #fff 100%);
}

.theme-ember {
  background: linear-gradient(180deg, #ffe3d6 0%, #fff 100%);
}
```

- [ ] **Step 4: Run a local static server**

Run: `rtk python3 -m http.server 4173`
Expected: terminal shows `Serving HTTP on`

- [ ] **Step 5: Open the home page and verify behavior**

Run: `rtk curl -I http://127.0.0.1:4173/`
Expected: `HTTP/1.0 200 OK`

Manual check:
- hero loads without layout break
- three product cards render
- each card has a working `View details` link

- [ ] **Step 6: Commit the landing page rendering work**

```bash
rtk git add index.html styles/site.css scripts/app.js
rtk git commit -m "Render storefront from product JSON

Constraint: Keep catalog data-driven with one source of truth
Rejected: Hardcoded product cards in HTML | duplicates content and slows updates
Confidence: high
Scope-risk: narrow
Directive: Add new products in JSON before touching UI templates
Tested: Home page renders via local static server
Not-tested: Keyboard-only traversal"
```

### Task 3: Build the reusable product detail page

**Files:**
- Modify: `scripts/product.js`
- Modify: `styles/site.css`
- Modify: `product.html`

- [ ] **Step 1: Replace the product page stub with query-driven rendering**

```js
import { loadProductById } from "./data.js";

const detailRoot = document.querySelector("#product-detail");
const params = new URLSearchParams(window.location.search);
const productId = params.get("id");

function renderMissingState() {
  detailRoot.innerHTML = `
    <section class="status-card">
      <p class="eyebrow">Catalog note</p>
      <h1>We could not find that toy.</h1>
      <p class="hero-copy">Return to the catalog and choose another fidget.</p>
      <a class="button button-primary" href="./index.html#catalog">Back to shop</a>
    </section>
  `;
}

function renderProduct(product) {
  detailRoot.innerHTML = `
    <section class="detail-hero ${`theme-${product.gradient}`}">
      <div class="detail-copy">
        <p class="eyebrow">${product.category} · ${product.quietLevel}</p>
        <h1>${product.name}</h1>
        <p class="hero-copy">${product.description}</p>
        <div class="detail-actions">
          <span class="price-badge">$${product.price}</span>
          <a class="button button-primary" href="./index.html#catalog">Keep shopping</a>
        </div>
      </div>
      <aside class="detail-panel">
        <h2>Quick facts</h2>
        <ul class="detail-list">
          <li><strong>Age:</strong> ${product.ageRange}</li>
          <li><strong>Colors:</strong> ${product.colors.join(", ")}</li>
          <li><strong>Feel:</strong> ${product.tagline}</li>
        </ul>
      </aside>
    </section>

    <section class="detail-body">
      <article class="detail-section">
        <h2>Why students like it</h2>
        <ul class="feature-list">
          ${product.features.map((feature) => `<li>${feature}</li>`).join("")}
        </ul>
      </article>
    </section>
  `;
}

async function initProductPage() {
  if (!productId) {
    renderMissingState();
    return;
  }

  try {
    const product = await loadProductById(productId);

    if (!product) {
      renderMissingState();
      return;
    }

    document.title = `${product.name} | Fidget Orbit`;
    renderProduct(product);
  } catch (error) {
    renderMissingState();
    console.error(error);
  }
}

initProductPage();
```

- [ ] **Step 2: Add a loading state to the product page shell**

```html
<main id="product-detail" class="product-detail" aria-live="polite">
  <p class="status-card">Loading product...</p>
</main>
```

- [ ] **Step 3: Extend the stylesheet for the product detail layout**

```css
.product-detail {
  padding: 2rem 0 4rem;
}

.detail-hero {
  display: grid;
  gap: 1rem;
  grid-template-columns: 2fr 1fr;
  padding: 1.25rem;
  border-radius: var(--radius-lg);
  border: 1px solid rgba(31, 41, 51, 0.08);
  box-shadow: var(--shadow);
}

.detail-panel,
.detail-section {
  background: rgba(255, 255, 255, 0.75);
  border-radius: var(--radius-md);
  padding: 1rem;
  border: 1px solid rgba(31, 41, 51, 0.08);
}

.detail-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1rem;
}

.price-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.7rem 1rem;
  border-radius: 999px;
  background: #1f2933;
  color: white;
  font-weight: 700;
}

.detail-list,
.feature-list {
  margin: 0;
  padding-left: 1.2rem;
  line-height: 1.7;
}

.detail-body {
  margin-top: 1.25rem;
}
```

- [ ] **Step 4: Verify product routes work**

Run: `rtk curl -I "http://127.0.0.1:4173/product.html?id=nebula-loop"`
Expected: `HTTP/1.0 200 OK`

Manual check:
- valid `id` shows matching title and details
- missing `id` shows a clear fallback state
- “Back to shop” and “Keep shopping” return to the catalog

- [ ] **Step 5: Commit the product page**

```bash
rtk git add product.html styles/site.css scripts/product.js
rtk git commit -m "Add reusable product detail page

Constraint: Product detail must stay static-host friendly
Rejected: Generated HTML page per SKU | unnecessary for a three-item starter catalog
Confidence: high
Scope-risk: narrow
Directive: Preserve the query-driven route shape unless SEO needs change
Tested: Product detail page renders for valid and missing ids
Not-tested: Browser back/forward flow"
```

### Task 4: Tune the UI for Chromebook-sized screens and accessibility

**Files:**
- Modify: `styles/site.css`
- Modify: `index.html`
- Modify: `product.html`

- [ ] **Step 1: Add accessible focus styles and smaller-screen behavior**

```css
a:focus-visible,
button:focus-visible {
  outline: 3px solid var(--accent-soft);
  outline-offset: 3px;
}

@media (max-width: 840px) {
  .site-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .hero {
    padding-top: 2rem;
  }

  .detail-hero {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 560px) {
  .site-header,
  .hero,
  .why-strip,
  .catalog-section,
  .product-detail {
    width: min(calc(100% - 1rem), var(--max-width));
  }

  .hero h1,
  .section-heading h2 {
    font-size: clamp(2rem, 10vw, 3rem);
  }

  .product-grid {
    grid-template-columns: 1fr;
  }

  .button {
    width: 100%;
  }
}
```

- [ ] **Step 2: Improve semantic labels in the page markup**

```html
<!-- index.html -->
<main id="main-content">
```

```html
<!-- product.html -->
<main id="product-detail" class="product-detail" aria-live="polite" aria-busy="true">
```

Note: when implementing, also remove `aria-busy="true"` in JavaScript after content finishes rendering.

- [ ] **Step 3: Update page scripts to clear loading state**

```js
// Add to scripts/app.js after successful or failed render
productGrid.removeAttribute("aria-busy");
```

```js
// Add to scripts/product.js after successful or fallback render
detailRoot.removeAttribute("aria-busy");
```

- [ ] **Step 4: Manual accessibility smoke test**

Manual check:
- tab order reaches nav, primary actions, and product links
- focus ring is visible on both pages
- no text overlaps at 1366x768 viewport
- buttons remain easy to tap on touchscreens

- [ ] **Step 5: Commit the responsive and accessibility polish**

```bash
rtk git add index.html product.html styles/site.css scripts/app.js scripts/product.js
rtk git commit -m "Tune storefront for Chromebook screens

Constraint: Primary target is smaller classroom laptops
Rejected: Desktop-only dense card layout | hurts readability on 11-13 inch displays
Confidence: medium
Scope-risk: narrow
Directive: Test all new sections at 1366x768 before shipping
Tested: Manual responsive and keyboard smoke checks
Not-tested: Screen reader pass"
```

### Task 5: Add setup docs and content editing guidance

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the run and edit instructions**

````md
# Fidget Orbit

Simple static storefront for fidget toys. No build step.

## Run locally

```bash
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173`.

## Edit products

Update `data/products.json`.

Each product needs:

- `id`
- `name`
- `price`
- `quietLevel`
- `ageRange`
- `category`
- `tagline`
- `description`
- `colors`
- `features`
- `gradient`

## File map

- `index.html` - storefront
- `product.html` - product detail page
- `styles/site.css` - all styling
- `scripts/data.js` - shared catalog loading
- `scripts/app.js` - storefront rendering
- `scripts/product.js` - product detail rendering
````

- [ ] **Step 2: Verify the README matches the shipped structure**

Run: `rtk sed -n '1,200p' README.md`
Expected: README mentions all final file paths and local run command

- [ ] **Step 3: Commit the docs**

```bash
rtk git add README.md
rtk git commit -m "Document static storefront workflow

Constraint: Future edits should stay easy for non-framework users
Rejected: Omit docs and rely on file names | raises onboarding cost
Confidence: high
Scope-risk: narrow
Directive: Keep README updated when product schema changes
Tested: README paths and run command reviewed
Not-tested: External hosting guide"
```

### Task 6: Final verification and release-ready smoke check

**Files:**
- Verify only: `index.html`, `product.html`, `styles/site.css`, `scripts/app.js`, `scripts/product.js`, `scripts/data.js`, `data/products.json`, `README.md`

- [ ] **Step 1: Start the static server if it is not already running**

Run: `rtk python3 -m http.server 4173`
Expected: terminal shows `Serving HTTP on`

- [ ] **Step 2: Verify both pages return OK**

Run: `rtk curl -I http://127.0.0.1:4173/`
Expected: `HTTP/1.0 200 OK`

Run: `rtk curl -I "http://127.0.0.1:4173/product.html?id=pixel-pop-pad"`
Expected: `HTTP/1.0 200 OK`

- [ ] **Step 3: Perform final manual QA**

Manual check:
- landing page loads with hero, benefits, and product cards
- each `View details` link opens the right toy
- invalid `?id=missing` shows a friendly fallback
- layout works at 1366x768 and phone width
- no console errors during normal browsing

- [ ] **Step 4: Review git status**

Run: `rtk git status --short`
Expected: clean working tree

- [ ] **Step 5: Prepare final delivery notes**

Include:
- what files were added
- how to run locally
- how to add a new product
- any known gaps, such as no real checkout flow yet

## Self-Review

- Spec coverage: plan covers a storefront landing page, data-driven product cards, product detail pages, Chromebook-friendly styling, and simple run docs.
- Placeholder scan: no `TBD`, `TODO`, or “implement later” placeholders remain.
- Type consistency: product schema keys stay consistent across JSON, storefront rendering, product detail rendering, and README instructions.

Plan complete and saved to `docs/superpowers/plans/2026-05-25-chromebook-fidget-storefront.md`. Two execution options:

1. Subagent-Driven (recommended) - I dispatch a fresh subagent per task, review between tasks, fast iteration
2. Inline Execution - Execute tasks in this session using executing-plans, batch execution with checkpoints
