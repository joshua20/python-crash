#working with a file' contents

from pathlib import Path

path=Path('pi_digits.txt')
contents= path.read_text()

lines=contents.splitlines()

pi_string=''

for line in lines:
    pi_string +=line
    
print(pi_string)
print(f"the pi_string has {len(pi_string)} characters")

