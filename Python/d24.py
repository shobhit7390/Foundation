# tuple

# Tuples cannot be changed whereas Lists can be

t=(1)
print(type(t),t)        # type:<class 'int'> 1

t=(1,)
print(type(t),t)        # <class 'tuple'> (1,)

# t[0]=99       # throws type error

tup=(1,2,"green",17,True)
print(tup)

# Indexing
print(tup[0])
print(tup[2])

# Check elements's presence

if 2 in tup:
    print("Yes present")
else:
    print("No")

# Slicing same as Lists

tup2=tup[1:4]
print(tup2)