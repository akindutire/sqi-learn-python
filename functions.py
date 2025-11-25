#Parametised function and unParametised function
# fn declaration: give fn a name
# fn invokation: calling the fn to work
def call_my_name():
    print('I am who I am')
    
# Invokation
call_my_name()

#parameritised fn
def call_my_name_with_param(name: str):
    print(f'I am {name}')

call_my_name_with_param('Ayomide')

#Function can also be called with named parameters
call_my_name_with_param(name='John')

# Function with default parameter, default arg always comes last
def call_my_name_with_default_param(name: str, age: int=30):
    print(f'I am {name} and I am {age} years old')


# Use of global variable inside a fn
my_age = 25
def print_my_age():
    print(f'My age is {my_age}')

print_my_age()

# Quick three: Functions are documented using docstrings
def print_the_age_again() -> None | any:
    # Global keyword is used to modify a global variable inside a fn
    '''This fn prints the age again after modifying it using global keyword'''
    global my_age
    my_age += 5
    print(f'my age is still {my_age}')
print_the_age_again()


#Lambda function: anonymous fn, fn without a name
v_lambda_age_fn = lambda name, age: f"I am {name} and I am {age} years old"
print(v_lambda_age_fn('Sholly', 22))


# List comprehension returns a generator
a = ['ac', 'ds', 'sf', 'f']
b = (x for x in a if len(x)>1) #generator
for c in b:
    print(c)