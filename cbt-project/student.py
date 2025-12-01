#assignment
#register student
#take test
#display result
import random
import mysql.connector as sql
from config import Config

class Student:
    def __init__(self):
        config = Config()
        self.__db_cursor = config.get_db_cursor()
        
        self.__num_of_students = int(input("Enter number of students: "))
        self.__final_students_registered = 0
        self.__students = []
        self.__questions = [
            "What is the capital of Canada? \n A: Ottawa \n B: Alberta \n C: Vancouver",
            "Who painted the Mona Lisa? \n A: Leonardo da Vinci \n B: Poseidon Reily \n C: Fred Coleman",
            "What is the chemical symbol for gold? \n A: Ag \n B: Ar \n C: Au"
        ]
        self.__answers = [
            "A", "A", "C",
        ]

    def register(self):
        """Function to register students for the test"""
        for i in range(1, self.__num_of_students + 1):
            name = str(input(f"Enter name of student {i}: "))
            if name in [student['name'] for student in self.__students]:
                print(f"Student {name} has been registered, Skipping...\n")
                continue
            age = int(input(f"Enter student {i}: age "))
            data = {
                'name': name,
                'age': age if age > 0 else random.randint(10,30),
                'score': 0
            }
            self.__students.append(data)
            self.__final_students_registered += 1
    
    def take_test(self):
        """Function to take test for all registered students"""
        for i, student in enumerate(self.__students):
            print(f"\nStarting test for {student['name']}\n")
            questionCounter = 1
            for question,correctAnswer in zip(self.__questions, self.__answers):
                if questionCounter > 1:
                    print("-------------------------\n")
                    
                print(f"Q: {question}")
                studentAnswer = str(input("Enter your answer (A, B, C): ")).strip()
                
                continuationStatement = 'Moving on...'
                if questionCounter == len(self.__questions):
                    continuationStatement = '...Cinema has ended!'
                        
                if studentAnswer.upper() == correctAnswer:    
                    # Each correct answer awards 33 point
                    print(f"Correct, {continuationStatement}")
                    self.__students[i]['score'] += 33
                else:
                    print(f"Wrong, {continuationStatement}")
                    
                # Increase counter    
                questionCounter += 1 
            
    
    def show_results(self):
        """Result and granding display"""
        
        print("\n\n------RESULT--------")
        _max = 0
        _max_stude = ''
        _total = 0
        _min = 0
        _min_stud = ''
        isFirstStudentIteration = True
        for student in self.__students:
            name = student['name'].capitalize()
            score = student['score']
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
            
        iavg = _total/len(self.__students)

        print(f"\nMax Student= {_max_stude} has {_max}\nMin Student = {_min_stud} has {_min}\nAverage = {iavg}\nNumber of students registered = {self.__final_students_registered}")

    
    def bootstrap(self):
        self.register()
        self.take_test()
        self.show_results()