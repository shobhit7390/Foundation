#--------if-else--------------

a=int(input("Enter your age: "))
print("Your age is: ",a)

if(a>18):
    print("You can drive")
    print("yes")
else:
    print("You can't drive")
    print("No")
print("Outside if-else")


#---------- elif-----------

num=int(input("Enter any number: "))

if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is 0")


#----------- Nested if-------------

num=int(input("Enter any number: "))

if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is bw 1-10")
    elif(num>10 and num<=20):
        print("Number is bw 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is 0")