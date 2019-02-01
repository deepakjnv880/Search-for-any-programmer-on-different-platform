from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def codechef_web_scraping(username):
	base="https://www.codechef.com/users/"
	profile=base+username
	# print(profile)
	req = Request(profile, headers={'User-Agent': 'Mozilla/5.0'})
	web_byte = urlopen(req).read()
	webpage = web_byte.decode('utf-8')
	# print(webpage)
	soup=BeautifulSoup(webpage,'lxml')
	deepak=soup.select('.user-details')
	# print(deepak[0].attrs['colour'])
	return deepak[0]
	# deepak=deepak.unicode('utf-8')
	# for i in deepak:
	# print(i)