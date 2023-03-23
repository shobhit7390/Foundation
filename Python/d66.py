# Instance variable and Class variables

# Class variables are defined at the class level and are shared among all instances of the class.The are defined outside any method and are usually used to share info that is common to all instances.

# Instance variable are defined a the instance level and are unique to each instance.The are defined inside the __init__ method and store the info that is spcific to an instance.


class Employee:
    companyName="Apple"
    no_of_employee=0

    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.no_of_employee+=1

    def showDetails(self):
        print(f"The name of employee is {self.name} and the raise amount in {self.no_of_employee} sized {self.companyName} company is {self.raise_amount}")

emp1=Employee("Shobhit Yadav")
emp1.raise_amount=0.3
emp1.companyName="Apple India"
emp1.showDetails()

Employee.companyName="Google"
print(Employee.companyName)

emp2=Employee("Abhishek")
emp2.companyName="Nestle"
emp2.showDetails()



