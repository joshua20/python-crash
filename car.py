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
    
    def update_odometer(self, miles):
        '''method to update odometer'''
        if miles>= self.odometer_reading:
            self.odometer_reading=miles
            print(f"updated odometer reading is now at {self.odometer_reading}")
        else:
            print("you cannot rollback the odometer")

my_new_car=Car('audi','a4',2012)
print(my_new_car.get_descriptive_name())

#modifying an attribute directly
print("cars milage before start of journey")
my_new_car.read_odometer()

print("new odometer reading")

my_new_car.odometer_reading=40

my_new_car.read_odometer()

#my_new_car.update_odometer(30)
print("updated odometer reading")
my_new_car.update_odometer(45)
