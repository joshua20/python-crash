#using arbitray arguments in functions

def make_pizza(*toppings):
    '''print a list of arbitrary toppings that have been requested'''
    print(toppings)

make_pizza('peperoni')
make_pizza('mushrooms','green peppers','extra cheese')

