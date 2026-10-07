import os
import json
import re

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.liquid'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Find schema blocks
                schemas = re.findall(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
                for schema_str in schemas:
                    try:
                        json.loads(schema_str)
                    except json.JSONDecodeError as e:
                        print(f"Invalid JSON schema in {path}: {e}")
