from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib
import requests
import sys

matplotlib.use('Agg')
BITCOIN_STATISTIC_IN_LAST_10_MONTHS_URI = "https://www.in2013dollars.com/bitcoin-price"


def get_statistics(uri=BITCOIN_STATISTIC_IN_LAST_10_MONTHS_URI):
	res = requests.get(uri)
	if res.status_code != 200:
		sys.exit('\x1b[31m' + "Page not found" + '\x1b[0m')
	html_doc = res.content
	soup = BeautifulSoup(html_doc, 'html.parser')
	table = soup.find_all('table')[-1]
	rows = table.find_all('tr')[1:11] # this range of rows that cotain exactly the last 10 months statistic in descending state
	stats = []
	for row in rows:
		stats.append(row.find_all('td')[2].find(text=True))
	stats = [float(price.replace(',', '')) for price in stats]
	avg = sum(stats)/len(stats)
	avg = "%.2f" % avg
	x = [i for i in range(1,11)]
	y = stats[::-1]
	plt.scatter(x, y)
	plt.plot(x, y)
	plt.xlabel('month')
	plt.ylabel('price')
	plt.savefig('./static/bitcoin-stats.jpg')
	return avg


if __name__ == '__main__':
	avg = get_statistics()
	print(f'bitcoin price in last 10 months: {avg} $')
