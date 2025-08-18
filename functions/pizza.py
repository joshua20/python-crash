#using arbitray arguments in functions

def make_pizza(*toppings):
    '''print a list of arbitrary toppings that have been requested'''
    print("\n making pizza wit the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('peperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#mixing positional and arbitrary arguments

def mak_pizza(size, *toppings):
    '''mixing positional and arbitrary arguments'''
    print(f"\n making a {size}-inch pizza with the following toppings")

    for topping in toppings:
        print(topping)

mak_pizza(4, 'mushroom','peperoni')
