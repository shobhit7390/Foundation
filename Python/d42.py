# Enumerate in python

# It gives the value as well as its index 

marks=[12,56,32,99,91,32,14,56]

index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("Awesome result!")
    index+=1

# Instead of using index and incrementing it we can directly use

for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Appreciable Result!")


# In strings

fruits=['apple','banana','mango','papaya']

for i,fruit in enumerate(fruits):
    print(i,fruits[i])

