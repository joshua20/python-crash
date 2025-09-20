#plotting the fig using scatter()
import matplotlib.pyplot as plt

values=[1,2,3,4,5,6]
squares=[1,4,9,16,25,36]

plt.style.use('bmh')
fig,ax=plt.subplots()

ax.scatter(values,squares, s=100)

#set title 
ax.set_title("scatter() point", fontsize=18)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("square of values", fontsize=14)

#set tick params
ax.tick_params(labelsize=16)

plt.savefig("scatter.png")
