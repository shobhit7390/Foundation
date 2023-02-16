# break statement

for i in range(12):
    if(i==10):
        break
    print("5 x",i,"=",5*(i))
print("Loop breaked")


print("-------")

# continue

for i in range(12):
    if(i==10):
        print("Skipped this iteration")
        continue
    print("5 x",i,"=",5*(i))
print("Loop breaked")
