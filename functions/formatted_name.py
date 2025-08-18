#creating functions with return values

def get_formatted_name(firstname,lastname):
    '''function returning a formatted name'''
    full_name=f"{firstname}  {lastname}"
    return full_name.title()


president=get_formatted_name('Viliadmin', 'Putin')
print(president)

student=get_formatted_name('branson','nyakundi')

print(f"The student name is {student}")

#making arguments optional


def formatted_name(firstname,lastname,middlename=''):
    '''you can make arguments optional in functions'''

    fullname=f"{firstname}  {middlename} {lastname}"

    return fullname.title()

writter=formatted_name('joshua','ariemba','nyakundi')
print(f"the writer is {writter}")

joker=formatted_name("erick","okiamba")
print(f"our famous joker is {joker}")

