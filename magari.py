#using the if statement to change case for cars

cars=['bmw','audi','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
