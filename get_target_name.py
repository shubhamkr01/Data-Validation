import requests

import re

r=requests.get('http://www.uiw.edu/internationaladmissions/scholarships.html')


f='WeberEdge International Scholarship'
pattern=re.compile('(([A-Z]\w+\s)+Scholarship|([A-Z]\w+\s)+Award|([A-Z]\w+\s)+Waiver|([A-Z]\w+\s)+Fund|([A-Z]\w+\s)+Aid|([A-Z]\w+\s)+Grant|([A-Z]\w+\s)+Fellowship|([A-Z]\w+\s)+Assistantship'))
r=requests.get('http://www.weber.edu/issc/top/scholarship.html')
'''p=re.findall(pattern,r.text)
for i in p:
	if(i==f):
		print('correct')
		break;
	print('incorrect')'''

re.search(pattern,r.text).group(0)
