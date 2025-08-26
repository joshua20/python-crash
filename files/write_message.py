#writing to a file

from pathlib import Path

path=Path('programming.txt')

path.write_text("I love programming in Python")

#writing multiple lines

contents="i feel python is the future for me\n"
contents+="it really makes programming fun\n"
contents+="you should take keen interest into programming\n"
contents+="i will keep up my pace"
path2=Path('programming.txt')
path.write_text(contents)

