
from pathlib import Path
import csv

import matplotlib.pyplot as plt

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
    high=row[22]
    highs.append(high)
print(highs)

#plot the elevation 

plt.style.use('classic')
fig,ax=plt.subplots()

ax.plot(highs, color='green')

#format the plot
ax.set_title("elevation for newyork city")
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("elevation", fontsize=16)
ax.tick_params(labelsize=16)

plt.savefig("newyork.png")

