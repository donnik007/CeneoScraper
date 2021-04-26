import requests
from bs4 import BeautifulSoup
import json

def extractComponent(opinion, selektor,attribute=None):
    try:
        if attribute:
            return opinion.select(selektor).pop(0)[attribute].strip()
        if attribute is None:
            return opinion.select(selektor).pop(0).get_text().strip()
        return [item.get_text().strip() for item in opinion.select(selektor)]
    except IndexError:
        return None
    
components = {
            "author":["span.user-post__author-name"],
            "rcmd":["span.user-post__author-recomendation > em"],
            "stars":["span.user-post__score-count"],
            "content":["div.user-post__text"],
            "pros":["div[class*=\"positives\"] ~ div.review-feature__item",False],
            "cons":["div[class*=\"negatives\"] ~ div.review-feature__item",False],
            "purchased":["div.review-pz"],
            "publishDate":["span.user-post__published > time:nth-child(1)","datetime"],
            "purchaseDate":["span.user-post__published > time:nth-child(2)","datetime"],
            "useful":["span[id^=\"votes-yes\"]"],
            "useless":["span[id^=\"votes-no\"]"],
        }

print(11488356)
print(96270890)
print(97065427)
productId = input("Podaj kod produktu: ")
response = requests.get("https://www.ceneo.pl/{}#tab=reviews".format(productId))
page = 2
opinionsList = []

while response:
    pageDOM = BeautifulSoup(response.text, 'html.parser')
    opinions = pageDOM.select("div.js_product-review")

    for opinion in opinions:
        opinionDict = {key:extractComponent(opinion, *value) for key, value in components.items()}
        opinionDict["opinionId"] = opinion["data-entry-id"]

        opinionsList.append(opinionDict)

    response = requests.get("https://www.ceneo.pl/{}/opinie-".format(productId)+str(page), allow_redirects=False)
    if response.status_code == 200:
        page += 1
    else:
        break
        
with open(f"./opinions/{productId}.json", "w", encoding="UTF-8") as f:
    json.dump(opinionsList, f, indent = 4, ensure_ascii=False)

