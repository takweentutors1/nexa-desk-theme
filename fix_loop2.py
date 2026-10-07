with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'r') as f:
    content = f.read()

import re
pattern = r'\{%\s*assign display_products.*?\{%\s*endpaginate\s*%\}'

new_loop = '''          {%- assign target_collection = collection -%}
          {%- if target_collection.products.size == 0 -%}
            {%- assign target_collection = collections['all'] -%}
          {%- endif -%}

          {% paginate target_collection.products by 48 %}
            {%- for product in target_collection.products -%}
              {%- if product.available -%}
                {% render 'nexa-product-card', card_product: product %}
              {%- endif -%}
            {%- else -%}
              <p class="no-products-msg" style="grid-column: 1/-1; padding: 40px; text-align: center;">No products match the selected filters.</p>
            {%- endfor -%}
          {% endpaginate %}'''

content = re.sub(pattern, new_loop, content, flags=re.DOTALL)

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'w') as f:
    f.write(content)
