# Function arguments

# Default srguments

def average(a=1,b=9):                   
    print("The average is :",(a+b)/2)

average()       # It uses default values
average(5,1)    # It uses passed values in the function
average(5)      # Uses b defailt value 
average(b=3)    # Uses b=3 and a's default value


# Keyword arguments

average(b=21,a=7)       # Order of args can be changed


# Variable length arguments

def average3(*numbers):
    print(type(numbers))        # tuple
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is: ",sum/len(numbers))

average3(5,6,7)


# keyword arbitrary arguments

def name(**name):
    print(type(name))       # dict
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Singh",lname="Dhoni",fname="Mahendra")


# Return statement

def average_return(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c=average_return(5,6,7,10)
print(c)