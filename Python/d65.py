# Static Methods

# Often used to create utility functions that dont need access to instance data.They are defined using @staticmethod decorator

class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
    
result=Math.add(1,2)
print(result)

# We can also use it using object function

a=Math(5)
print(a.num)

a.addtonum(7)
print(a.num)

print(a.add(5,6))
print(Math.add(5,6))
