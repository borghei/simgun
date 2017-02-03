__author__ = 'Shervin manzuri'
from bs4 import BeautifulSoup
import requests
import os
import re
from urllib.parse import urldefrag, urljoin, urlparse
from collections import deque

"""
read the web page, create a DOM of the page, and extract a
list of the targets of all links on the page
"""

def recursive_crawl(startpage, maxpages=200, singledomain=False):

    information = {}
    pagequeue = deque()
    pagequeue.append(startpage)
    crawled = []
    domain = urlparse(startpage).netloc if singledomain else None

    pages = 0

    sess = requests.session()
    while pages < maxpages and pagequeue:
        url = pagequeue.popleft()

        try:
            response = sess.get(url)
        except (requests.exceptions.MissingSchema,
                requests.exceptions.InvalidSchema):
            continue
        if not response.headers['content-type'].startswith('text/html'):
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        crawled.append(url)
        page_info = scrape_page(soup)

        if (page_info is not None):
            information[url] = page_info

        pages += 1
        if pagehandler(url, response):
            links = getlinks(url, domain, soup)
            for link in links:
                if not url_in_list(link, crawled) and not url_in_list(link, pagequeue):
                    pagequeue.append(link)

    return

"""
the below method is for bugfixing only
"""
def pagehandler(pageurl, pageresponse):
    print('Crawling:' + pageurl + ' ({0} bytes)'.format(len(pageresponse.text)))
    return True


def url_in_list(url, listobj):
    http_version = url.replace('https://', 'http://')
    https_version = url.replace('http://', 'https://')
    return (http_version in listobj) or (https_version in listobj)


def getlinks(pageurl, domain, soup):
    links = [a.attrs.get('href') for a in soup.select('a[href]') if hasNumbers(a.attrs.get('href'))]
    links = [urldefrag(link)[0] for link in links]
    links = [link for link in links if link]
    links = [link if bool(urlparse(link).netloc) else urljoin(pageurl, link) for link in links]

    if domain:
        links = [link for link in links if samedomain(urlparse(link).netloc, domain)]

    return links


def samedomain(netloc1, netloc2):
    domain1 = netloc1.lower()
    if '.' in domain1:
        domain1 = domain1.split('.')[-2] + '.' + domain1.split('.')[-1]

    domain2 = netloc2.lower()
    if '.' in domain2:
        domain2 = domain2.split('.')[-2] + '.' + domain2.split('.')[-1]

    return domain1 == domain2


def scrape_page(soup):
    info = {}
    source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

    try:
        info['isbn'] = soup.find("span", {"itemprop": "isbn"}).text
        print("BOOK FOUND!!!")
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


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

recursive_crawl("http://shahreketabonline.com/",100)