# Inheritance

# WHen a classs derives from another class . The child class will inherit all the public and protected properties and methods from the parent class


class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of the employee {self.id} is : {self.name}")



class Programmer(Employee):             # Inheritence
    def showLanguage(self):
        print("The default language is Python")



e1=Employee("Rohan",121)
e1.showDetails()
e2=Employee("Amber Sahai",125)
e2.showDetails()


e3=Programmer("Shobhit Y",131)
e3.showDetails()
e3.showLanguage()


