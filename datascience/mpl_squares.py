#ploting a simple line graph)

import matplotlib.pyplot as plt

squares=[1,4,9,16,25,36]

fig,ax=plt.subplots()
ax.plot(squares)
plt.savefig("my_squares.png")
#plt.show()

