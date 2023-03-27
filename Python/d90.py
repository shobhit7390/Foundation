# News app in Python using requests module

import requests
import json 

query=input("What type of news you are interested in? : ")

url=f"https://newsapi.org/v2/everything?q={query}&from=2023-02-27&sortBy=publishedAt&apiKey=76aa2f1ffec64fdcb2b301572231ce7a"
r=requests.get(url)

news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------")

# print(news,type(news))

