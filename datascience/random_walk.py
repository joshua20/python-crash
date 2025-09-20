#creating a class to generate random walks

from random  import choice

class RandomWalk:
    '''A class to generate random walks'''
    def __init__(self, num_points=5000):
        self.num_points=num_points
        
        #all walks start at 0
        self.x_values=0
        self.y_values=0
