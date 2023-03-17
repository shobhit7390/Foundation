'''
Associate for given Transportation

Problem Statement:
Create class Associate with below attributes:
id-int
name-string
technology=string
experienceinYears-int

Create class Solution and implement static method "associatesForGiven Technology" in the Solution class. This method will take array of Associate objects and a search Technology string as parameters. And will return another array of Associate objects where the search Technology String matches with the original array of Associate object's technology attribute (case insensitive search) and experienceInYears attribute should be multiples of 5

Write necessary getters and setters
Before calling "associatesForGiven Technology" method in the main method, read values for five associate objects referring the attributes in above sequence along with a String search Technology. Then call the "associatesForGiven Technology" method and write the logic to print the ios in the main method


Input:

5
101
Alex
Java
15
102
Albert
Unix
20
103
Alferd
Testing
13
104
Alfa
Java
15
105
Almas
Java
29
Java

Output:

101
104

'''



class Associate:
    def __init__(self,id1,name,technology,experienceInYears):
        self.id1=id1
        self.name=name
        self.technology=technology
        self.experienceInYears=experienceInYears

class Solution:
    @classmethod
    def associatesForGivenTechnology(cls,arrAssociates,searchTechnology):
        result=[]
        for i in arrAssociates:
            if i.technology.lower()==searchTechnology.lower() and i.experienceInYears%5==0:
                result.append(i.id1)
        return result

n=int(input())
arrAssociates=[]

for i in range(n):
    id1=int(input())
    name=input()
    technology=input()
    experienceInYears=int(input())

    arrAssociates.append(Associate(id1,name,technology,experienceInYears))

searchTechnology=input()

answer=Solution.associatesForGivenTechnology(arrAssociates,searchTechnology)

for i in answer:
    print(i)


