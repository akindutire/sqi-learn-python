from config import Config
import json
class Admin:
    def __init__(self):
        self.__config = Config()
       
    def orchestrate(self):
        
        # Only connect to db when needed
        self.__db, self.__db_cursor = self.__config.get_db_cursor()
        
        print("\nAdmin Module Started...\n")
        
        while True:
            print("""
              1. Create test
              0. Exit/Skip test creation
              """)
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Exiting test creation...\n")
                break
            elif choice == 1:
                self.__create_test()
            else:
                print("Invalid choice. Please try again.\n")
        
        # Check if questions exist
        question_count = self.__no_of_question_exist()
        if question_count > 0:
            print(f"{question_count} test(s) are available for students. You can proceed.\n")
        else:
            print("No tests available. Exiting application.\n")
            self.__close_connection()
            exit()
         
        
        # Commit changes to db
        self.__db.commit()
        
        # close db cursor
        self.__close_connection()


    def __create_test(self):
        question = str(input("Enter question: ")).strip()
        
        option_range = int(input("Enter number of options for the question: "))
        options = []
        
        for i in range(option_range):
            option = str(input(f"Enter option {i+1}: ")).strip()
            options.append(option)
        
        correct_option = int(input("Enter correct option (1, 2, 3, etc): "))
        
        if correct_option < 1 or correct_option > option_range:
            print("Invalid correct option number. Aborting test creation.")
            return
        query = "INSERT INTO tests (id, question, options, answer) VALUES (%s, %s, %s, %s)"
        values = (None, question, json.dumps(options), correct_option)
        self.__db_cursor.execute(query, values)
        print("Test created successfully!")
    
    def __no_of_question_exist(self):
        self.__db_cursor.execute("SELECT COUNT(*) FROM tests")
        return self.__db_cursor.fetchone()[0]        
    
    def __close_connection(self):
        """Function to close database connection"""
        if self.__db:
            self.__db.close()
        if self.__db_cursor:
            self.__db_cursor.close()