#reading exercise files

from pathlib import Path

texts=Path('learning_python.txt')
contents=texts.read_text()

lines=contents.splitlines()
print("printing the lines form the doc")
for line in lines:
    print(line)


texts_file=''

for line in lines:
    texts_file+=line

print(" the data stored in the file")
print(texts_file.strip())

