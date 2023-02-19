# KBC Code challenge

ques=[
    ["Which language was used to create facebook?","Python","French","Js","PHP",4],
    ["Which among the following teams has played World Cup (Cricket) final match maximum number of times, but could not win a single trophy?","England","WI","Sri Lanka","South Africa",1],
    ["The classical/folk dances namely Kathakali and Mohiniyattam belong to …?","Tripura","Himachal Pradesh","West Bengal","Kerala",4],
    ["Pandit Ravi Shankar is related to …?","Sitar","Table","Flute","Saroda",1],
    ["The trophy All India Maharaja Ranjit Singh Gold Cup is related to …?","Hockey","Badminton","Cricket","Basketball",1],
    ["Air Force Academy is located in...?","Kolkata","Dundigul","Gopalpur","Guindy",2],
    ["The term ''hook serve'' is related to …?","Football","Swimming","Volleyball","Basketball",3],
    ["Big Ben is located in …?","USA","UK","Russia","Italy",2],
    ["Which among the following is popular as City of Seven Hills?","New York","Rome","London","Paris",2],
    ["Which among the following is the biggest ocean?","Atlantic","Indian","Pacific","Arctic",3]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

money=0

for i in range(0,len(ques)):
    question=ques[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")

    user_ans=int(input("Enter your answer(1-4) or 0 to quit:"))

    if user_ans==0:
        money=levels[i-1]
        break

    if user_ans==question[-1]:
        print(f"Correct Answer! You have won Rs. {levels[i]}")
        if i==4:
            money=10000
        elif i==9:
            money=32000
        elif i==14:
            money=10000000
    else:
        print("Sorry, Wrong Answer!")
        break

print(f"Hey User, Your total take home money is: {money}")

