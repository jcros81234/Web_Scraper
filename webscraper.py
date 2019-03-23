#webscraper
from selenium import webdriver
from bs4 import BeautifulSoup
import requests



#grabs page
url =  "https://google.com"
browser = webdriver.Firefox()
browser.get(url)

# import time
# time.sleep(10)

# html = browser.page_source

# #xml parsing
# soup = BeautifulSoup(html, 'html.parser')


# #finds all ticker 
# ticker = soup.find_all('td', class_='screener-body-table-nw')

# print(ticker)
