with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'r') as f:
    content = f.read()

old_block = '''      </div>
    </div>

      </div>
      </div>

      <!-- Main Grid -->'''

new_block = '''      </div>
    </div>

      <!-- Main Grid -->'''

content = content.replace(old_block, new_block)

# Let's also wrap the products loop in paginate and check for product.available
old_loop = '''          {%- for product in collection.products -%}
            {% render 'nexa-product-card', card_product: product %}
          {%- else -%}
            <p class="no-products-msg" style="grid-column: 1/-1; padding: 40px; text-align: center;">No products match the selected filters.</p>
          {%- endfor -%}'''

new_loop = '''          {% paginate collection.products by 48 %}
            {% assign in_stock_products = collection.products | where: 'available' %}
            {%- for product in in_stock_products -%}
              {% render 'nexa-product-card', card_product: product %}
            {%- else -%}
              <p class="no-products-msg" style="grid-column: 1/-1; padding: 40px; text-align: center;">No products match the selected filters.</p>
            {%- endfor -%}
          {% endpaginate %}'''

content = content.replace(old_loop, new_loop)

# Also wait, if there are no products in the collection because it's a test environment without products assigned to /collections/all,
# we can gracefully fallback to collections['all'].products
# Actually, `where: 'available'` might be safest.
# Let's replace the whole grid area just in case.

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'w') as f:
    f.write(content)

