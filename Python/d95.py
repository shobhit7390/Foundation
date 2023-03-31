# Regular expressions 

import re

pattern=r"[A-Z]jango"
text='Django is a Python-based web framework that allows you to quickly create efficient web applications. It is also called batteries included framework because Django provides built-in features for everything including Django Admin Interface, default database SQLlite3, etc. When you are building a website, you always need a similar Mjango set of components: a way to handle user authentication (signing up, signing in, signing out), a management panel for your website, forms, a way to upload files, etc. Django gives you ready-made Yjango components to use and that too for rapid development.'

# match=re.search(pattern,text)         # It tells the first occurence of the text
# print(match)

matches=re.finditer(pattern,text)

for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])



ptrn=r"[a-z]at"

txt="The cat and the bat is in the hat."

matches=re.findall(ptrn,txt)
print(matches)

new_text=re.sub(ptrn,"dog",txt)
print(new_text)


