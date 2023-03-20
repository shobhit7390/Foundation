/*
Given square matrix,calculate absolute diff. between the sum of its 2 diagonals.

Input:
3
1   2   3
4   5   6
9   8   9

Output:
2

Explanation:

1+5+9=15
3+5+9=17
So, abs diff=|15-17|=2
*/


#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;

    int arr[n][n];

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
    }
    int suml=0;
    int sumr=0;

    int i=0;
    while(i!=n){
        suml+=arr[i][i];
        i++;
    }

    i=0;
    int j=n-1;
    while(i!=n && j>=0){
        sumr+=arr[i][j];
        i++;
        j--;
    }

    cout<<"Absolute difference is:"<<abs(suml-sumr)<<endl;
}