#try it youself exercise

def make_shirt(size,message):
    '''function to make a shirt'''
    print(f"\n i need {size} sized shirt labeled '{message}'")

make_shirt('medium','i shall make it happen')



def large_shirt(message, size='large'):
    '''making a large sized shirt'''
    print(f"\n i need a {size} shirt reading '{message}'")

large_shirt('I love Python')


def describe_city(city, country):
    '''describing cities'''
    print(f"\n{city.title()} is in {country.title()}")

describe_city('nairobi','kenya')
