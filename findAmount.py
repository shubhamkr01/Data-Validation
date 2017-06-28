import re

import requests

r=requests.get('http://www.uiw.edu/internationaladmissions/scholarships.html')

signpattern=re.compile('[$]\d{1,1000},*\d{1,1000}')
amount=re.findall(signpattern,r.text)

#amount = ['$8,000']
