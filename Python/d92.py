# Function Caching Python

# Technique for improving the performance of the program by storing the results of the function call so that you can reuse the results instead of recomputing them every time the function is called .
# This can be achieved by functools.lru_cache decorator. It used to cache the results  of a function so that you can reuse it.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

print("-------------")

print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(61))
print("Done for 61")


