#using range() to generate numbers and then use for loop access them

squares=[]

for value in range(1,11):
    square=value **2
    squares.append(square)

print(squares)

