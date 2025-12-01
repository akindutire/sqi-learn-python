from student import Student
from admin import Admin

class CBTProject:
    def __init__(self):
        self.__student = Student()
        self.__admin = Admin()
        
    def orchestrate(self):
        print("Welcome to CBT CLI application...\n")
        
        self.__admin.orchestrate()
        self.__student.orchestrate()


# This implies that this file is being run directly
if __name__ == "__main__":
    app = CBTProject()
    app.orchestrate()