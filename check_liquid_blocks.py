import os
import re

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.liquid'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # capture {% liquid ... %} and {%- liquid ... -%}
                liquid_blocks = re.findall(r'{%-?\s*liquid\s+(.*?)\s*-?%}', content, re.DOTALL)
                for i, block in enumerate(liquid_blocks):
                    print(f"--- {path} block {i} ---")
                    print(block)
