from name_function import get_formatted_name

print("enter 'q' at any time to cancel")
while True:
    first=input("\n please enter your first name  ")
    if first == 'q':
        break
    last=input("\n enter your last  name  ")
    if last =='q':
        break
    

    formatted_name=get_formatted_name(first,last)
    print(f"formatted name: {formatted_name}.")

