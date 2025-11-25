print("Welcome to Calculator")
operators = ['+', '-', '/', '*']
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
choiceOfOperation = str(input("Enter choice of operation: "))

if choiceOfOperation in operators:
    if choiceOfOperation == "+":
        print(f'{number1} + {number2} = {number1 + number2}')
    elif choiceOfOperation == "-":
        print(f'{number1} - {number2} = {number1 - number2}')
    elif choiceOfOperation == "/":
        print(f'{number1} / {number2} = {number1 / number2}')
    elif choiceOfOperation == "*":
        print(f'{number1} * {number2} = {number1 * number2}')
    else:
        print(f"Go back to operation")
else:
    print("Wrong operator")