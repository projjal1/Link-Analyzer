#Python script to analyze redirect links

import requests

get_link=input("Input link: ")

res=requests.get(get_link)

responses=res.history

print("Redirected through following links:")

for each in responses:
    print(each.url, each)


