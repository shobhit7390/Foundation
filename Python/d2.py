        ## Strings in Python

txt="The best things in life are free !"
print(len(txt))
print("free" in txt)        # Results true 

if "free" in txt:
    print("Yes,'free' is present in txt")
    
# 'not in' is used to check the presence of certain phrase or char
if "expensive" not in txt:
    print("No,'expensive' is not present")
    

        # Slicing in Python

a="Hello, Brother!"
print(a[2:5])           # 5th position is not included
print(a[2:])            # prints till end
print(a[:8])            # prints from starting index till 7th char
print(a[::-1])          # print reversed string

        # Negative Indexing
b="Hello World !"
print(b[-5:-2])         # -2 not included


        # Modification in Strings
c="Hello, Brother!"
print(c.upper())        # Converts all letters into capital
print(c.lower())

d="  Hello,Coder!       "
print(d.strip())               # Removes Whitespaces (Spaces before and after the actual text)
print(c.replace("He","J"))       # Replaces a string/letter with other string
print(c.split(","))

        # Concatenation
a1="Hello,"
b1="World!"
print(a1+b1)
print(a1+"my "+b1)


        # format()
age=22
txt="My name is Shobhit, and I am {}"
print(txt.format(age))              # It takes the paased argument ,formats it and places them in string at the place of '{}'
                                    # Multiple arguments can also be passed

# Index numbers can be used 
quantity=3
itemno=567
price=49.61
myorder="I want to pay {2} dollars for {0} pieces of item_no {1}"
print(myorder.format(quantity,itemno,price))




