#Assignment
# 0. Use loop to re-ask question and name 
# 1. Build a simple quiz application using the zip class approach
#2. Ask the user to input their name and take the text
#3. Display the result of the test for each student
#4. Find the student with the min scores
#5. Find the student with the max scores
#6. Calculate the average score
#7. Add grading system to show student that pass and the one that failed
print("_____Welcome to CBT aApplication______\n")

numberOfStudents = int(input("Enter number of students taking the test: "))
questions = [
    "What is the capital of Canada? \n A: Ottawa \n B: Alberta \n C: Vancouver",
    "Who painted the Mona Lisa? \n A: Leonardo da Vinci \n B: Poseidon Reily \n C: Fred Coleman",
    "What is the chemical symbol for gold? \n A: Ag \n B: Ar \n C: Au"
]
answers = [
    "A", "A", "C",
]

students = {}

for i in range(1, numberOfStudents+1):
    print("\n")
    studentData = {
        'name': str(input(f"Enter name of student {i}: ")),
        'age': int(input(f"Enter student {i}: age ")),
        'score': 0
    }
    if students.get(studentData["name"]) != None:
        print(f"Student {studentData["name"]} has taken this test, Skipping...\n")
        continue
        
    students[studentData["name"]] = studentData   
    questionCounter = 1
    for question,correctAnswer in zip(questions,answers):
        if questionCounter > 1:
            print("-------------------------\n")
            
        print(f"Q: {question}")
        studentAnswer = str(input("Enter your answer (A, B, C): ")).strip()
        
        continuationStatement = 'Moving on...'
        if questionCounter == len(questions):
            continuationStatement = '...Cinema has ended!'
                
        if studentAnswer.upper() == correctAnswer:    
            # Each correct answer awards 33 point
            print(f"Correct, {continuationStatement}")
            students[studentData["name"]]['score'] += 33
        else:
             print(f"Wrong, {continuationStatement}")
             
        # Increase counter    
        questionCounter += 1
        

# Show Max
# Show Min
# Show average

print("\n\n------RESULT--------")
_max = 0
_max_stude = ''
_total = 0
_min = 0
_min_stud = ''

isFirstStudentIteration = True
for name,data in students.items():
    score = data['score']
    #Trying to get the first student score as min
    if isFirstStudentIteration == True:
        _min = score
        _min_stud = name
        isFirstStudentIteration = False
        
    grade = "Fail"
    if score >= 50:
        grade = "Pass"
    print(f"{name} = {score}, Grade: {grade}")
    
    if score > _max:
        _max = score
        _max_stude = name
    
    if score < _min:
        _min = score
        _min_stud = name
    
    _total += score
    
iavg = _total/len(students)

print(f"Max Student= {_max_stude} has {_max}\nMin Student = {_min_stud} has {_min}\nAverage = {iavg}")

# Assignment
#convert lot of code snippets to functions
# fn for stud reg
# fn for that covers for assignment of question, marks and grade
# fn for displaying result