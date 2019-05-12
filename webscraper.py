# webscraper

from bs4 import BeautifulSoup
import requests
import time

startTime = time.time()
url =  "https://finviz.com/screener.ashx?v=111&f=cap_midover,ta_pattern_wedgedown,ta_sma20_cross50a,ta_sma200_pa&ft=4"

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
endTime = time.time()

print("Run Time", endTime - startTime)