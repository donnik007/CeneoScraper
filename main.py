import requests

response = requests.get("https://www.ceneo.pl/11488356#tab=reviews")
print(response.text)