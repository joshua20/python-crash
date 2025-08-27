#using json.loads() to read stored data

from pathlib import Path
import json


path=Path("username.json")
contents=path.read_text()

username=json.loads(contents)

print(f"welcome back, {username}")

