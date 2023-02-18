# Dictionay Methods

emp1={122:45,123:89,124:67,125:78}
emp2={222:67,245:91}

# update ()
emp1.update(emp2)
print(emp1)

# clear()
emp2.clear()
print(emp2)

# popitem()         # removes last key:val pair
emp1.popitem()
print(emp1)

# pop()             # removes specified key:value pair
emp1.pop(122)
print(emp1)

# empty dict
empt={}
print(type(empt))
print(empt)

# 'del' is used to delete entire dictionary------> del emp2
del emp1[125]       # deleted key 125 and its value
print(emp1)