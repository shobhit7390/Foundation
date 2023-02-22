# WAP to translate a message into a secret code language .Use below rules

# Coding:

# If word contains atleast 3 chars ,remove first letter and append it to the last of each word
# Now append 3 random chars at the starting and at the end
# else:
#   Simply reverse the string

# Decoding:

# If the word contains leass than 3 chars, reverse the string
# else:
#   Remove 3 random chars from starting and end,now remove the last letter and append it to the starting

# ***Your program should ask whether to code or decode***


#----------- Solution--------------

import random
import string

def ran_str(n):
    res=''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase,k=n))
    return res

coding=int(input("Press 1 to code and 0 to decode:"))
st=input("Enter message:")
words=st.split(" ")

if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1=ran_str(3)
            r2=ran_str(3)
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))




