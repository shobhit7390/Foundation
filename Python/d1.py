
#Indentation

if 5>2:
    print("Five greater than 2")
        # print("This line will not be executed")
        
# Variables

x=5                     # type int
y="Hello Duniya"         #type str

#print(x+y)     # Error due to different data types
print(x,y)

print(type(x))          #type() to get data type of Variables

                # Variables are case-sensitive

#Assigning multiple Variables
x,y,z="Apple","Orange","Grapes"
print(x,y,z)

# Unpack a list Collection
fruits=["Apple","Orange","Grapes"]
print(x,y,z)


        ########## Global Variables
        
x="awesome"
def myfunc():
    x="fantastic"
    print("Python is "+x)
myfunc()
print("Python is "+x)

def func1():
    global x        # To create a global variable inside a function
    x="pretty"
func1()
print("Python is "+x)

