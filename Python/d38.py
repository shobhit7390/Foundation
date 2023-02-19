# Raising Custom Errors
# We use 'raise' keyword to raise errors

a=input("Enter a number b/w 5 and 9 :")


if a=="quit":
    print("Only this string is valid")
else:
    if(int(a)<5 or int(a)>9):
        raise ValueError("Value should be b/w 5 and 9")


