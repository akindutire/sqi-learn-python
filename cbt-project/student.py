#assignment
#register student
#take test
#display result
import json
import random
from config import Config

class Student:
    def __init__(self):
        self.__config = Config()
        self.__students = []
        self.__questions = []

        # "What is the capital of Canada? \n A: Ottawa \n B: Alberta \n C: Vancouver",
        #         "Who painted the Mona Lisa? \n A: Leonardo Da Vinci \n B: Poseidon Reily \n C: Fred Coleman",
        #         "What is the chemical symbol for gold? \n A: Ag \n B: Ar \n C: Au"
    
    def orchestrate(self):
        
        # Only connect to db when needed
        self.__db, self.__db_cursor = self.__config.get_db_cursor()
        
        #Are there students? register
        no_of_students_exist = self.__no_of_student_exist()
        print(f"\nWelcome to the Student Module..., there are {no_of_students_exist} students available to take test\n You can skip registration if need be")
        try:
            while True:
                print("""
                    1. Register student
                    0. Exit student registration
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
                self.__close_connection()
                exit()
            
            #populate students into class variable
            self.__db_cursor.execute("SELECT id,name,matric_no FROM students")
            student_data_frm_db = self.__db_cursor.fetchall()
            self.__students = [{'id':student[0], 'name':student[1], 'matric_no': student[2], 'question_and_answer': []} for student in student_data_frm_db]
            
            #Further populate student question and answer if they have taken test before
            for i, student in enumerate(self.__students):
                self.__db_cursor.execute("SELECT test_id, answer_picked, is_correct FROM test_responses WHERE student_id = %s", (student['id'],))
                student_qa_data_frm_db = self.__db_cursor.fetchall()
                self.__students[i]['question_and_answer'] = [(qa[0], chr(64 + qa[1]), qa[2]) for qa in student_qa_data_frm_db]  
                
            #populate tests into questions class variable
            self.__db_cursor.execute("SELECT * FROM tests")
            tests = self.__db_cursor.fetchall()
            for test in tests:
                t = f"{test[1]} \n"
                test_options = [(i,op) for i,op in enumerate(json.loads(test[2]), 1)]
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
            self.__show_results()
            
            print("Student module operations completed...\n")
            self.__close_connection()
            
        except ValueError as e:
            print(f"Invalid input: {e}. Aborting student module.")
            self.__close_connection()
            return
        
        
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
                None,
                name,
                name+'@'+"sqi-pyhton.com",
                '080'+str(random.randint(10000000,99999999)),
                'RAND',
                'SQI-PY-'+str(random.randint(1000,9999)),
                None,
            ]
            students.append(data)

        self.__db_cursor.executemany("INSERT INTO students (id, name, email, phone, password, matric_no, date_created) VALUES (%s, %s, %s, %s, %s, %s, %s)", students)
        self.__db.commit()
    
    def __take_test(self):
        """Function to take test for all registered students"""
        
        for i, student in enumerate(self.__students):

            print(f"\nStarting test for {student['name'].title()}/{student['matric_no']}\n")
            questionCounter = 1
            
            all_question_id_answered_in_previous_attempt = [qa[0] for qa in student['question_and_answer']]
            for question in self.__questions:

                if question['id'] in all_question_id_answered_in_previous_attempt:
                    print(f"{student['name'].title()} has answered this question (Q{question['id']}) before, Skipping...\n")
                    continue
                
                if questionCounter > 1:
                    print("-------------------------\n")
                    
                print(f"Q{questionCounter}: {question['qs']}")
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
                    .execute("INSERT INTO test_responses (id, answer_picked, is_correct, test_id, student_id) VALUES (%s, %s, %s, %s, %s)", (None, 66-ord(student_answer), is_correct, question_id, student_id))
        self.__db.commit()

    def __show_results(self):
        """Result and granding display"""
        
        print("\n\n------RESULT--------")
        _max = 0
        _max_stude = ''
        _total = 0
        _min = 0
        _min_stud = ''
        
        _highest_possible_score = len(self.__questions) * 33
        
        isFirstStudentIteration = True
        for student in self.__students:
            name = student['name'].title()
            matric_no = student['matric_no'].upper()
            student_question_and_answer = student['question_and_answer']
            score = 0
            for qa in student_question_and_answer:
                if qa[2] == 1:
                    score += 33
 
            #Trying to get the first student score as min
            if isFirstStudentIteration == True:
                _min = score
                _min_stud = matric_no
                isFirstStudentIteration = False
                
            grade = "Fail"
            if score >= _highest_possible_score/2:
                grade = "Pass"
            print(f"{name} / {matric_no} = {score}, Grade: {grade}")
            
            if score > _max:
                _max = score
                _max_stude = matric_no
            
            if score < _min:
                _min = score
                _min_stud = matric_no

            _total += score
            
        iavg = _total/len(self.__students)

        print(f"\nMax Student= {_max_stude} has {_max}\nMin Student = {_min_stud} has {_min}\nAverage = {iavg}\nNumber of students registered = {len(self.__students)}")

    def __close_connection(self):
        """Function to close database connection"""
        if self.__db:
            self.__db.close()
        if self.__db_cursor:
            self.__db_cursor.close()
    