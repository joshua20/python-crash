#class inheritance

class Car:
    '''a simple car class'''
    def __init__(self, make,model,year):
        '''initialize attribute to describe a car'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def descriptive_name(self):
        '''return a neatly formatted name'''
        longname=f"{self.year} {self.make} {self.model}"
        return longname.title()

    def read_odometer(self):
        '''print a statement showing the odometer reading'''
        print(f"This car has a {self.odometer_reading} reading on it")

    def update_odometer(self, mileage):
        '''set the odometer reading to a given value'''
        if mileage>= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print(f"you cannot rollback dometer")

    def increment_odometer(self, miles):
        '''add a given amount to the odometer reading'''
        self.odometer_reading += miles

my_car=Car('subaru','outback','2024')
print(my_car.descriptive_name())

my_car.update_odometer(20)
my_car.read_odometer()

class ElectricCar(Car):
    '''represents aspects of a car, specific to electric vehicles'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

#example of an electric car

my_leaf=ElectricCar('nissan','leaf','2020')

print(my_leaf.descriptive_name())

