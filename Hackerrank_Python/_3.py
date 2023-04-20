'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Sample Input:
5
2 3 6 6 5
Sample Output:
5

'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    secondTop=-100
    top=-100
    
    for i in arr:
        if i>top:
            secondTop=top
            top=i
        if i>secondTop and i!=top:
            secondTop=i
    print(secondTop)

