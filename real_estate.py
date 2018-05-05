from bs4 import BeautifulSoup as soup
import requests, lxml, re
import urllib2

f = open('2BHK_Property_Price.csv', 'w')
headers = 'No. of Rooms' + '|' + 'Location' + '|' + 'Price\n' 
f.write(headers)


opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2&cityName=Bangalore'
html_file = opener.open(url).read()
content = soup(html_file, 'html.parser')

title = content.findAll('div',{'class':'flex relative clearfix m-srp-card__container'})
for item in title:
	try:
		Loc = item.find('a').text.replace("\n",' ').strip().replace('  ',' ').title().encode('utf-8').split('For Sale In')
		price = item.find('div',{'class':'m-srp-card__price'}).text.encode('utf-8')	
		print '|'.join(Loc)+'|'+price
		f.write('|'.join(Loc)+'|'+price+'\n')
	except AttributeError:
		price='No Data'

f.close()