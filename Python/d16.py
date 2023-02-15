# Match case is supported in python 3.10 not in below versions

x=int(input("Enter the value of x :"))

match x:
    case 0:
        print("")
    case 4:
        print("")
    case _ if x!=90:
        print(x," is not 90")
    case _ if x!=80:
        print(x," is not 80")
    case _:
        print(x)