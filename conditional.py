val1 = 67

if val1 == 50:
    val1 -= 10
    print(True)
else:
    val1 += 10
    print(False)

if val1 >= 50:
    val1 += 10
    print("Greater than or equal to 50")


if val1 == 40:
    print("Equal to 40")
elif val1 == 60:
    print("Equal to 60")
else:
    print("Not equal to 40 nor 60")

# != not equal to
# <= less than or equal to
# < less than
# > greater than

# Nested if
if val1 == 40:
    if True:
        print("I got 40")
    else:
        print("Na camouflage o, i no get 40 o")
        
# Grammer action IF condition ELSE another_action
# print("End of conditional statements") if True else print("This will never be printed")

#In f string
print(f"The value of va1 is { 'I am '+val1+' yrs old' if val1 == 40 else 'Na camouflage o, i no get 40 o' }")