# os.listdir() function

import os

folders=os.listdir("10_days_of_code")

print(folders)

print(os.getcwd())              # for current working directory

for folder in folders:
    print(folder,end=" ")
    print(os.listdir(f"10_days_of_code/{folder}"))