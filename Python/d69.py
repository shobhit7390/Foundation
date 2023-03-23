# Class methods in Python

# A class is a type of method that is bound to the class and not the instance of the class. In other words,it operates on the class as a whole rather than on a specific instance of the class. These are defined using '@classmethod' decorator. 

class Employee:
    companyName="Apple"
    def show(self):
        print(f"The name is {self.name} and company name is {self.companyName}")

    @classmethod                                # This method will actually change the value of class variable
    def changeCompany(cls,newCompany):          # Here class is passed as argument
        cls.companyName=newCompany

e1=Employee()
e1.name="Shobhit"
e1.show()

e1.changeCompany("Tesla")
e1.show()

print(Employee.companyName)

