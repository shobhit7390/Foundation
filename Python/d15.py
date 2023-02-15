import time

timestamp=int(time.strftime('%-H'))
if(timestamp<12):
    print("Good morning")
elif(timestamp>12 and timestamp<15):
    print("Good Afternoon")
elif(timestamp>=15 and timestamp<21):
    print("Good Evening")
elif(timestamp>=21):
    print("Good Night")
else:
    print("Good Noon")



"""
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)
"""

