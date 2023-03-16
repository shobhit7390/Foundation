'''
Create a class Traveler with below attributes
travelerName: (string type)
traveled Country: (list of string type represents the names of the country the traveler has travelled.) 
travelerAge: (int type)
countryFrom :(string type)

Create a constructor which takes all the above attributes in the same sequence.
Define another class Travel Agency with below attributes:
travelerList: (list of Traveler objects)
and having the below member functions:

countTravelersTraveledCountry: Which takes a string representing the name of a country as input, and returns the count of travelers from the travelerList of Travel Agency who has travelled that country.

getTravelerTravelledMaxCountry: finds the traveler who has travelled highest number of countries and returns the name of that traveler. If more than one such travelers are there having the highest count of countries travelled method returns the name of the traveler whose name appears first in the list as taken as input.

Instructions to write main function:

a. You would require to write the main section completely, hence please follow the below Instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence.
c. Create the respective objects(Traveler and TravelAgency) with the given sequence of arguments requirement, defined in the respective classes to fulfill the init_method as mentioned in referring to the below instructions. Insight


L. Create a list of travelers. To create the list,
1. First read the number of travelers you want to store in the list.
2. Read the values for the travelers, create the Traveler object and add to the list. This point repeats for the number of traveler to be added to the list (consider the input taken in point 1 above).
a. First read the name of the traveler.
b. Then, read a number representing the count of countries travelled.
c. Read a string representing the name of the country countries and add to the list. This point repeats for the count taken in point 
#2.b above.
d.Finally read values for travelerAge and countryFrom.


Sample test case-input:

5
Sachin
4
Japan
Brazil
China
Nepal
40
India
Kamini
4
Denmark
Australia
Indonesia
Ghana
37
Nepal
Saurav
6
Brazil
Bhutan
Afganistan
UK
Nepal
Newzealand
32
Bangladesh
Ricky
3
Australia
Europe
Germany
42
UK
Dravid
2
India
Bhutan
39
Pakistan
Australia

O/p:

2
Saurav

'''




class Traveler:
    def __init__(self,travelerName,traveledCountry,travelerAge,countryFrom):
        self.travelerName=travelerName
        self.traveledCountry=traveledCountry
        self.travelerAge=travelerAge
        self.countryFrom=countryFrom

class TravelAgency:
    @classmethod
    def countTravelersTraveledCountry(cls,list_obj,find_country):
        counter=0
        for i in list_obj:
            if find_country in i.traveledCountry:
                counter+=1
        return counter
    
    @classmethod
    def getTravelerTravelledMaxCountry(cls,list_obj):
        max_con=0
        max_name=''
        for i in list_obj:
            list1=i.traveledCountry
            if max_con<len(list1):
                max_con=len(list1)
                max_name=i.travelerName
        return max_name


n=int(input())
list_obj=[]

for i in range(n):
    travelerName=input()
    c=int(input())
    traveledCountry=[]
    for j in range(c):
        traveledCountry.append(input())
    travelerAge=int(input())
    countryFrom=input()

    list_obj.append(Traveler(travelerName,traveledCountry,travelerAge,countryFrom))

find_country=input()

ans1=TravelAgency.countTravelersTraveledCountry(list_obj,find_country)
ans2=TravelAgency.getTravelerTravelledMaxCountry(list_obj)

print(ans1)
print(ans2)


