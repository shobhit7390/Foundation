# Lists

# Ordered collection of items , may have different data types

list1=[1,2,3,4,5]
list2=["Red","Green","Blue"]
print(list1)
print(list2)
print(type(list1))

# Indexing starts with 0

details=[101,"Rohan",8.2,"Ghaziabad"]
print(details)
print(details[0])
print(details[1])
print(details[2])

print(len(details))     # 4

# Negative indexing
print(details[-1])          # Index from starting : len(details) -1
print(details[-3])

# To check existence of elemnt in a list
# Same thing applies in Strings as well

if "Rohan" in details:      # String in list
    print("yes")
else:
    print("No")

if 3 in list1:              # Number in list
    print("yes")
else:
    print("No")

# Slicing in list
print(list1[1:5])
print(list1[2:-1])

print(list1[1:5:2])         # Jump index 2

print(details[::-1])        # Reverse the list

# List Comprehension

lst=[i for i in range(8)]
print(lst)

lst2=[i*i for i in range(16) if i%2==0]
print(lst2)