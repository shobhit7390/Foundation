# Loops

# In strings
name="Shobhit Yadav"
for i in name:
    print(i,end=", ")
print("")

# In lists

colors=["Red","Green","Blue","White"]

for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k+1)

# step argument in range

for i in range(1,20,2):     # 2 here is step 
    print(i)