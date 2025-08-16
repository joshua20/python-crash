#creating functions with return values

def get_formatted_name(firstname,lastname):
    '''function returning a formatted name'''
    full_name=f"{firstname}  {lastname}"
    return full_name.title()


president=get_formatted_name('Viliadmin', 'Putin')
print(president)

student=get_formatted_name('branson','nyakundi')

print(f"The student name is {student}")


