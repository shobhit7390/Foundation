'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints:
1<=len(string)<=200

Each character in the string is an ascii character.

Output Format:

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
ABCDCDC
CDC

Sample Output:
2

'''


def count_substring(string,sub_string):
    s=0
    l1=len(string)
    l2=len(sub_string)

    for i in range(l1-l2+1):
        if string[i:i+l2]==sub_string:
            s+=1
    return s

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)