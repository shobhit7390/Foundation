# Decorators 

# These are the functions that takes another function as an argument and returns a new function that modifies the behaviour of original function 

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")


def add(a,b):
    print(a+b)

# greet(hello)()
hello()

greet(add)(1,2)


