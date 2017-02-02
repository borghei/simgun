__author__ = 'Shervin'
from bs4 import BeautifulSoup
import requests

url = "http://shahreketabonline.com"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser") #html content related to that specific request
for link in soup.find_all("a"):
    print(link.text, " ", link.get("href"))

