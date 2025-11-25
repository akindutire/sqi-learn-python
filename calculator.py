firstVar = input("Enter first number: ")
secondVar = input("Enter second number: ")

print('''
    Choice
    1. Addition
    2. Subtraction
    3. Division
    4. Integer Division
    5. Multiplication
    6. Modulus
    7. Exponent
    8. Exit
    ''')
choiceVar = int(input("Enter your choice (1-8): "))

if (choiceVar not in [1,2,3,4,5,6,7,8]):
    print("Invalid choice, Exiting...")
    exit()
    
# switch case in python
match choiceVar:
    case 1:
        print(f"The addition of {firstVar} and {secondVar} is: {float(firstVar) + float(secondVar)}")
    case 2:
        print(f"The subtraction of {firstVar} and {secondVar} is: {float(firstVar) - float(secondVar)}")
    case 3:
        print(f"The division of {firstVar} and {secondVar} is: {float(firstVar) / float(secondVar)}")
    case 4:
        print(f"The integer division of {firstVar} and {secondVar} is: {int(firstVar) // int(secondVar)}")
    case 5:
        print(f"The multiplication of {firstVar} and {secondVar} is: {float(firstVar) * float(secondVar)}")
    case 6:
        print(f"The modulus of {firstVar} and {secondVar} is: {int(firstVar) % int(secondVar)}")
    case 7:
        print(f"The exponent of {firstVar} and {secondVar} is: {float(firstVar) ** float(secondVar)}")
    case 8:
        print("Exiting...")
        exit()