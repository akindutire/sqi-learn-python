# For loop
print("For loop from 1 to 12")
mylimit = 5
for i in range(1,mylimit+1):
    print(i)


# The zip function zaps two iterable objects together
print("Zipping two lists together")
listOne = ['a', 'b', 'c']
listTwo = [1, 2, 3]
for letter, number in zip(listOne, listTwo):
    print(f"Letter: {letter}, Number: {number}")
    
    
#Nested for loop
for i in range(1,12):
    print(f"Multiplication table of {i}")
    for j in range(1,13):
        print(f"{i} x {j} = {i*j}")
    
# Extend the above to +,-,/
# Use membership operator to check if operator selected is in the whitelist
# raise error when operator is not in whitelist
#While loop
#pass keyword is used to create an empty block of code
i = 1
while True:
    print(f"I got here @ {i}")
    if i == 20:
        break
    i+=1