__author__ = 'Shervin'
from bs4 import BeautifulSoup
import requests
import os

source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

url = "http://shahreketabonline.com/products/115/29771/%D8%B3%DB%8C%D9%84%D9%85%D8%A7%D8%B1%DB%8C%D9%84%DB%8C%D9%88%D9%86"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())

book_isbn = soup.find("span", {"itemprop": "isbn"}).text
book_title = soup.find("span", {"itemprop": "name"}).text
book_author = soup.find("span", {"itemprop": "author"}).text
book_pagecount = soup.find("span", {"itemprop": "numberOfPages"}).text
book_publisher = soup.find("span", {"itemprop": "publisher"}).text
book_price = soup.find("span", {"itemprop": "price"}).text
book_description = [x.text for x in soup.find_all("div", {"style": "text-align: justify;"})][2::]

image_source = soup.find("img", {"class": "full-image img-responsive"})['src']
book_pic_path = os.path.join(source_path,str(book_isbn)+".jpg")
with open(book_pic_path, "wb") as file:
    response = requests.get(image_source)
    file.write(response.content)

book_translator = soup.find("label", text = "\n            مترجم            :").parent.find("strong").text

print("translator")
print(book_translator)
#book_category = soup.find("span", {"itemprop": "isbn"})

print(image_source)
print(book_isbn)
print(book_price)
print(book_pagecount)
print(book_publisher)
print(book_title)
print(book_author)
print(book_description)
