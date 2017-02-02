__author__ = 'Shervin'
from bs4 import BeautifulSoup
import requests
import os

source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

def scrape_page(url):
    info = {}
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    book_isbn = soup.find("span", {"itemprop": "isbn"}).text
    book_title = soup.find("span", {"itemprop": "name"}).text
    book_author = soup.find("span", {"itemprop": "author"}).text
    book_pagecount = soup.find("span", {"itemprop": "numberOfPages"}).text
    book_publisher = soup.find("span", {"itemprop": "publisher"}).text
    book_price = soup.find("span", {"itemprop": "price"}).text
    book_description = [x.text for x in soup.find_all("div", {"style": "text-align: justify;"})][2::]
    book_category = soup.find("label", text = "دسته‌بندی").next_sibling[3:]

    info['isbn'] = book_isbn
    info['title'] = book_title
    info['author'] = book_author
    info['description'] = book_description
    info['page_count'] = book_pagecount
    info['publisher'] = book_publisher
    info['price'] = book_price
    info['category'] = book_category

    image_source = soup.find("img", {"class": "full-image img-responsive"})['src']
    book_pic_path = os.path.join(source_path,str(book_isbn)+".jpg")
    info['pic'] = book_pic_path
    with open(book_pic_path, "wb") as file:
        response = requests.get(image_source)
        file.write(response.content)

    try:
        book_translator = soup.find("label", text = "\n            مترجم            :").parent.find("strong").text
        info['translator'] = book_translator
    except:
        book_translator = None
    return info
