#looping  through a dictionary

user_0={
        'username':'josh20',
        'firstname':'Joshua',
        'Lastname':'Ariemba',
        }

for key, value in user_0.items():
    print(f"{key}:{value}")


#looping for keys in a dictionary
print("looping through a dictionary for keys only")
for key in user_0.keys():
    print(key)

#looping through a dict 's keys in a particular order

for key in sorted(user_0.keys()):
    print(f"i now know your keys\n\t {key}")

#looping through dict's values 

print("the user has the following detais")

for values in user_0.values():
    print(values)
