#calculating data automatically

import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values]

plt.style.use('bmh')

fig,ax=plt.subplots()
#plot
ax.plot(x_values,y_values,color='red')

ax.set_title("ploting numbers automatically")
ax.set_xlabel("X_labels", fontsize=16)
ax.set_ylabel("y_values", fontsize=16)

#set range for axis
ax.axis([0,1100,0,1_100_000])
#set tick_params

ax.tick_params(labelsize=20)

plt.savefig("auto_squares.png")
