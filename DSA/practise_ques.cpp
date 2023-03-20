/*
Write a program to find the smallest integer value 'b':

For the given value of'a'. If we multiply the digits of 'b', we should get the exact value of 'a'. Result 'b' must contain more than one digit.

Constraints:
1<=a<=10000

Examples:

Input: 10
Output: 25
Explanation: 2*5 = 10. Hence 25 is the smallest value
for 10.

Input: 56
Output: 78
Explanation: 7*8 = 56

Input: 150
Output: 556
Explanation: 5*5*6 = 150

Input: 13
Output: -1

Instructions:
Input must be a single integer value.
Print -1 if result not found.​
*/

#include<bits/stdc++.h>
using namespace std;

int helper(int A){
    if(A<10)
        return (A+10);
    
    stack<int> s;
    
    for(int i=9;i>=2;i--){
        while(A%i==0){
            s.push(i);
            A=A/i;
        }
    }
    if(A!=1)
        return -1;
    
    int b=0;
    while(!s.empty()){
        int x=s.top();
        s.pop();
        b=b*10+x;
    }
    return b;
}

int main()
{
    int A;
    cin>>A;
    
    cout<<helper(A)<<endl;
}


