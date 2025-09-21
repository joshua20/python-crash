#rolling the die

from die import Die

#create a die

die=Die()

#make some rolls and store results in a list

results=[]

for roll_num in range(100):
    result=die.roll()
    results.append(result)

print(results)

#analyze the results

frequencies=[]

poss_results=range(1, die.num_sides +1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)

print("frequencies")
print(frequencies)
