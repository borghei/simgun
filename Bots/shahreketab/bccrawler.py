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

book_isbn = soup.find("span", {"itemprop": "isbn"})
book_title = soup.find("span", {"itemprop": "name"})
book_author = soup.find("span", {"itemprop": "author"})
book_pagecount = soup.find("span", {"itemprop": "numberOfPages"})
book_publisher = soup.find("span", {"itemprop": "publisher"})
book_price = soup.find("span", {"itemprop": "price"})

#book_pic = soup.find("span", {"itemprop": "isbn"})
#book_translator = soup.find("span", {"itemprop": "isbn"})
book_description = soup.find_all("div", {"style": "text-align: justify;"})
#book_category = soup.find("span", {"itemprop": "isbn"})

print(book_isbn)
print(book_price)
print(book_pagecount)
print(book_publisher)
print(book_title)
print(book_author)
for item in book_description:
    print(item.text)

