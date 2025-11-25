class Human:
    property1:str
    
    #constructor
    def __init__(self):
        self.property1 = "HATER"
    
    # self must be the first parameter of any method in a class
    def talk(self, name: str='Ayomide'):
        print(f"Hello, I am {name}\nI have a property called {self.property1}")
    
    def _can_act(self):
        print("I can act")

ayomide = Human()
# ayomide.property1 = "MADHATTER CURIOSITY"
ayomide.talk('Dele')


class Mermaid(Human):
    def __init__(self):
        self.property1 = "MERMAID"
        
#Inheritance
class Man(Human):
    
    # constructor can be inherited from parent or overriden
    # def __init__(self):
    #     super().__init__()
        # self.property1 = "MAN"
        
    def walk(self):
        print("I can walk")
        
        
john = Man()
john.talk('John')


#Encapsulation
# Use __ to make a property private
# Use _ to make a proerty protected
class Person:
    
    __property1:str
    
    def __init__(self):
        self.__property1 = "SECRET"
        
    def reveal_secret(self):
        print(f"My secret property is {self.__property1}")
        
peter = Person()
peter.reveal_secret()
# print(peter.__property1)  # This will raise an AttributeError


        
        
ariel = Mermaid()
ariel._can_act()  # Inherited method from Human