# Multiple Inheritance

# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class. 

class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name


o=DancerEmployee("Kathak","Shivani")
print(o.name)
print(o.dance)

o.show()                # The name is Shivani will be printd because------> Employee is inherited first in DancerEmployee class

print(DancerEmployee.mro())         # Method Resolution Order
                                    # The way python resolves the method or attributes


