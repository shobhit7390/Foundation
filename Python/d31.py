# Sets in Python

# Unordered collection of elements ,do not have duplicate elements, these are unchangeable

s={2,4,4,2,6,5,8,8}
print(s)

info={"Shobhit",23,"Ghz",8.1,23}
print(info)

temp={}
print(type(temp))       # type: dict

# To create empty set
tmp=set()
print(type(tmp))


# ---------- Set Methods ----------

# union() and update()
s1={1,2,5,6}
s2={3,6,7,2}

print(s1.union(s2))

s1.update(s2)

print(s1,s2)

# intersection() and intersection_update()

cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Silicon Valley","Kabul","Madrid"}

cities3=cities1.union(cities2)
print(cities3)

cities3=cities1.intersection(cities2)
print(cities3)

# cities1.intersection_update(cities2)
# print(cities1)

cities3=cities1.symmetric_difference(cities2)
print(cities3)

cities3=cities1.difference(cities2)
print(cities3)

print(cities1.isdisjoint(cities2))

print(cities1.issuperset(cities2))
print(cities1.issubset(cities3))

# .add() and .remove() are used to add and remove elements from the set

# .remove() throws error if element you are removing is not present
# .discard() do not throws an error even if element is not present

# pop()             removes a random element
city={"Tokyo","Madrid","Berlin","Delhi"}
item=city.pop()
print(item)
print(city)

# 'del' is used to delete entire set

# del city
# print(city)            # Throws NameError

# 'clear' is used remove all elements not entire set like 'del'

city.clear()
print(city)



