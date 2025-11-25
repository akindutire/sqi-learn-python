'''
Assignment:
Build a simple USSD menu using conditional statements
1. create a list of different ussd you use max of 3
2. use cond. statements to build a dashboard for ussd menu for each code using membership operator ro confirm the ussd
3. Each ussd code should have atleast 3 options
4. Each option should have least 3 inner navigations from the root and a message when selected
5. user neested conditional statement to achieve this
6. Be mindful of exceptions like when user enters the wronf /ussd code or wrong option and create code to handle this using else
'''

print('Welcome to *312# ussd menu\n')

def captureChoice(whitelist: tuple[int,...]) -> int|None :
    
    if not isinstance(whitelist, tuple):
        raise TypeError("Only tuples are allowed as whitelisted choices")
    
    try:
        choice = int(input("Pick an option: "))
    except:
        choice = -1
        
    if choice not in whitelist:
        print("Operation not allowed Exiting...")
        exit()
    
    if choice == 0:
        print("Exiting...")
        exit()
        
    return choice




print("""
      Enter your choice
      1. Data Plans
      2. Voice offers
      3. Xtra Values
      0. Exit
      """)
choice = captureChoice((1,2,3,0))

if choice == 1:
    print("""
    Enter your choice : Data Plans
    1. Daily
    2. 2-3 days
    3. Weekly
    0. Exit
    """)
    choice = captureChoice((1,2,3,0))
    if choice == 1:
        print("""
        Enter your choice : Daily
        1. 75MB
        2. 100MB
        3. 200MB
        0. Exit
        """)
        choice = captureChoice((1,2,3,0))
        match choice:
            case 1:
                print("Welcome to 75mb package")
            case 2:
                print("100MB package selected")
            case 3:
                print("200MB package selected")
    elif choice == 2:
        print("""
        Enter your choice : 2-3 days Plans
        1. 600 = 1.5G
        2. 750 = 2GB
        3. 900 = 2.5GB
        0. Exit
        """)
        choice = captureChoice((1,2,3,0))
        match choice:
            case 1:
                print("Welcome to 1.5GB package")
            case 2:
                print("2GB package selected")
            case 3:
                print("2.5 package selected")
    elif choice == 3:
        print("""
        Enter your choice : Weekly Plans
        1. 500 = 500MB
        2. 800 = 1GB
        3. 1000 = 1.5GB
        0. Exit
        """)
        choice = captureChoice((1,2,3,0))
        match choice:
            case 1:
                print("Welcome to 500MB package")
            case 2:
                print("1GB package selected")
            case 3:
                print("1.5GB package selected")
                
elif choice == 2:
    print("""
    Enter your choice : Voice offers
    1. 100mins = N400
    2. 150mins = N600
    3. 200mins = N800
    0. Exit
    """)
    choice = captureChoice((1,2,3,0))
    match choice:
        case 1:
            print("Welcome to 100min of local voice call")
        case 2:
            print("Welcome to 150min of local voice call")
        case 3:
            print("Welcome to 200min of local voice call")
                
elif choice == 3:
    print("""
    Enter your choice : Xtra Values
    1. XtraData
    2. XtraTalk
    3. Valuedata
    0. Exit
    """)
    choice = captureChoice((1,2,3,0))
    if choice == 1:
        print("""
        Enter your choice : XtraData
        1. 5MB = 500
        2. 1.5GB = 1500
        3. 3G = 3000
        0. Exit
        """)
        choice = captureChoice((1,2,3,0))
        match choice:
            case 1:
                print("Welcome to 5MB package")
            case 2:
                print("1.5GB selected")
            case 3:
                print("3GB package selected")
    elif choice == 2:
        print("""
        Enter your choice : 2-3 days Plans
        1. 500
        2. 1500
        3. 3000
        0. Exit
        """)
        choice = captureChoice((1,2,3,0))
        match choice:
            case 1:
                print("N500 airtalk has been added")
            case 2:
                print("N1500 airtalk has been added")
            case 3:
                print("N3000 airtalk has been added")
    elif choice == 3:
        print("""
        Enter your choice : Value Data
        1. 6.75GB = 3000
        2. 14.5GB = 5000
        3. 3.34GB = 10000
        0. Exit
        """)
        choice = captureChoice((1,2,3,0))
        match choice:
            case 1:
                print("6.75GB has been allocated")
            case 2:
                print("14.5GB has been allocated")
            case 3:
                print("3.34GB has been allocated")
                

