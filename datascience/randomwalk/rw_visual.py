#plotting the rando walk

import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:

    #make a randomwalk

    rw=RandomWalk()
    rw.fill_walk()

    #plot the walk points

    plt.style.use('classic')

    fig,ax=plt.subplots()
    
    #coloring the points
    point_numbers=range(rw.num_points)
    
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)

    ax.set_aspect('equal')
    #plotting the starting and ending points

    ax.scatter(0,0,c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.savefig("randomwalk.png")


    keep_running=input("make another walk? y/n:")
    if keep_running == 'n':
        break

