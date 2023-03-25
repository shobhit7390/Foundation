# time module in python

import time

# time.strftime()

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)

#time.sleep()

print("Hello User ! Wait for 5 seconds to get your Welcome msg..")
time.sleep(5)
print("Welcome to Python Course")


# time.time()

def usingWhile():
    i=0;
    while(i<1000):
        i=i+1
        print(i)

def usingFor():
    for i in range(1000):
        print(i)

init=time.time()
usingFor()
x=time.time()-init

init=time.time()
usingWhile()
y=time.time()-init

print(x)
print(y)

