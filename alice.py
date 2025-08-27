#handling the filenotfounderror exception


from pathlib import Path

path=Path("alice.txt")
try:
    contents=path.read_text(encoding='utf=8')
except FileNotFoundError:
    print(f"the file {path} is not found")



