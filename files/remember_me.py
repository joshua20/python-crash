#using json to store user generated data

from pathlib import Path
import json


path =Path("username.json")
if path.exists():
    contents=path.read_text()
    username=json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username=input("what is your name?")
    contents=json.dumps(username)
    path.write_text(contents)
    print(f"we will remember you when you return, {username}")




