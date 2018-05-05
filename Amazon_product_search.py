import urllib2
from bs4 import BeautifulSoup as soup


def product_search(name):
	
	pgno = 1
	name = name.replace(' ', '_')
	filename = name + '.csv'
	f = open(filename, 'w')
	headers = 'Brand' + ',' + 'Amazon Price\n' 
	f.write(headers)

	while pgno < 4:
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		url = 'http://www.amazon.in/s/page=' + str(pgno) + '&keywords=' + name
		response = opener.open(url).read()
		page_html = soup(response, "html.parser")
		container = page_html.findAll("div", {"class":"s-item-container"})
	
		for item in container:
			try:
				item_contain = item.findAll("div", {"class":"a-row a-spacing-small"})
				final_product = item_contain[0].text.strip().encode('utf-8')
				final_cost = item.find("span", {"class":"a-size-base a-color-price s-price a-text-bold"}).text.encode('utf-8')
				print final_product.replace(',', '|').strip() + ',' + final_cost.replace(',','')
				f.write(final_product.replace(',', '|').strip() + ',' + final_cost.replace(',','') + ',' + '\n')
			except IndexError:
				print "No Data"
		pgno += 1
	f.close()

''' Call function by passing the product you want to search '''

product_search('Mens Puma Shoes')