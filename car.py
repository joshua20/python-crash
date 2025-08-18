#Working with classes and instances
class Car:
    '''a class torepresent a simple car model'''
    def __init__(self, make,model,year):
        '''Initialize attributes to describe'''
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        '''return a neatly formatted name .'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car=Car('audi','a4',2012)
print(my_new_car.get_descriptive_name())
