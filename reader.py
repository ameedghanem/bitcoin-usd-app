from bs4 import BeautifulSoup
import requests
import sys


BITCOIN_TO_USD_URI = "https://www.google.com/search?q=bitcoin+in+usd&ei=iUxoYYf5IcmSkwWVv7HQAg&ved=0ahUKEwjH4ffOm8rzAhVJyaQKHZVfDCoQ4dUDCA4&uact=5&oq=bitcoin+in+usd&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMggIABAWEAoQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsANKBQg6EgExSgQIQRgAUGpYamCMCGgAcAN4AIABpgGIAaYBkgEDMC4xmAEAoAEByAEIwAEB&sclient=gws-wiz"


def get_doc(uri=BITCOIN_TO_USD_URI):
	"""
	 It sends a get request to the gievne uri and returns the proper html file 
	"""
	res = requests.get(uri)
	if res.status_code != 200:
		sys.exit('\x1b[31m' + "Page not found" + '\x1b[0m')
	doc = res.content
	return doc


def get_bitcoin():
	"""
	It inspects the given html document and returns bitcoin price
	"""
	html_doc = get_doc()
	soup = BeautifulSoup(html_doc, 'html.parser')
	text = soup.select('div[class="BNeawe iBp4i AP7Wnd"]')[0] # searhing for this specific html element with the specified class attribute 
	price = text.string.split()[0]
	return price
	

if __name__ == '__main__':
	bitcoin_in_usd = get_bitcoin(html_doc)
	print(f'Bitcoin in USD: {bitcoin_in_usd}')