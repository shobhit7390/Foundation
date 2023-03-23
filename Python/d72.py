# 'super' keyword in Python

# It is used to refer to the parent class . It is useful when a class inherits from multiple parent classes  and you want to call a method from one of the parent classes.


class ParentClass:
    def parent_method(self):
        print("This is the parent method 1")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Hello")
        super().parent_method()

    def child_method(self):
        print("This is the child method 2")
        super().parent_method()

child_object=ChildClass()
child_object.child_method()

child_object.parent_method()


#----- Another Example---------

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    # def __init__(self,name,id,lang):              # DRY
    #     self.name=name
    #     self.id=id
    #     self.lang=lang
    
    # We can use super to use constructor of Parent class
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

mack=Employee("Mack Orpid",121)
steve=Programmer("Steve Smith",532,"Python")

print(mack.name,mack.id)
print(steve.name,steve.id,steve.lang)

