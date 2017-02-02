__author__ = 'Shervin'
from bs4 import BeautifulSoup
import requests

url = ""
r = requests.get(url)

soup = BeautifulSoup(r.content) #html content related to that specific request

soup.find_all("a") #find all tags of <a>

print(soup.prettify())