# Tuple Methods

# Change items in tuple
countries=("Spain","Italy","India","Germany","England","America")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)


# Concatenate

country1=("Spain","Italy")
country2=("India","Germany","England","America")

countries=country1+country2
print(countries)


# count()

tuple1=(0,1,2,2,2,3,4,2,8,90)
print("Count of 2 in tuple1 is :",tuple1.count(2))

# index()
print("Index of 2 in tuple1 is :",tuple1.index(2))      # First occurence

print("Index of 2 in tuple1 is :",tuple1.index(2,4,9))  # for specified window: tuple.index(element,start,end)      
# If 2 not present throws error

# len()
print(len(tuple1))