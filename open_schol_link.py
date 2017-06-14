
from selenium import webdriver
import time

redirect = []

def open_schol_link():
	browser=webdriver.Chrome()
	for i in range(len(urls)):
		if(i!=0  and urls[i]!=''):
			browser.get(urls[i])
			
			#appending '1' for the redirecting urls to a list called redirect & '0' otherwise
			if(browser.current_url!=urls[i]):
				redirect.append('1')
			else:
				redirect.append('0')
