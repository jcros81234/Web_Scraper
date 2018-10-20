#webscraper

from bs4 import BeautifulSoup
import requests

#grabs page
url =  requests.get('https://finviz.com/screener.ashx?v=111&f=sh_price_o5,ta_perf_1wup&ft=3&o=company').text

#xml parsing
soup = BeautifulSoup(url, 'lxml')

#finds all ticker 
ticker = soup.find_all('td', class_='screener-body-table-nw')

print(ticker)
