from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
url="https://codechef.com/users/deepakjnv880"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
# print(webpage)
soup=BeautifulSoup(webpage,'lxml')
deepak=soup.select('.rating-star')
# deepak=deepak.unicode('utf-8')
for i in deepak:
  print(i)
  # print("helolok")
# print(deepak)