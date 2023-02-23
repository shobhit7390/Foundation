# File I/O in Python

# Reading a file

f=open('myfile.txt','r')

text=f.read()
print(text)
f.close()

# Writing a file

f=open('myfile.txt','w')
f.write("Hello ! Welcome again")
f.close()

# Appending in a file

f=open('myfile.txt','a')
f.write("--Python--")
f.close()


with open('myfile.txt','a') as f:           # This 'with' keyword opens and closes the file by itself
    f.write("Hii")