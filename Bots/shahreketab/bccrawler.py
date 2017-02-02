__author__ = 'Shervin'
from bs4 import BeautifulSoup
import requests

# url = "http://shahreketabonline.com"
# r = requests.get(url)
#
# soup = BeautifulSoup(r.content, "html.parser") #html content related to that specific request
# for link in soup.find_all("a"):
#     print(link.text, " ", link.get("href"))

url = "http://shahreketabonline.com/products/43/163698/%D8%B3%D9%81%D8%B1%D9%87_%D8%A2%D8%B1%D8%A7%DB%8C%DB%8C_%D9%85%DB%8C%D9%88%D9%87_%D8%A2%D8%B1%D8%A7%DB%8C%DB%8C_%D9%88_%D8%AA%D8%B2_%DB%8C%D9%86%D8%A7%D8%AA_%D9%BE%D8%A7%D9%86%DB%8C%D8%B0"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
g_data = soup.find_all("div", {"class":"book_large"})

print(g_data)

for item in g_data:
    for stuff in item.contents:
        try:
            print(len(stuff.find_all("label")))
        except AttributeError:
            print("")