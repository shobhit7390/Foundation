# Sponsor class

'''

Sample Problem:

Create a class 'Sponsor' with below attributes.
sName: string type
sCompany: string type
stieups: list of strings
sCategory: string type
Create a constructor which takes all the above values in same sequence.

Define two functions outside of all classes.

✓ getSponsor: it takes a string represents 'sCategory' as argument, and returns the name of sponsor belong to that category.
✓ findSponsorWithMaxTieups: It finds the name of sponsor from sponsors list who has maximum number of tieups.


Sample Input:

3
bade
badetutorials
5
badetutind
badetutaus
badetuteng
badetutnz
badetutrsa
education partner
sony
sony corporation
2
sonyaus
sonyeng
entertainment partner
aututorials
aututorialspoint
3
auaus
aueng
aunz
education partner
education partner

Output:
aututorials
bade
bade

'''

def getSponsor(slist,category_check):
    names=[]
    for s in slist:
        if(s.sCategory.lower()==category_check.lower()):
            names.append(s.sName)

    if(len(names)>0):
        names.sort()
        return names
    else:
        return None
    
def findSponsorWithMaxTieups(slist):
    mx=0
    name=''
    for s in slist:
        if(len(s.stieups)>mx):
            mx=len(s.stieups)
            name=s.sName
    
    return name


class Sponsor:
    def __init__(self,sName,sCompany,stieups,sCategory):
        self.sName=sName
        self.sCompany=sCompany
        self.stieups=stieups
        self.sCategory=sCategory

n=int(input())
sponsors=[]

for i in range(n):
    sName=input()
    sCompany=input()
    ntieups=int(input())
    my_tieups=[]
    for j in range(ntieups):
        my_tieups.append(input())
    sCategory=input()

    obj=Sponsor(sName,sCompany,my_tieups,sCategory)
    sponsors.append(obj)


category_check=input()

res1=getSponsor(sponsors,category_check)
res2=findSponsorWithMaxTieups(sponsors)

if(res1==None):
    print("No matching record")
else:
    for name in res1:
        print(name)


if(res2==None):
    print("No matching record")
else:
    print(res2)




