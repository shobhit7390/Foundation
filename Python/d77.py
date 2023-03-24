# Operator Overloading

# Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 


class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    

v1=Vector(3,5,6)
print(v1)

v2=Vector(2,4,7)
print(v2)

print(v1+v2)
print(type(v1+v2))


