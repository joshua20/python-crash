#using a function to read lists

def greet_users(names):
    '''passing a list to a function'''
    for name in names:
        msg=f"hello, {name.title()}"
        print(msg)

students=['john','Kimberly','jescah','enock']
greet_users(students)
