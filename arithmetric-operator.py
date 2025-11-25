# Numbers and operators
additionVar = 5 + 5
print("Addition", additionVar)

subtractionVar = 5 - 5
print("Sub", subtractionVar)

divisionVar = 5.2 / 5
print("Division", divisionVar)

# integer division
intDivisionVar = 6 // 5
print("Integer division", intDivisionVar)

print("floor division", 20.7//10.2)

multiplicationVar = 5 * 5
print("Multiplication", multiplicationVar)

modulusVar = 6 % 5
print("Modulus",modulusVar)

exponent = 5 ** 2
print("Exponent", exponent)

# assignment operators
x = 5
x += 3 # x = x + 3
print("Addition assignment", x)
x -= 3 # x = x - 3  
print("Subtraction assignment", x)

y = 6
y //= 3 # y = y // 3 
print("Integer or floor division assignment - it rounds down", y)


# Comparison ==, >= <=, >, <, !=
# Logical op, and, or, not, xor
# Membership op: in, not in
print('Checking if tunde exist in a list using membership op', 'Tunde' in set(['Tunde', 'Ayo']))
# Identity operator: is, is not, it compares memory locations and not just value
print('Checking using identity op \'is\'', 5 is 5)