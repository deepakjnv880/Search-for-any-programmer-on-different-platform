#Used to make requests
import urllib.request
from urllib.request import Request, urlopen
# used to parse values into the url
import urllib.parse

import re


# url = 'https://www.google.com/search'
# values = {'q' : 'python programming tutorials'}

# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()

# print(respData)


# x = urllib.request.urlopen('https://codeforces.com/contests/1106')
x = Request('https://www.codechef.com/contests', headers={'User-Agent': 'Mozilla/5.0'})
print(x.read())




# deepka=re.findall(r'<span class="format-time" data-locale="en">(.*?)</span>',str(x.read()))
# # print(deepka)
# for i in deepka:
#   print(i)

# deepka=re.findall(r'<a (.*?)</a>',str(x.read()))
# print(deepka)
# for i in deepka:
#   print(i)

# notifies Python that you are opening this file, with the intention to write
# saveFile = open('exampleFile.txt','w')

# # actually writes the information
# saveFile.write((x.read()).decode("utf-8"))

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()