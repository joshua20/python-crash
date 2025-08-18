#Working with classes and instances
class Car:
    '''a class torepresent a simple car model'''
    def __init__(self, make,model,year):
        '''Initialize attributes to describe'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        '''return a neatly formatted name .'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        '''method to read car's odometer'''
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car=Car('audi','a4',2012)
print(my_new_car.get_descriptive_name())

#modifying an attribute directly
print("cars milage before start of journey")
my_new_car.read_odometer()

print("new odometer reading")

my_new_car.odometer_reading=40

my_new_car.read_odometer()


