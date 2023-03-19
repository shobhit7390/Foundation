# Getters and Setters

class MyClass:
    def __init__(self,value):
        self.value=value
    
    def show(self):
        print(f"Value is {self.value}")

    @property
    def ten_value(self):
        return 10*self.value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value/10
    
obj=MyClass(10)
print(obj.ten_value)
obj.show()

obj.ten_value=80       
print(obj.ten_value)
obj.show()


