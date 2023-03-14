# Constructors 

# It is a unique function that gets automatically called when an object is created of a class
# Main purpose is to initialise or assign values to the data members of that class 

class Person:

    def __init__(self,n,o):             # Constructor 
        print("Hey I am a person")
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("Shobhit","SDE")
b=Person("Neety","HR")

a.info()
b.info()

print(a.name)