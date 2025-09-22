
from pathlib import Path
import csv

path=Path("USW00094728.csv")
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)

print(header_row)

#printing the headers and their positions 

for index, column_header in enumerate(header_row):
    print(index, column_header)

#extracting the elevation

highs=[]

for row in reader:
    high=row[3]
    highs.append(high)
print(highs)
