#returning a dictionary in a function


def build_person(firstname,lastname):
    '''return a dictionary of information about a person'''
    person={'firstname':firstname,'lastname':lastname}
    return person

teacher=build_person('jonh','maina')
print(teacher)
for key, value in teacher.items():
    print(f"the teacher's name is {key}:{value}")

