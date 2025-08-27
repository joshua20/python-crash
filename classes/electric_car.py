#class inheritance

class Car:
    '''a simple car class'''
    def __init__(self, make,model,year):
        '''initialize attribute to describe a car'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
        self.fuel=23
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
    def fill_tank(self,fuel):
        '''refill tank if fuel is empty'''
        if self.fuel=="":
            self.fuel += 10
        print(f" your tank has {self.fuel} litres of fuel")
        
my_car=Car('subaru','outback','2024')
print(my_car.descriptive_name())

my_car.update_odometer(20)
my_car.read_odometer()
my_car.fill_tank(30)
class Battery:
    '''a new class to handle electric car battery infor'''
    def __init__(self, battery_size=40):
        '''initialize battery class'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''print a statement describing battery'''
        print(f"this car has a {self.battery_size}-kwh batterry")
    def get_range(self):
        '''print the range this battery provides'''
        if self.battery_size == 40:
            range=150
        elif self.battery_size ==65:
            range=225

        print(f"this battery can take you a range of {range} miles")

class ElectricCar(Car):
    '''represents aspects of a car, specific to electric vehicles'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
        self.charge=0
  
    def fill_tank(self, charge):
        '''recharge battery if charge is 0'''
        if self.charge == 0:
            self.charge += 100
        print(f"you now have {self.charge} of charge")

#example of an electric car

my_leaf=ElectricCar('nissan','leaf','2020')

print(my_leaf.descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.fill_tank(0)
my_leaf.battery.get_range()
