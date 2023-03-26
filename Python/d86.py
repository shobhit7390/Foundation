# Walrus Operator

# Walrus-operator is another name for assignment expressions. According to the official documentation, it is a way to assign to variables within an expression using the notation NAME := expr. The Assignment expressions allow a value to be assigned to a variable, even a variable that doesn’t exist yet, in the context of expression rather than as a stand-alone statement.


numbers=[1,2,3,4,5]

while(n:=len(numbers))>0:
    print(numbers.pop())

#---------Another Example-------

'''
foods=list()

while True:
    food=input("What food do you like? : ")
    if(food=="quit"):
        break
    foods.append(food)

'''

foods=list()
while(food:=input("What food do you like? : ")) != "quit":
    foods.append(food)

print(foods)


