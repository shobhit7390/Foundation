# Hybrid Inheritance

# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

class School:
    def func1(self):
        print("This function is in school.")
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 

object = Student3()
object.func1()
object.func2()



# Hierarchical Inheritance

# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
# Derivied class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
 
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

