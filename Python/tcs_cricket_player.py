'''
Sample Problem:

Create a class 'CricketPlayer' with below attributes.
cplayerName: string type
cplayed Country: set of strings
cplayerAge: int type
cpCountryFrom: string type
Create a constructor which takes all the above values in same sequence.


Create a class 'Solution' with attribute as set of players obtained from main function
Define two functions inside 'Solution' class.
✓countPlayers: it takes a string represents 'country name' as argument, and returns the total count of players belonging to that country.
✓getPlayerPlayed ForMaxCountry: It finds the name of player from players list of Solution class who has played against highest number of countries.

Input:

3
virat
5
aus
nz
eng
wi
pak
35
ind
raina
3
aus
pak
nz
34
ind
gayle
3
aus
ind
pak
42
wi
ind

Output:

2
virat

'''


class CricketPlayer:
    def __init__(self,cplayerName,cplayedCountry,cplayerAge,cpCountryFrom):
        self.cplayerName=cplayerName
        self.cplayedCountry=cplayedCountry
        self.cplayerAge=cplayerAge
        self.cpCountryFrom=cpCountryFrom

class Solution:
    def __init__(self,player_list):
        self.player_list=player_list
    
    def countPlayers(self,check_country):
        count=0
        for i in self.player_list:
            if i.cpCountryFrom.lower()==check_country.lower():
                count=count+1
        return count

    def getPlayerPlayedForMaxCountry(self):
        max_country=0
        max_pname=''
        for i in self.player_list:
            if max_country<len(i.cplayedCountry):
                max_country=len(i.cplayedCountry)
                max_pname=i.cplayerName
        return max_pname


player_obj=[]
n=int(input())

for i in range(n):
    cplayerName=input()
    cplayedCountry=[]
    count_playedCountry=int(input())
    for j in range(count_playedCountry):
        cplayedCountry.append(input())
    cplayedCountry=set(cplayedCountry)
    cplayerAge=int(input())
    cpCountryFrom=input()

    player_obj.append(CricketPlayer(cplayerName,cplayedCountry,cplayerAge,cpCountryFrom))


sol=Solution(player_obj)

check_country=input()

print(sol.countPlayers(check_country))
print(sol.getPlayerPlayedForMaxCountry())