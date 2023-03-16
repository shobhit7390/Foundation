'''
Create class Medicine with below attributes:
MedicineName-String
batch-String
disease-String
price-int

Create class Solution and
implement static method "getPriceByDisease" in the Solution class. This method will take array of Medicine objects and a disease String as parameters.
And will return another array of Integer objects where the disease String matches with the original array of Medicine object's disease attribute (case insensitive search).
Write necessary getters and setters.
Insight
Before calling "getPriceByDisease" method in the main method, read values for four Medicine objects referring the attributes in above sequence along with a String disease.
Then call the "getPriceByDisease" method and print the result.


Input:

4
dolo650
FAC124W
fever
100
paracetamol
PAC545B
bodypain
150
almox
ALM7475
fever
200
aspirin
flu
ASP849Q
250
fever

Output:
100
200


'''

class Medicine:
    def __init__(self,MedicineName,batch,disease,price):
        self.MedicineName=MedicineName
        self.batch=batch
        self.disease=disease
        self.price=price

class Solution:
    @classmethod
    def getPriceByDisease(cls,list_Med,dis):
        result=[]
        for i in list_Med:
            if i.disease.lower()==dis.lower():
                result.append(i.price)
        return result



n=int(input())
list_Med=[]

for i in range(n):
    MedicineName=input()
    batch=input()
    disease=input()
    price=int(input())

    list_Med.append(Medicine(MedicineName,batch,disease,price))

dis=input()
answer=Solution.getPriceByDisease(list_Med,dis)

for i in answer:
    print(i)



