from student import Student
from admin import Admin

class CBTProject:
    def __init__(self):
        self.__student = Student()
        self.__admin = Admin()
        
    def orchestrate(self):
        print("Welcome to CBT CLI application...\n")
        self.__admin.bootstrap()
        # self.__student.register()
        # self.__student.take_test()
        # self.__student.show_results()
        

# This implies that this file is being run directly
if __name__ == "__main__":
    app = CBTProject()
    app.orchestrate()