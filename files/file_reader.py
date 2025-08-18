from pathlib import Path

path=Path('pi_digits.txt')
contents=path.read_text()
print(contents)


#reading lines

lines=contents.splitlines()

for line in lines:
    print(line)
