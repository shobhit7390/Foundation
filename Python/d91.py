# Generators in Python

# Generators allow you to generate the values on-the-fly.

def my_generator():
    for i in range(10):
        yield i

gen=my_generator()              # Generator object

print(next(gen))                # Generates value when it is called
print(next(gen))
print(next(gen))
print(next(gen))

for j in gen:
    print(j)



    