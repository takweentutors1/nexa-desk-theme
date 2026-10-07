import os
import re

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.liquid'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                tags_to_check = ['if', 'for', 'capture', 'form', 'paginate', 'unless', 'case', 'raw']
                for tag in tags_to_check:
                    # Match exact tags like {% if ... %} or {%- if ... -%}
                    # Need to distinguish between {% if %} and {% ifchanged %}
                    open_pattern = r'{%-?\s*' + tag + r'\b[^}]*-?%}'
                    # End tags like {% endif %}
                    close_pattern = r'{%-?\s*end' + tag + r'\s*-?%}'
                    
                    opens = len(re.findall(open_pattern, content))
                    closes = len(re.findall(close_pattern, content))
                    
                    if opens != closes:
                        print(f"Mismatch in {path}: {tag} ({opens} open vs {closes} close)")
                        
