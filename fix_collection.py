import re

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'r') as f:
    content = f.read()

# 1. Replace the top container
old_top = '''<div class="collection-filters-section page-width" data-section-id="{{ section.id }}">
  <div class="collection-layout-grid">
    <!-- Desktop Sticky Sidebar -->
    <div class="sticky-filter-wrapper" id="nexa-desktop-sidebar">'''

new_top = '''<div class="collection-page-layout" data-section-id="{{ section.id }}">
  <!-- Collection Hero Banner -->
  <div class="collection-hero-banner">
    <div class="collection-hero-inner">
      <div class="collection-breadcrumbs">
        <a href="/">Home</a> / <a href="/collections">Collections</a> / <span class="current">{{ collection.title | default: 'All Products' }}</span>
      </div>
      <h1 class="collection-hero-title">{{ collection.title | default: 'All Products & Workstations' }}</h1>
      <p class="collection-hero-desc">
        {{ collection.description | default: 'Explore premium single-cable docks, crystal-clear 4K displays, and ergonomic risers engineered for productive remote work.' }}
      </p>
      <div class="collection-meta-bar">
        <span class="meta-pill">UK Warehouse • Next-Day Dispatch Available</span>
        <span class="meta-pill-outline">30-Day Hassle-Free UK Returns</span>
      </div>
    </div>
  </div>

  <div class="collection-discovery-container">
    <div class="collection-toolbar-row">
      <div class="toolbar-left-group">
        <button type="button" class="desktop-filter-toggle-btn" onclick="document.querySelector('.collection-main-layout').classList.toggle('sidebar-hidden')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="4" y1="21" x2="4" y2="14"></line>
            <line x1="4" y1="10" x2="4" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12" y2="3"></line>
            <line x1="20" y1="21" x2="20" y2="16"></line>
            <line x1="20" y1="12" x2="20" y2="3"></line>
            <line x1="1" y1="14" x2="7" y2="14"></line>
            <line x1="9" y1="8" x2="15" y2="8"></line>
            <line x1="17" y1="16" x2="23" y2="16"></line>
          </svg>
          Hide Filters
        </button>
        <span class="toolbar-stats-text">Showing <strong>{{ collection.products_count | default: '18' }}</strong> items</span>
      </div>
      <div class="toolbar-sort-wrap">
        <span class="sort-label">Sort by:</span>
        <select class="collection-sort-select">
          <option>Featured Workstations</option>
          <option>Price: Low to High</option>
          <option>Price: High to Low</option>
        </select>
      </div>
    </div>

    <div class="collection-main-layout">
      <!-- Desktop Sticky Sidebar -->
      <div class="faceted-filter-sidebar" id="nexa-desktop-sidebar">
        <div class="sticky-filter-wrapper">'''

content = content.replace(old_top, new_top)

# 2. Replace the bottom
old_bottom = '''    <!-- Main Grid -->
    <div class="collection-products-area">
      <!-- We can put products grid here if we want to bundle it, but if it's just the filter section, we can end it here -->
      <div class="products-grid-four-col">
        {%- for product in collection.products -%}
          {% render 'nexa-product-card', card_product: product %}
        {%- else -%}
          <p class="no-products-msg" style="grid-column: 1/-1; padding: 40px; text-align: center;">No products match the selected filters.</p>
        {%- endfor -%}
      </div>
    </div>
  </div>
</div>'''

new_bottom = '''      </div>
      </div>

      <!-- Main Grid -->
      <div class="collection-products-area">
        <div class="products-grid">
          {%- for product in collection.products -%}
            {% render 'nexa-product-card', card_product: product %}
          {%- else -%}
            <p class="no-products-msg" style="grid-column: 1/-1; padding: 40px; text-align: center;">No products match the selected filters.</p>
          {%- endfor -%}
        </div>
      </div>
    </div>
  </div>
</div>'''

content = content.replace(old_bottom, new_bottom)

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'w') as f:
    f.write(content)

