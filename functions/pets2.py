#default values in functions

def describe_pet(pet_name, animal_type='sheep'):
    '''describing sheep pets'''
    print(f"\n i have a {animal_type}")
    print(f"\n my {animal_type}'s name is {pet_name.title()}")

describe_pet("okioma")
