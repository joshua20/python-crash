#creating a restaurant class

class Restaurant:
    '''restaurant class'''
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describe_rest(self):
        '''method describing the restaurant'''
        print(f"the restaurants' name is {self.name.title()}")
        print(f"The restaurant's cusine is {self.cuisine_type}")

    def open_rest(self):
        '''method openning the restaurant'''
        print(f"{self.name.title()} is now open!!")


my_restaurant=Restaurant('mochama','kienyeji')
print(my_restaurant.name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_rest()
my_restaurant.open_rest()

class User:
    ''' class describing a user'''
    def __init__(self, firstname, lastname, age , nationality):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.nationality=nationality

    def describe_user(self):
        '''a method that describies a user'''
        print(f"We have {self.firstname.title()} {self.lastname.title()}")
        print(f"{self.firstname} if aged {self.age} years old")
        print(f"{self.firstname} is a {self.nationality.title()}n")

    def greet_user(self):
        '''method to greet a user'''
        print(f" Hello, {self.firstname.title()} {self.lastname.title()}")


my_student=User('nehemiah','kerandi',28,'kenya')
my_student.describe_user()
my_student.greet_user()
