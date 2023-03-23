# Class Methods as alternative constructors

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))          # Returns a class object as an instance
    

e1=Employee("Mack",120000)
print(e1.name)
print(e1.salary)

string="John-175000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)


# Another example


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))
    
person=Person.from_string("Meg Lanning,31")

print(person.name,person.age)

