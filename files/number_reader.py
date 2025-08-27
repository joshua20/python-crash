#using json loads() to read stored json data
from pathlib import Path
import json

path=Path("numbers.json")

contents=path.read_text()
numbers=json.loads(contents)

print(numbers)
