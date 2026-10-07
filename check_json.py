import os
import json

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.json'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Invalid JSON in {path}: {e}")
