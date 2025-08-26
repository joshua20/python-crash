#replacing the word python with java

from pathlib import Path

texts_file=Path('learning_python.txt')

contents=texts_file.read_text()
java_contents=contents.replace('python','java')

lines=java_contents.splitlines()

for line in lines:
    print(line)

