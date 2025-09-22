
from pathlib import Path
import csv

path=Path("USW00094728.csv")
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)

print(header_row)
