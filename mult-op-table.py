opWhitelist = ["add", "multiply", "subtract", "divide"]
print("Operation whitelist")
index = 0
for op in opWhitelist:
    print(f'{index+1} - {op}')
    index += 1
    #Add a break since count recongises the last on the list
    if index == len(opWhitelist):
        print('---------\n')
    
choice = str(input("Enter operation: "))

# using early returns
if choice not in opWhitelist:
    print("Error: Operator not in available, Exiting...")
    exit()
    
limit = 12
print(f'{choice.capitalize()} Table for 1 to {limit}')
for i in range(1,limit+1):
    print(f'\nTable {i}\n----------')
    for j in range(1, limit+1):
        if choice == 'add':
            print(f'{i} + {j} = {i+j}')
        elif choice == 'multiply':
            print(f'{i} x {j} = {i*j}')
        elif choice == 'subtract':
            print(f'{i} - {j} = {i-j}')
        elif choice == 'divide':
            print(f'{i} / {j} = {i/j}')