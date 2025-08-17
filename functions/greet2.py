#using a function with a while loop

def get_formatted_name(firstname,lastname):
    '''getting a formated name using a function'''
    fullname=f"{firstname} {lastname}"
    return fullname.title()

while True:
    print("\n please tell me your name")
    fname=input("firstname  :  ")
    if fname =='q':
        break
    lname=input("lastname:  ")
    if lname == 'q':
        break
    formatted_name= get_formatted_name(fname,lname)
    print(f"\nHello, {formatted_name}")
