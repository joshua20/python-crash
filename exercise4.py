#counting to 20
for value in range(1,21):
    print(value)


#one million

million=list(range(1,1000001))
for value in million:
    print(value)

print(f"max: {max(million)}")

print(f"min:{min(million)}")

print(f"sum: {sum(million)}")


#print odd numbers 

odd_number=list(range(1,21,3))

for num in odd_number:
    print(num)

#multi[les of 3
threes=[]#for value**3 in range(3,31)]
for number in range(3,31,3):
    threes.append(number)

print(f"threes:{threes}")




