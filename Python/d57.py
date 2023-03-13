# OOPS 
# Classes and objects
# Class is a blueprint for an object

class Person:
    name="Shobhit"
    occupation="SDE"
    Salary=50000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()

print(a.name)
print(a.occupation)
a.info()

b=Person()
b.name="Nitika"
b.occupation="HR"

b.info()

a.name="Abhishek"
a.occupation="Advocate"
print(a.name)
print(a.occupation)
a.info()




