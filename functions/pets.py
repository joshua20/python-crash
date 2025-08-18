#positional arguments in functions

def describe_pet(animal_type, pet_name):
    '''function to describe a pet'''
    print(f"\n i have a {animal_type}.")
    print(f"\n My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog','box')

describe_pet('cat', 'kangina')
