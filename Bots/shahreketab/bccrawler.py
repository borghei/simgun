__author__ = 'Shervin manzuri'
from bs4 import BeautifulSoup
import requests
import os
from collections import deque

def recursive_crawl(start_url):
    response = requests.get(start_url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [a.attrs.get('href') for a in soup.select('a[href]')]
    return


def scrape_page(url):
    info = {}
    source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    try:
        info['isbn'] = soup.find("span", {"itemprop": "isbn"}).text
    except AttributeError:
        return

    info['title'] = soup.find("span", {"itemprop": "name"}).text
    info['author'] = soup.find("span", {"itemprop": "author"}).text
    info['description'] = [x.text for x in soup.find_all("div", {"style": "text-align: justify;"})][2::]
    info['page_count'] = soup.find("span", {"itemprop": "numberOfPages"}).text
    info['publisher'] = soup.find("span", {"itemprop": "publisher"}).text
    info['price'] = soup.find("span", {"itemprop": "price"}).text
    info['category'] = soup.find("label", text = "دسته‌بندی").next_sibling[3:]

    image_source = soup.find("img", {"class": "full-image img-responsive"})['src']
    info['pic'] = os.path.join(source_path,str(info['isbn'])+".jpg")
    with open(info['pic'], "wb") as file:
        response = requests.get(image_source)
        file.write(response.content)

    try:
        book_translator = soup.find("label", text = "\n            مترجم            :").parent.find("strong").text
        info['translator'] = book_translator
    except AttributeError:
        info['translator'] = ''

    return info