# Magic/Dunder Methods

# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"
    
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    def __call__(self):
        print("Hello !")
    
    
e=Employee("Shobhit")

# print(e.name)
# print(len(e))