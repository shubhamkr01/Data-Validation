import requests

import re

r=requests.get('http://www.uiw.edu/internationaladmissions/scholarships.html')


f='WeberEdge International Scholarship'
pattern=re.compile('((([A-Z]\w+[(of)(-)(for)]?\s)+Scholarship([\s(of)(-)(for)]?\s[A-Z]\w+)?)|([A-Z]\w+\s)?Award([A-Z]\w+\s)?|([A-Z]\w+\s)+Waiver([A-Z]\w+\s)?|([A-Z]\w+\s)+Fund([A-Z]\w+\s)?|([A-Z]\w+\s)+Aid)')
r=requests.get('http://www.weber.edu/issc/top/scholarship.html')
'''p=re.findall(pattern,r.text)
for i in p:
	if(i==f):
		print('correct')
		break;
	print('incorrect')'''

re.search(pattern,r.text).group(0)
