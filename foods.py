#copying a list

my_foods=['pizza','sukuma wiki','ugali','smokie']

print("my favorite foods are :")

print(my_foods)

#copy list
friend_foods=my_foods[:]

print("my friend's foods are:")
print(friend_foods)

my_foods.append("chapati")
friend_foods.append("wali")

print(my_foods)
print(friend_foods)
