/*
Problem Description:

You are given the scores of a football league among a set of teams. You need to find the winner of the league and print the name of winner and points earned by the team. Each team gets 3 points for a win, 1 point for a draw and 0 for a loss. The name of the teams is represented as upper case character viz. A B... Z.

Constraints:
There will only be one team which gets the highest points

Input:

There are many lines in the input.
The first line contains an integer, N, representing number of teams in the league. The next (N*(N-1))/2 lines contain three space separated strings <Team1, Team2, Score >
Here,
Team1 is the name of the home team.
Team2 is the name of the away team.
Score represents the score of the match, (M-N), where M represents the score of the home team and N represents the score of the away team.

Output:
The output should have two lines.
The first line should contain a character representing the name of the leader team.
The second line containing an integer representing the points won by the leader team.

Time Limit:
1

Explanation:

Example 1:
Input:
3
A B 2-1
B C 5-6
C A 2-1

Output:
C
6

Explanation:
A has won 1 match : 3 points
B has won 0 match: 0 points
C has won 2 match : 6 points

*/

#include<bits/stdc++.h>
using namespace std;

int main(){
    int teams;
    cin>>teams;

    string str;
    getline(cin,str);
    
    int scores[teams]={0};

    for(int i=0;i<(teams*(teams-1))/2;i++){
        string matchInfo;
        getline(cin,matchInfo);

        char home=matchInfo[0];
        char away=matchInfo[2];

        string scorehome="";
        string scoreaway="";

        int j=4;
        while(matchInfo[j] != '-'){
            scorehome+=matchInfo[j];
            j++;
        }
        j++;
        int x=stoi(scorehome);

        while(j<matchInfo.length()){
            scoreaway+=matchInfo[j];
            j++;
        }
        int y=stoi(scoreaway);

        if(x<y){
            scores[away-'A']+=3;
        }
        else if(x==y){
            scores[home-'A']+=1;
            scores[away-'A']+=1;
        }
        else{
            scores[home-'A']+=3;
        }
    }

    int index=-1;
    int highest=INT_MIN;

    for(int i=0;i<teams;i++){
        if(scores[i]>highest){
            highest=scores[i];
            index=i;
        }
    }

    cout<<char('A'+index)<<endl;
    cout<<highest<<endl;
    return 0;
}




