import sys
import os

file_path = 'requirements.txt'

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    sys.exit(1)

try:
    # Try utf-16 first as powershell > creates utf-16
    with open(file_path, 'r', encoding='utf-16') as f:
        content = f.read()
except UnicodeError:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeError:
        with open(file_path, 'r', errors='replace') as f:
            content = f.read()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Print content to stdout (ensure utf-8)
sys.stdout.reconfigure(encoding='utf-8')
print(content)
