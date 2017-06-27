import urllib.request
import urllib.parse
newurl='http://jvsbvirbvievb.com'
TypeError: 'module' object is not callable
req=urllib.request.Request(newurl) 
try:
	response=urllib.request.urlopen(req)
except:
	print('no')
