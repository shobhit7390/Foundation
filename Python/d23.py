# List Methods

# append()

l=[23,8,2,9,2,14,2,56,3]
l.append(10)            # adds an element at the last of list
print(l)

print(l.index(2))       # prints the index of first occurence of an element
print(l.count(2))       # counts the occurence of an element

# copy()

# m=l                     # acts as reference
# m[0]=0                  # changes in actual list l not in list m
# print(l)
m=l.copy()
m[0]=0                  # changes in list m
print(l)

# insert()
l.insert(1,999)         # inserts an element at particular index,here index=1
print(l)

# reverse()

l.reverse()             # list in reverse order
print(l)


# sort()
l.sort()                # sorts in ascend. order
print(l)
l.sort(reverse=True)    # sorts a lit in descend. order
print(l)



# extend()

colors=["red","green","blue"]
rainbow=["yellow","violet","Pink","grey"]

k=colors+rainbow
print(k)

colors.extend(rainbow)      # adds rainbow at the end of list colors
print(colors)