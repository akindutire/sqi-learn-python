import math
print('Welcome to our grading app')

score = float(input("What is your score in the test: "))
score = math.floor(score)
if(score > 100 and score < 0):
    print("We don't havea grade for you, Exiting...")
    exit()

if score in range(0,39+1):
    print(f'You failed, please meet the cordinator for a re-sit: Grade=F')
elif score in range(40,44+1):
    print("Grade = E")
elif score in range(45,49+1):
    print("Grade = D")
elif score in range(50,59+1):
    print("Grade = C")
elif score in range(60,74+1):
    print("Grade = B")
elif score in range(75,100+1):
    print("Grade = A, Excellent pikin")
else:
    print("This is an exception, handle it offline with your advisor")