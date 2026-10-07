with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'r') as f:
    content = f.read()

import re
pattern = r'\{%\s*paginate collection\.products by 48\s*%\}.*?\{%\s*endpaginate\s*%\}'

new_loop = '''          {% assign display_products = collection.products | where: 'available' %}
          {% if display_products.size == 0 %}
            {% assign display_products = collections['all'].products | where: 'available' %}
          {% endif %}
          
          {% paginate collections['all'].products by 48 %}
            {%- for product in display_products -%}
              {% render 'nexa-product-card', card_product: product %}
            {%- else -%}
              <p class="no-products-msg" style="grid-column: 1/-1; padding: 40px; text-align: center;">No products match the selected filters.</p>
            {%- endfor -%}
          {% endpaginate %}'''

content = re.sub(pattern, new_loop, content, flags=re.DOTALL)

with open('/Users/pc/nexa-desk/nexa-deskcnew/sections/nexa-collection-filters.liquid', 'w') as f:
    f.write(content)
