#creating the die class

from random import randint

class Die:
    ''' a class representing a single die'''

    def __init__(self, num_sides=6):
        '''assume a six sided die'''
        self.num_sides=num_sides

    def roll(self):
        '''return any random number from any of the sides'''
        return randint(1, self.num_sides)

