# Nexa Precision Workstation - Native Shopify Dawn Integration Guide

Welcome to the **Nexa Desk** Shopify Dawn theme implementation. This directory (`nexa-deskcnew/`) contains all necessary assets, layouts, sections, snippets, and JSON templates to manually migrate the custom Hydrogen/Remix storefront into native Shopify Liquid.

---

## 📁 Directory Structure & File Map

```text
nexa-deskcnew/
├── config/
│   └── settings_data.json                  <-- Presets & 'scheme-nexa-dark' color definition
├── assets/
│   ├── nexa-theme.css                      <-- Master obsidian dark stylesheet & tokens
│   ├── nexa-interactive.js                 <-- Setup wizard, blueprint SVG & port tooltips
│   └── nexa-cart-drawer.js                 <-- £300 free shipping meter & bundle interceptor
├── layout/
│   └── theme.liquid                        <-- Master theme shell & asset loading
├── sections/
│   ├── nexa-header.liquid                  <-- Morphing glass header + device status badge
│   ├── nexa-hero-assembly.liquid           <-- Kinetic hero with exploded workstation visual
│   ├── nexa-device-selector.liquid         <-- Host device picker (P1, P2, P3, P4)
│   ├── nexa-power-visualizer.liquid        <-- 100W GaN power & dual 4K telemetry schematic
│   ├── nexa-bento-grid.liquid              <-- Asymmetrical collection showcase
│   ├── nexa-customer-showcase.liquid       <-- UK customer setups with interactive hotspot pins
│   ├── nexa-setup-wizard.liquid            <-- 4-step workstation configurator
│   ├── nexa-workstation-blueprint.liquid   <-- Interactive SVG architecture blueprint
│   ├── nexa-bundle-drawer.liquid           <-- Single-click bundle checkout slide-over
│   ├── nexa-dock-comparison.liquid         <-- 3-column dock comparison matrix
│   ├── nexa-product-gallery.liquid         <-- Sticky left PDP gallery with thumbnails
│   ├── nexa-port-diagram.liquid            <-- Front & rear port pin explorer
│   ├── nexa-tech-specs.liquid              <-- Collapsible technical specifications accordion
│   ├── nexa-whats-in-box.liquid            <-- Unboxing hardware grid
│   ├── nexa-sticky-bar.liquid              <-- Floating bottom product buy bar
│   └── nexa-footer.liquid                  <-- 4-column footer with UK 24h dispatch pill
├── snippets/
│   ├── nexa-logo.liquid                    <-- Vector gold gradient branding logo
│   ├── nexa-incompatibility-modal.liquid   <-- Hardware wattage mismatch explainer dialog
│   ├── nexa-spec-diff-toggle.liquid        <-- 'Highlight Differences Only' switch
│   ├── nexa-compatibility-widget.liquid    <-- Interactive 'Will It Fit My Device?' widget
│   ├── nexa-product-card.liquid            <-- Dark product card with hover flip & stock alert
│   ├── nexa-free-shipping-bar.liquid       <-- Dynamic £300 Free UK delivery milestone bar
│   └── nexa-cart-item-badge.liquid         <-- _SetupReference and _DeviceProfile badges
└── templates/
    ├── index.json                          <-- Homepage JSON layout
    ├── product.nexa-pdp.json               <-- Modular Product Detail Page template
    ├── page.setup-builder.json             <-- Find My Setup configurator page template
    └── page.compare.json                   <-- Dock Comparison page template
```

---

## 🚀 Step-by-Step Installation Instructions

### Step 1: Upload Theme Assets
1. Open your **Shopify Admin** &rarr; **Online Store** &rarr; **Themes**.
2. Select your Dawn theme &rarr; Click **...** (Actions) &rarr; **Edit code**.
3. Under the **Assets** folder, click **Add a new asset** and upload:
   * `nexa-theme.css`
   * `nexa-interactive.js`
   * `nexa-cart-drawer.js`

### Step 2: Configure Layout
1. In the **Layout** folder, open `theme.liquid`.
2. Ensure `nexa-theme.css`, `nexa-interactive.js`, and `nexa-cart-drawer.js` are loaded in `<head>`, and verify `<body class="gradient nexa-dark-theme color-scheme-nexa-dark">`.

### Step 3: Add Snippets
In the **Snippets** folder, click **Add a new snippet** and copy over each file:
* `nexa-logo.liquid`
* `nexa-incompatibility-modal.liquid`
* `nexa-spec-diff-toggle.liquid`
* `nexa-compatibility-widget.liquid`
* `nexa-product-card.liquid`
* `nexa-free-shipping-bar.liquid`
* `nexa-cart-item-badge.liquid`

### Step 4: Add Sections
In the **Sections** folder, click **Add a new section** and create:
* `nexa-header.liquid`
* `nexa-footer.liquid`
* `nexa-hero-assembly.liquid`
* `nexa-device-selector.liquid`
* `nexa-power-visualizer.liquid`
* `nexa-bento-grid.liquid`
* `nexa-customer-showcase.liquid`
* `nexa-setup-wizard.liquid`
* `nexa-workstation-blueprint.liquid`
* `nexa-bundle-drawer.liquid`
* `nexa-dock-comparison.liquid`
* `nexa-product-gallery.liquid`
* `nexa-port-diagram.liquid`
* `nexa-tech-specs.liquid`
* `nexa-whats-in-box.liquid`
* `nexa-sticky-bar.liquid`

### Step 5: Add JSON Templates
Under the **Templates** folder:
* Replace or add `index.json` to instantly apply the full homepage layout.
* Add `product.nexa-pdp.json` under Templates &rarr; Add a new template &rarr; Product.
* Add `page.setup-builder.json` under Templates &rarr; Add a new template &rarr; Page (name: `setup-builder`).
* Add `page.compare.json` under Templates &rarr; Add a new template &rarr; Page (name: `compare`).

### Step 6: Create Store Pages in Shopify Admin
1. Go to **Online Store** &rarr; **Pages** &rarr; Click **Add page**.
2. Title: **Find My Setup** &rarr; Select Theme Template: `page.setup-builder`.
3. Title: **Compare Docks** &rarr; Select Theme Template: `page.compare`.

---

## 🎨 Color Scheme Tokens Reference
* **Background Primary**: `#030712` (Obsidian)
* **Surface Background**: `#0f172a` (Slate 900)
* **Card Background**: `#1e293b` (Slate 800)
* **Text High-Contrast**: `#f8fafc` (Slate 50)
* **Text Muted**: `#94a3b8` (Slate 400)
* **Accent Neon Blue**: `#3b82f6`
* **Accent Cyan Glow**: `#06b6d4`
* **Compatible Emerald**: `#10b981`
* **Warning Amber**: `#f59e0b`
* **Error Ruby**: `#ef4444`
