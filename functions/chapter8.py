#creating functions

def display_message():
    '''a function that informs a friend'''
    friend=input("enter the friend's name")
    print(f"Hello, {friend.title()}. I am learning python functions")

display_message()



#creating a book function

def favorite_book():
    '''a function that prints a book title'''
    title=input("Enter the title of the book you are reading  ")
    print(f"i am reading {title.upper()}")

favorite_book()
