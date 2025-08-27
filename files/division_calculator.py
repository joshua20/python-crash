#division by zero error handling

try:
    print(5/0)

except ZeroDivisionError:
    print("you cannot divide any number by zero")

#get two numbers to divide

print("give me two numbers and i will divide them")

print("enter 'q' to quit")

while True:
    firstnumber=input("\n firstnumber:  ")
    if firstnumber == 'q':
        break

    second_number=input("\n second number:  ")
    if second_number == 'q':
        break
    answer=int(firstnumber) / int (second_number)
    print(answer)
