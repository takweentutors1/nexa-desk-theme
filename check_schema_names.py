import os
import json
import re

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.liquid'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                schemas = re.findall(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
                for schema_str in schemas:
                    try:
                        s = json.loads(schema_str)
                        name = s.get('name', '')
                        if len(name) > 25:
                            print(f"Schema name > 25 chars in {path}: {name}")
                    except Exception:
                        pass
