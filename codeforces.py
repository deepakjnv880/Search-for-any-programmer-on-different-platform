import urllib.request
import simplejson as JSON
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def codeforces_web_scraping(username):
	base="http://codeforces.com/api/user.info?handles="
	profile=base+username
	request_url = urllib.request.urlopen(profile) 
	request=request_url.read().decode("utf-8")
	data=JSON.loads(request)
	# data.JSON()
	# JSON.parse(request_url);
	# print("deepak")
	# print(data['result'][0]['rating'])
	# for i in data['result'][0]:
	# 	print(i, data['result'][0][i])
	return data['result'][0]