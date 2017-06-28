import requests
from bs4 import BeautifulSoup as bs
import re


r=requests.get(url)

bsObj=bs(r.text,'html.parser')
