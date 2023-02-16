# Functions

# User defined are created using def keyword

def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")

def islesser(a,b):
    pass            # nothing happens ,avoids error,code may be written in future

a=8
b=10
calculategmean(a,b)
isgreater(a,b)

calculategmean(10,5)
isgreater(10,5)

# Built in functions  
# these are predefined or pre-coded in python eg. max(),min(),len(),tuple(),list(),etc