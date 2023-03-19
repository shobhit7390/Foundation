# Access Modifiers in Python

# Public modifiers
class Employee:
    def __init__(self,name,age):
        self.name=name              # Public variable
        self.age=age                # Public variable


obj=Employee("Shekhar",28)
print(obj.age)
print(obj.name)         # Directly accessed


# Private modifier
# double underscore '__' is used before the name

class Student:
    def __init__(self,age,name):
        self.__age=age                  # An indication of private variable bcz of '__' 
        self.__name=name

    def __func(self):                   # Indication of private method due to '__'
        self.y=22
        print(self.y)

stu=Student(22,"Shobhit")
# print(stu.__age)                  # Cant be accessed directly like this


# ********* But it can be accessed indirectly using name mangling*******

print(stu._Student__age)
print(stu._Student__name)


# Protected modifier
# It can only be accessed by class itself and its subclasses


class Course:
    def __init__(self):
        self._name="Python"

    def _funcName(self):                # Protected method
        return "It is a computer language"
    
class User(Course):         # Inherited class
    pass

c=Course()
u=User()

# Calling by object of Course class
print(c._name)
print(c._funcName())


# Calling by object of User class
print(u._name)
print(u._funcName())




