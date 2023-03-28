# Player Class
'''

Create a class Player with below attributes
playerName:(string type)
String playerCountry:(string type)
playerAge:(int type)
noOfMatches: (int type)
noOfRuns:(int type)
noOfWickets:(int type)

Create a constructor which takes all the above attributes in the same sequence.
Define another class Team with the below member functions.

getMinRuns: Which takes list of Player objects as input parameter and returns the player details who scored Minimum runs(Assume that no player has same number of runs scored). 
getMaxWickets: which takes list of Player objects as input parameter and returns the player, who took the Maximum wickets(Assume that no player has same number of wickets).

Instructions to write main function:
a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the mian program which is inline to the "sample input descrption section" mentioned below and to read the data in the same sequence.
c. create the respective objects(Player and Team) with the given sequence of arguments to fulfill the_init_ method as mentioned in requirement, defined in the respective classes referring to the below instructions.
1. Create a list of players. To create the list,
1. First read the number of players you want to store in the players list.
2.Read the values for the players. This point repeats for the number of players to be added to the list
(consider the input taken in point 1 above).
ii. Create a Team object
d.Call the functions getMinRuns and getMaxWickets repectively by passing the player list created in #c.l as argument and display the results.


You can use/refer the below given sample input and output for more details of the format for input and output.
Note: Request not to initialize resultant object with None

Sample Input description:
a.First line represents the integer value which represents the number of player objects.
b. Next 6 lines of input represents one player specific data as below one by one in each line.
PlayerName
playerCountry
playerAge
noOfMatches
noOfRuns
noOfWickets
c. The point #b repeats for the number of objects mentioned in the point#a

Input:

5
Sachin
India
40
350
15000
120
Klusnar
SountAfrica
37
270
3000
250
Dhoni
India
38 
345
12000
0
RickyPointing
Australia
42
290
11000
3
Dravid
India
39
320
11200
12

Output:

Klusnar
3000
SouthAfrica
Klusnar
250
SouthAfrica

'''


class Player:
    def __init__(self,playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets):
        self.playerName=playerName
        self.playerCountry=playerCountry
        self.playerAge=playerAge
        self.noOfMatches=noOfMatches
        self.noOfRuns=noOfRuns
        self.noOfWickets=noOfWickets

    
class Team:
    def __init__(self,players):
        self.players=players

    def getMinRuns(self):
        info=[]
        for i in self.players:
            info.append(i.noOfRuns)

        ans=[]
        min_runs=min(info)

        for i in self.players:
            if(i.noOfRuns==min_runs):
                ans.append(i.playerName)
                ans.append(min_runs)
                ans.append(i.playerCountry)

        return ans

    def getMaxWickets(self):
        info=[]
        for i in self.players:
            info.append(i.noOfWickets)

        ans=[]
        max_wickets=max(info)

        for i in self.players:
            if(i.noOfWickets==max_wickets):
                ans.append(i.playerName)
                ans.append(max_wickets)
                ans.append(i.playerCountry)

        return ans


n=int(input())
players=[]

for i in range(n):
    playerName=input()
    playerCountry=input()
    playerAge=int(input())
    noOfMatches=int(input())
    noOfRuns=int(input())
    noOfWickets=int(input())

    obj=Player(playerName,playerCountry,playerAge,noOfMatches,noOfRuns,noOfWickets)
    players.append(obj)

t=Team(players)

res1=t.getMinRuns()
res2=t.getMaxWickets()

for i in res1:
    print(i)

for i in res2:
    print(i)



