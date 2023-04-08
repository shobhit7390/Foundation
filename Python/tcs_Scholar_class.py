
'''

Create a class Scholar with attributes:
Scholarld-Number (representing a unique id for each student)
ScholarName - String (represents the name of the student)
State String (representing the state of the student)
Marks List (storing the marks of 3 subjects, obtained marks from each subject is out of 100)

Define the __init_method which takes parameters in the above sequence and sets the values for attributes.

Create another class ScholarResult with following attribute and methods

ScholarGrade list of dictionaries (It will contain the record for each student which will
have Scholarld, ScholarName, TotalMarks, Grade and State) 
Define the init_method which sets the values for above mentioned attribute.

Define the methods in the ScholarResult class as below

1. First method will take the list of Scholar objects and Grade as an input parameters.
Firstly, you need to calculate the percentage for each student (based on the marks obtained in 3 subjects).
To calculate the percentage use the following formula:
Percentage (Subject1 Marks + Subject2Marks + Subject3Marks)/3)
Note: Percentage must be an integer value and rounds the value. That means, if
Percentage >=40.0% or <40.5% then it will be considered as a 40% and
Percentage >=40.5% or <41% then it will be considered as a 41% 
After calculating the percentage you need to assign grades as per the following conditions:

If student's percentage >= 80 then assign Grade "A"
If student's percentage >= 60 and < 80 then assign Grade "B" If student's percentage >= 50 and < 60 then assign Grade "C"
If student's percentage <50 then assign Grade "D"
After calculating the grades, make a dictionary which contains Scholarld, ScholarName, TotalMarks, Grade and State and append it to the ScholarGrade (list of dictionaries) which is an attribute of ScholarResult class.

Secondly, your method will return the list of dictionaries according to the Grade passed as parameter. This list of dictionaries will be sorted based on their TotalMarks in descending order.

For Example:
[{'Scholarld: 106, 'Scholar Name': 'palak', 'TotalMarks': 282, 'Grade': 'A', 'State': 'gujarat'), ('Scholarld: 104, 'ScholarName': 'ramesh', 'TotalMarks': 275, 'Grade': 'A', 'State': 'rajasthan'),
'Scholarld: 102, 'ScholarName': 'ram', 'TotalMarks': 270, 'Grade': 'A', 'State': 'delhi'}] 
Assumption: No scholars would have same TotalMarks
Method should return None, in the following cases:
if search is unsuccessful
if no records are found, or
Grade is any other string apart from "A", " B " " C " or "D"

2. Second method will calculate the pass:fail ratio for each state and will return the list of states with pass:fail ratio. This list will be sorted in ascending order based on state's name.
For example: We have 2 states i.e. delhi and rajasthan. Output would be delhi first and then rajasthan.
A student who has acquired either Grade "A", "B" or "C" will be considered as a Pass and a student with Grade "D" will be considered as a Fail.
Formula to calculate the Passing and Failing Percentage:
PassingPercentage (Number of Scholars Passed/Total Scholars)* 100) FailingPercentage (Number of Scholars Failed / Total Scholars)* 100) = Note: Percentage must be an integer value and rounds the value. That means, if Percentage >=40.0% or <40.5% then it will be considered as a 40% and,
if percentage >=40.5% or <=41.0% then it will be considered as a 41%.
For Example-
Your returning list must follow the format as per the below sample example:
[['delhi', '60:40'], ['gujarat', '100:0'], ['rajasthan', '70:30']] If no records are found then method should return None.

Instructions to write main section of the code:
1. You would require to write the main section completely, hence please follow the below instructions for the same.
2. You would be required to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence. 3. Create the respective objects(Scholar and ScholarResult) with the given sequence of arguments to fulfill the __init__ method requirement defined in the respective classes referring to the below instructions.
i. Create a list of Scholar Objects.
3.To create the list of objects:
a. Read the count of Scholar objects you want to create.
b. Create a Scholar object after reading the data related to it and add the object to the list of Scholar objects which will be provided to the ScholarResult object. This point repeats for the number of Scholar objects (considered in the first line of input, point #3.i.a).
4. Read the Grade as an input from the user.
5. Call the first method which has a list of Scholar's objects and Grade (either "A", "B",
"C" or "D") as the arguments and return the list of dictionaries as required.

Format of the output would be:

"Scholarld ScholarName TotalMarks Grade State" (excluding the quotes).
If the first method is returning None, then display "No Record Found" (excluding the quotes).
For more clarity please refer the sample testcase.
6. Call the second method which will return a list of states with pass:fail ratio.
Format of the output would be:
"State PassingPercentage:FailingPercentage" (excluding the quotes).
If the second method is returning None, then display "No Record Found" (excluding the quotes).
For more clarity please refer the sample testcase.
Note: All the inputs and searches will be case insensitive. Display State and ScholarName in the lowercase.


You can consider below sample input and output to verify your implementation before submitting.
Sample Input1:

5
101
Tanmay
delhi
90
88
93
102
Sunil
delhi
90
95
90
103
Karvi
maharashtra
70
45
50
104
monika
tamilnadu
20
35
40
105
Ram
tamilnadu
90
65
50
a


Sample Output1:
102 sunil 275 A delhi
101 tanmay 271 A delhi
delhi 100:0
maharashtra 100:0
tamilnadu 50:50

'''

