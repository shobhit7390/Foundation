# Exception Handling
# It is used to avoid program hault if something goes wrong

a=input("Enter the value of a:")
print(f"Multiplication table of {a} is: ")

# for i in range(1,11):
#     print(f"{int(a)} * {i} = {int(a)*i}")

# print("Some lines of code")
# print("End of program")

# If string is passed in above code,then error will come rest lines will not be printed 
# Using try and except

try:
    for i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except Exception as e:
    print(e)                        # prints the error nd loop goes to rest lines 

print("Some lines of code")
print("End of program")

# You can handle mutliple errors using multiple exceptions after try block

try:
    num=int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number enterd is not an integer")
except IndexError:
    print("Index Error")