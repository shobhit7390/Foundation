# Lambda Functions
# It is a small asynchronous function without a name. It is defined using a 'lambda' keyword


# def double(x):
#     return x*2

double=lambda x: x*2
cube=lambda x:x*x*x

avg=lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(2))
print(avg(2,4,6))

def apple(fx,value):
    return 6+fx(value)

# print(apple(cube,2))
print(apple(lambda x:x*x*x,2))