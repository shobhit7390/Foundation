# Local and Global variables

x=4
print(x)

def hello():
    global x                # Nw x value can be changed inside the function
    x=10
    y=1
    print(f"Local x is {x}")
    print("Hello User!")

print(f"Global x is {x}")
hello()
print(f"Global x is {x}")

# print(y)          # Error beacuse of accessing local variable outside the func