#ploting a simple line graph)

import matplotlib.pyplot as plt

squares=[1,4,9,16,25,36]

fig,ax=plt.subplots()
ax.plot(squares, linewidth=3)

#set chart title and label the axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("value", fontsize=16)
ax.set_ylabel("square of value", fontsize=16)

#set size of tick labels.
ax.tick_params(labelsize=14)

plt.savefig("my_squares.png")
#plt.show()

