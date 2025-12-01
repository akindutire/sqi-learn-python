from student import Student
from admin import Admin

class CBTProject:
    def __init__(self):
        self.__student = Student()
        self.__admin = Admin()
        
    def orchestrate(self):
        self.__admin.bootstrap()
        # self.__student.register()
        # self.__student.take_test()
        # self.__student.show_results()
        