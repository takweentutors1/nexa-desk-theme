import os
import re

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.liquid'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                open_perc = content.count('{%')
                close_perc = content.count('%}')
                
                if open_perc != close_perc:
                    print(f"Mismatch % in {path}: {open_perc} vs {close_perc}")
                    
                open_brace = content.count('{{')
                close_brace = content.count('}}')
                
                if open_brace != close_brace:
                    print(f"Mismatch braces in {path}: {open_brace} vs {close_brace}")
                    
