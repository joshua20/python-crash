#using arbitrary keyword arguments

def user_profile(first,last,**userinfo):
    '''using arbitrary key-value arguments in functions'''
    userinfo['firstname']=first
    userinfo['lastname']=last

    return userinfo


user=user_profile('joshua','nyakundi',age=30,langauge='python',location='Nairobi')

print(user)
