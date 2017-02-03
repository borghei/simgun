__author__ = 'Shervin manzuri'
from bs4 import BeautifulSoup
import requests
import json
import os
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

        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
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
    links = [a.attrs.get('href') for a in soup.select('a[href]')]
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
    image_source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    json_source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

    try:
        info['isbn'] = soup.find("meta", {"property": "book:isbn"})['content'].translate({ord(c): None for c in '-'})
        print(info['isbn'])
    except:
        return

    info['title'] = soup.find("meta", {"property": "og:title"})['content']
    print(info['title'])
    info['author'] = soup.find("meta", {"property": "book:author"})['content'].translate({ord(c): None for c in '~'})
    print(info['author'])
    # info['description'] = [x.text for x in soup.find_all("div", {"style": "text-align: justify;"})][2::]
    # info['page_count'] = soup.find("span", {"itemprop": "numberOfPages"}).text
    # info['publisher'] = soup.find("span", {"itemprop": "publisher"}).text
    # info['price'] = soup.find("span", {"itemprop": "price"}).text
    # info['category'] = soup.find("label", text = "دسته‌بندی").next_sibling[3:]

    image_source = soup.find("meta", {"property": "og:image"})['content']
    info['pic'] = os.path.join(image_source_path,str(info['isbn'])+".jpg")
    # with open(info['pic'], "wb") as file:
    #     response = requests.get(image_source)
    #     file.write(response.content)

    try:
        book_translator = soup.find("labehttp://www.adinehbook.com/gp/product/9643124797/ref=tbs_img_1000_6/891-4163377-8102068l", text = "\n            مترجم            :").parent.find("strong").text
        info['translator'] = book_translator
    except AttributeError:
        info['translator'] = ''

    # json_path = os.path.join(json_source_path,str(info['isbn'])+".json")
    # save_to_json(info, json_path)

    return info


def save_to_json(info, path):
    with open(path, 'w') as fp:
        json.dump(info, fp)
    return

recursive_crawl("http://www.adinehbook.com/gp/product/9643124797/ref=tbs_img_1000_6/891-4163377-8102068",20)
