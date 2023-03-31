'''
Write a python code to print the count of valid strings and invalid strings from a given list of strings.
A string is considered as valid if it contains combinations of alphabets (in upper case or lower case) with/without spaces.

Define a function to check if a given string is valid or not i.e if it contains combinations of alphabets (in upper case or lower case) with/without spaces. 

This function will take a string as input and return True if the string is valid, otherwise will return False.


Example :
If the string given as argument is "Hello Good Morning", the function will return True.
If the string given as argument is "Purabi@gmail.com", the function will return False.


Using this function in main section, build the logic to print the count of valid strings and invalid strings from a given list of strings.

Refer to below instructions and sample input-output for more clarity on the requirement.

Instructions to write main section of the code:

a. You would require to write the main section completely, hence please follow the below instructions for the same.

b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence. 


1. Create a list of strings. To create the list,
i. First read the number of elements/strings you want to store in the list.
ii. Read a string and add it to the list. This point repeats for the number of elements/strings to be stored in the list (considered in the first line of input i.e. in point #1.i).

2. Next print the message "Count Of Valid Strings=". Followed by this print the count of valid strings found in the list.

3. Next print the message "Count Of Invalid Strings=". Followed by this print the count of invalid strings found in the list.


You can use/refer the below given sample input and output to verify your solution.

Sample Input (below) description:

The first line of input taken in the main section contains an integer value representing the number of elements/strings to be added to the list.

The next lines of inputs are the strings to be added to the list one after another and is repeated for the number of elements/strings given in the first line of input. (each line represents one string to be added to the list).


Sample Input:

4
Hello Good Morning
abcd123Fghy
India
progoti.c


Sample Output:

Count Of Valid Strings= 2
Count Of Invalid Strings= 2

'''

def check(lst_string):
    ans=[]
    valid_str=0
    invalid_str=0
    for str in lst_string:
        count_u=0
        count_l=0
        count_s=0
        for i in str:
            if i.isupper()==True:
                count_u+=1
            elif i.islower()==True:
                count_l+=1
            elif i.isspace()==True:
                count_s+=1
            else:
                break
        if (count_l+count_s+count_u)==len(str):
            valid_str+=1
        else:
            invalid_str+=1
    ans.append(valid_str)
    ans.append(invalid_str)
    return ans


n=int(input())
l=[]

for i in range(n):
    l.append(input())

ans=check(l)

print(f"Count Of Valid Strings={ans[0]}")
print(f"Count Of Invalid Strings={ans[1]}")

