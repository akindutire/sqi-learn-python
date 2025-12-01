from config import Config
class Admin:
    def __init__(self):
        self.config = Config()
        self.db_cursor = self.config.get_db_cursor()
        
    def __create_test(self):
        question = str(input("Enter question: ")).strip()
        
        option_range = int(input("Enter number of options for the question: "))
        options = []
        
        for i in range(option_range):
            option = str(input(f"Enter option {i+1}: ")).strip()
            options.append(option)
        
        correct_option = int(input("Enter correct option (1, 2, 3, etc): ")).strip()
        
        if correct_option < 1 or correct_option > option_range:
            print("Invalid correct option number. Aborting test creation.")
            return
        query = "INSERT INTO tests (question, options, answer) VALUES (%s, %s, %s)"
        values = (question, ','.join(options), correct_option)
        self.db_cursor.execute(query, values)
        print("Test created successfully!")
    
    def __no_of_question_exist(self):
        self.db_cursor.execute("SELECT COUNT(*) FROM tests")
        count = self.db_cursor.fetchone()[0]
        return count
    
    def bootstrap(self):
        print("Admin Module Started...\n")
        print("""
              1. Create test
              0. Exit/Skip test creation
              """)
        
        while True:
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
            self.db_cursor.close()
            exit()
         
        # close db cursor
        self.db_cursor.close()
        