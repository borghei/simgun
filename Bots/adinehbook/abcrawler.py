__author__ = 'Shervin manzuri'
from bs4 import BeautifulSoup
import requests
import json
import os
import urllib.robotparser
from urllib.parse import urldefrag, urljoin, urlparse
from collections import deque

"""
read the web page, create a DOM of the page, and extract a
list of the targets of all links on the page
"""

def recursive_crawl(startpage, robotstexturl, maxpages=200, singledomain=False):

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstexturl)
    rp.read()

    information = {}
    pagequeue = deque()
    pagequeue.append(startpage)
    crawled = []
    domain = urlparse(startpage).netloc if singledomain else None

    pages = 0

    sess = requests.session()
    while pages < maxpages and pagequeue:
        url = pagequeue.popleft()

        if not rp.can_fetch("*", url):
            print('lol')
            continue

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
    info['author'] = soup.find("meta", {"property": "book:author"})['content'].translate({ord(c): None for c in '~'})
    info['page_count'] = soup.find("b", text = "تعداد صفحه:").next_sibling.translate({ord(c): None for c in ' '})
    info['publisher'] = soup.find("b", text="نشر:").next_sibling
    info['price'] = soup.find("b", {"class": "price"}).text
    info['description'] = soup.find("meta", {"name": "description"})['content'].translate({ord(c): None for c in '-1234567890~'})

    image_source = soup.find("meta", {"property": "og:image"})['content']
    info['pic'] = os.path.join(image_source_path,str(info['isbn'])+".jpg")
    with open(info['pic'], "wb") as file:
        response = requests.get(image_source)
        file.write(response.content)

    json_path = os.path.join(json_source_path,str(info['isbn'])+".json")
    save_to_json(info, json_path)

    return info


def save_to_json(info, path):
    with open(path, 'w') as fp:
        json.dump(info, fp)
    return

recursive_crawl("http://www.adinehbook.com", "http://www.adinehbook.com/robots.txt", 100)
# recursive_crawl("http://www.adinehbook.com/gp/product/9643124797/",1)
