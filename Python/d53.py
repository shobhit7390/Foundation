# map() filter() reduce()

# --------map() 

def cube(x):
    return x*x*x

l=[1,2,4,8,6,3,4,4]
# newl=[]

# for item in l:
#     newl.append(cube(item))

# newl=list(map(cube,l))
newl=list(map(lambda x:x*x*x,l))
print(newl)


# ------filter()

def filter_fuction(a):
    return a>4

l2=list(filter(filter_fuction,l))
print(l2)

# -------reduce()

from functools import reduce

nums=[1,2,3,4,5,6]

sum=reduce(lambda x,y:x+y,nums)
print(sum)



