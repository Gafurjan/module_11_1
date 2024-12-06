import requests
from Tools.i18n.makelocalealias import pprint

r = requests.get('https://api.github.com/events', stream=True) 
print(r.url)
print(r.headers)
print(r.content)
print(r.text)
print(r.json())
print(r.raw)
print(r.headers['Cache-Control'])