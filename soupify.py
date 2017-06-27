import requests
from bs4 import BeautifulSoup as bs


r=requests.get(url)

bsObj=bs(r.text,'html.parser')
