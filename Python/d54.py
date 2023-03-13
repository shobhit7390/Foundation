# is vs '=='

a=4
b="4"

# 'is'
print(a is b)                 # Exact location of oject in memory

# '=='
print(a==b)                  # comapares value


a=[1,3,23]
b=[1,3,23]

print(a is b)       # False
print(a==b)         # True


a=3
b=3

# Python allocates same memory for constants
print(a is b)       # True
print(a==b)         # True

