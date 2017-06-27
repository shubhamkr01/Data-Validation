import requests
r = requests.get(url)
if( r.url !=url):
  print('redirected')
else:
  print('not redirected')
  
