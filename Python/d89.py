# requests module in python

# Requests library is one of the integral part of Python for making HTTP requests to a specified URL. Whether it be REST APIs or Web Scraping, requests is must to be learned for proceeding further with these technologies. When one makes a request to a URI, it returns a response. Python requests provides inbuilt functionalities for managing both the request and response.


import requests
from bs4 import BeautifulSoup

url="https://www.google.com"
r=requests.get(url)

# print(r.text)

soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

for heading in soup.find_all("h2"):
    print(heading.text)

