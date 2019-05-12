# webscraper
#demos

from bs4 import BeautifulSoup
import requests
import time

url =  "https://finviz.com/screener.ashx?v=112&f=sh_price_o5,ta_perf_1wup&ft=3&o=company"

hasNextPage = True
firstPage = True
currentPageIndex = 0
charIndex = 0

while hasNextPage:
	if not firstPage:
		url += "&r=" + str(currentPageIndex)
		charIndex = -3 - len(str(currentPageIndex))
	# grabs page
	page = requests.get(url).text
	print url

	# parser
	soup = BeautifulSoup(page,'html.parser')

	# finds all ticker and prints
	counter = 0
	for el in soup.find_all('a', class_='screener-link-primary'):
		counter += 1
		print el.get_text()

	#resets url to original state if past first page
	if not firstPage:
		url = url[:charIndex]

	# toggle flag such that firstPage will be false after first run
	firstPage = False

    # advance to next page url
	if currentPageIndex == 0:
		currentPageIndex += 21
	else:
		currentPageIndex += 20
    # 20 is number of stocks per page
    # Less than 20 means final page

	if counter < 20:
		hasNextPage = False

	#wait 5 seconds before making next request
	time.sleep(5)
