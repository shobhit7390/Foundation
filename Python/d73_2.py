# Magic/Dunder Methods

# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

from d73_1 import Employee

e=Employee("Shobhit")

print(str(e))
print(repr(e))

# print(e.name)
# print(len(e))

e()