/*
A plumber wants to check whether a pipe junction where N incoming pipes and M outgoing pipes are balanced, and, if not, needs to balance the junction by adding an input pipe or an output pipe of a suitable capacity. At the junction, there are a set of input pipes and a set of output pipes. Each pipe has a rated capacity and an actual capacity. The actual capacity for each pipe is lower than the rated capacity by a constant R, the "rust factor", which depends on the material of the pipe, and is the same for all the pipes at the junction.

For example, if the rated capacity is 65, and R is 2, the actual capacity is 63.

A junction is balanced if the sum of the actual capacities of the input pipes is the same as the sum of the actual capacities of the output pipes. If it is not balanced, the plumber needs to add one input pipe or one output pipe to balance the junction, and determine the rated capacity of that added pipe.

Here we have N incoming pipes and M outgoing pipes. The incoming pipes may be of different rated capacities. Similarly, the outgoing pipes may also be of different rated capacities.

Find the rated capacity of the pipe required to make the junction balanced. If the combined actual capacity of the incoming pipes is more than the combined actual capacity of the outgoing pipes then the plumber will need to add an outgoing pipe. Conversely, if the combined…

Input:
The input has three lines:

The first line contains three space separated integers N M R denoting the number of incoming pipes, outgoing pipes and rust factor respectively.
The second line contains N space separated integers denoting the rated capacity of each incoming pipe.
The third line contains M space separated integers denoting the rated capacity of each outgoing pipe.

Output:
Print the rated capacity of the pipe required to balance the junction OR print "BALANCED" if the junction is already balanced.

input:
3 3 2
85 75 95
70 80 45

Output:
-62

Explanation:
There are 3 input pipes, 3 output pipes, and the rust factor is 2.

Example 2:
Input:
5 6 1
10 26 33 40 50
20 7 53 25 45 10

Output:
BALANCED

*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,m,r;
    cin>>n>>m>>r;
    
    int in[n];
    int out[m];
    
    int sum_in=0;
    
    for(int i=0;i<n;i++){
        cin>>in[i];
        sum_in+=in[i]-r;
    }
    
    int sum_out=0;
    
    for(int i=0;i<m;i++){
        cin>>out[i];
        sum_out+=out[i]-r;
    }
    
    if(sum_out<sum_in){
        int diff=sum_in-sum_out+r;
        cout<<(-1*diff)<<endl;
        return 0;
    }
    else if(sum_out>sum_in){
        int diff=sum_out-sum_in+r;
        cout<<diff<<endl;
        return 0;
    }
    else{
        cout<<"BALANCED"<<endl;
        return 0;
    }
    
}