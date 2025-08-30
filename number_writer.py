#using json.dumbs() and json.loads() to store data

from pathlib import Path
import json

numbers=[2,3,4,5,6,7,8,9]

path=Path('numbers.json')

contents=json.dumps(numbers)
path.write_text(contents)


