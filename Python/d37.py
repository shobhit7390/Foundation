# 'finally' keyword in try except block

try:
    l=[1,2,3,4]
    i=int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occurred")
finally:
    print("I am always executed")
# print("I am always executed")

# ABove if we do not use finally insted we use a print statmnt then also the op will be same
# But when we put this code in a function then scenario changes

def func1():
    try:
        l=[1,2,3,4]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")

x=func1()
print(x)

# ****In above function even after returning a value, 'finally' block code runs****



