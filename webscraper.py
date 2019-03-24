#webscraper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests



#grabs page
url =  "https://finviz.com/screener.ashx?v=112&f=sh_price_o5,ta_perf_1wup&ft=3&o=company"
browser = webdriver.Firefox()
browser.get(url)


WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.XPATH,"//div [@class='gray4056']")))
elm = browser.find_element_by_class_name('screener-link-primary')
elm.click()


# import time
# time.sleep(10)

# html = browser.page_source

# #xml parsing
# soup = BeautifulSoup(html, 'html.parser')

# #finds all ticker 
# ticker = soup.find_all('td', class_='screener-body-table-nw')

# print(ticker)
