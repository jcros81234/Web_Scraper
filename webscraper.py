#webscraper

from bs4 import BeautifulSoup
import requests

url =  requests.get('https://www.finviz.com').text

soup = BeautifulSoup(url, 'lxml')

print(soup)
