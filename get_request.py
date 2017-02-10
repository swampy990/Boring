import pprint
import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-sasha-gu10-led-spotlight-bar-4-light-ivory-brass/p2152091")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})

strPrice = element.text.strip()

jlewisPrice = float(strPrice[1:])


if jlewisPrice < 100:
    pprint.pprint( strPrice + ' is a deal')
else:
    pprint.pprint('Bandits!')



#  < span itemprop = "price" class ="now-price" > £80.00 < / span >


