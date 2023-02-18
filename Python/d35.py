# for loop with else

for i in []:
    print(i)
else:
    print("Sorry no i")

# ****if 'break' is used in for the it will not go in else part****
# else in for loop menas for loop has gone till last element then it comes to the else part

for i in range(7):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")