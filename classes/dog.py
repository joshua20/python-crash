#creating a dog class

class Dog:
    '''a simple attempt to model a dog'''
    def __init__(self, name,age):
        '''initialize name and age atributes'''
        self.name=name
        self.age=age

    def sit(self):
        '''simulate a dog sittingin response to a command'''
        print(f"{self.name} is now sitting")

    def roll_over(self):
        '''simuate a dog rolling over after a command'''
        print(f"{self.name} is now rolling over")