class Scholar:
    def __init__(self,ScholarId,ScholarName,State,Marks):
        self.ScholarId=ScholarId
        self.ScholarName=ScholarName
        self.State=State
        self.Marks=Marks

class ScholarResult:
    def __init__(self):
        self.ScholarGrade=[]

    def calculate_grade(self,scholar_list,grade):
        key_list=['ScholarId','ScholarName','total_marks','grade','State']

        if len(scholar_list)>0:
            for i in scholar_list:
                assign_grade=''
                total_marks=sum(i.Marks)
                perc=int(round(total_marks/3,0))

                if perc>=80:
                    assign_grade='A'
                elif 60<=perc<80:
                    assign_grade='B'
                elif 40<=perc<60:
                    assign_grade='C'
                else:
                    assign_grade='D'
                
                stu_record_list=[i.ScholarId,i.ScholarName,total_marks,assign_grade,i.State]
                student_record=dict(zip(key_list,stu_record_list))
                self.ScholarGrade.append(student_record)

            find_scholar=[rec for rec in self.ScholarGrade if rec['grade']==grade]
            find_scholar=sorted(find_scholar,key=lambda x: (x['total_marks']),reverse=True)
            return find_scholar
            
        else:
            return None
        
    def calculate_ratio(self):
        if(len(self.ScholarGrade)==0):
            return None
        else:
            ans=[]
            states=list(set([each_record['State'] for each_record in self.ScholarGrade]))
            states.sort()

            for item in states:
                count_scholars=0
                count_fail=0
                for each_record in self.ScholarGrade:
                    if each_record['State']==item:
                        count_scholars+=1
                        if each_record['grade']=='D':
                            count_fail+=1

                fail_perc=int(round((count_fail/count_scholars)*100,0))
                count_pass=count_scholars-count_fail
                pass_perc=int(round((count_pass/count_scholars)*100,0))
                one_state_record=[item,f"{pass_perc}:{fail_perc}"]
                ans.append(one_state_record)
        return ans


n=int(input())
scholar_list=[]

for i in range(n):
    ScholarId=int(input())
    ScholarName=input()
    State=input().lower()
    m1=int(input())
    m2=int(input())
    m3=int(input())
    Marks=[m1,m2,m3]
    scholar_obj=Scholar(ScholarId,ScholarName,State,Marks)
    scholar_list.append(scholar_obj)


grade=input().upper()
o=ScholarResult()
ans1=o.calculate_grade(scholar_list,grade)

if ans1 is None or len(ans1)==0:
    print("No record Found")
else:
    for record in ans1:
        for k,v in record.items():
            print(v,end=" ")
        print()

ans2=o.calculate_ratio()

if ans2 is None:
    print("No record Found")
else:
    for record in ans2:
        for item in record:
            print(item,end=" ")
        print()




