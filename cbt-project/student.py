#assignment
#register student
#take test
#display result
import random
from config import Config

class Student:
    def __init__(self):
        config = Config()
        self.__db_cursor = config.get_db_cursor()
 
        self.__students = []
        self.__questions = []
        self.__answers = []

    # "What is the capital of Canada? \n A: Ottawa \n B: Alberta \n C: Vancouver",
    #         "Who painted the Mona Lisa? \n A: Leonardo da Vinci \n B: Poseidon Reily \n C: Fred Coleman",
    #         "What is the chemical symbol for gold? \n A: Ag \n B: Ar \n C: Au"
    
    def orchestrate(self):
        #Are there students? register
        no_of_students_exist = self.__no_of_student_exist()
        print(f"Welcome to the Student Module..., there are {no_of_students_exist} students available to take test\n You can skip registration if need be")
        
        while True:
            print("""
                1. Register student
                2. Exit student registration
                """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                num_of_student_to_register = int(input("Enter number of student to register: "))
                self.__register(num_of_student_to_register)
            else:
                print("Exiting student registration...\n")
                break
            
        no_of_students_exist = self.__no_of_student_exist()
        if no_of_students_exist == 0:
            print("No students registered. Exiting application...\n")
            self.__db_cursor.close()
            exit()
        else:
            #populate students into class variable
            self.__db_cursor.execute("SELECT id,name FROM students")
            student_data_frm_db = self.__db_cursor.fetchall()
            self.__students = [{'id':student[0], 'name':student[1], 'question_and_answer': []} for student in student_data_frm_db]

            #populate tests into questions class variable
            self.__db_cursor.execute("SELECT * FROM tests")
            tests = self.__db_cursor.fetchall()
            for test in tests:
                t = f"{test[0]}. {test[1]} \n"
                test_options = [(i,op) for i,op in enumerate(test[2].split(','), 1)]
                for option in test_options:
                    t += f" {chr(64+option[0])}: {option[1]} \n"
                self.__questions.append({'id': test[0], 'qs': t, 'answer': test[3]})
            

        
        # Take test or skip test
        choice = int(input("Do you want to take the test now? (1 for Yes, 0 for No): "))
        if choice == 1:
            self.__take_test()
            #commit test to db
            self.__commit_test_results()
        
        #Calculate score for each student
        
        
        
    def __no_of_student_exist(self):
        """Function to return number of students already registered"""
        self.__db_cursor.execute("SELECT COUNT(*) FROM students")
        return self.__db_cursor.fetchone()[0]

    def __register(self, num_of_student_to_register):
        """Function to register students for the test"""
        
        students = []
        for i in range(1, num_of_student_to_register + 1):
            name = str(input(f"Enter name of student {i}: "))
            if name in [student[0] for student in students]:
                print(f"Student {name} has been registered, Skipping...\n")
                continue
            data = [
                name,
                name+'@'+"sqi-pyhton.com",
                '080'+str(random.randint(10000000,99999999)),
                'RAND',
                'SQI-PY-'+str(random.randint(1000,9999)),
            ]
            students.append(data)
            
        self.__db_cursor.executemany("INSERT INTO students (name, email, phone, password, reg_number) VALUES (%s, %s, %s, %s, %s)", students)
    
    def __take_test(self):
        """Function to take test for all registered students"""
        
        for i, student in enumerate(self.__students):
            print(f"\nStarting test for {student['name']}\n")
            questionCounter = 1
            for question in self.__questions:
                if questionCounter > 1:
                    print("-------------------------\n")
                    
                print(f"Q: {question.qs}")
                studentAnswer = str(input("Enter your answer (A, B, C): ")).strip()
                
                continuationStatement = 'Moving on...'
                if questionCounter == len(self.__questions):
                    continuationStatement = '...Cinema has ended!'
                      
                correctAnswer = chr(64 + question['answer'])  # Convert numeric answer to letter (1 -> A (65 in ASCII), 2 -> B, etc)
                if studentAnswer.upper() == correctAnswer:    
                    # Each correct answer awards 33 point
                    print(f"Correct, {continuationStatement}")
                    self.__students[i]['question_and_answer'].append((question['id'], studentAnswer.upper(), 1))
                else:
                    self.__students[i]['question_and_answer'].append((question['id'], studentAnswer.upper(), 0))
                    print(f"Wrong, {continuationStatement}")
                    
                # Increase counter    
                questionCounter += 1 
     
    def __commit_test_results(self):
        """Function to commit test results to the database"""
        
        for student in self.__students:
            student_id = student['id']
            for qa in student['question_and_answer']:
                question_id = qa[0]
                student_answer = qa[1] #A is 65 in ASCII
                is_correct = qa[2]
                self\
                    .__db_cursor\
                    .execute("INSERT INTO test_responses (answer_picked, is_correct, test_id, student_id) VALUES (%s, %s, %s, %s)", ( 66-ord(student_answer), is_correct, question_id, student_id))

    def __show_results(self):
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
            student_question_and_answer = student['question_and_answer']
            score = 0
            for qa in student_question_and_answer:
                if qa[2] == 1:
                    score += 33
 
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

    
    