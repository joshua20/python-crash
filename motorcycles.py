
#modifying elements in a list

motorcycles=['honda','yamaha','suzuki']

print(motorcycles)

motorcycles[0]="ducati"

print(f"new motorcycles list: \n\t {motorcycles}")

#adding elements to a list


#using the append() method

motorcycles.append("honda")

print(motorcycles)

motorcycles.append("hyundai")


#removing elements from a list

#using the del 

del motorcycles[0]

print(f"motorcyles list after removing element 0\n\t {motorcycles}")


#removing the last item using the pop() method

popped_motorcycle=motorcycles.pop()

print(f"popped element is : {popped_motorcycle}")

#popping items by value
first_owned=motorcycles.pop(0)

print(f"my first-owned motorcycle is: {first_owned}")

#removing an element using the remove()

print(motorcycles)

motorcycles.remove("honda")
print(f"removed cycles {motorcycles}")


