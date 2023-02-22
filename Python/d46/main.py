# 'os' module
# provides functions for interacting with the system (reading ,writing,running system commands)

import os

if(not os.path.exists("10_days_of_code")):
    os.mkdir("10_days_of_code")                     # It creates a directoy '10_days_of_code' if not exists

# for i in range(0,10):
#     os.mkdir(f"10_days_of_code/Day{i+1}")           # It creates Day1-Day10 directory inside '10_days_of_code'


# os.rename()

for i in range(0,10):
    os.rename(f"10_days_of_code/Day{i+1}",f"10_days_of_code/Tutorial {i+1}")


