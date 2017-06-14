
from selenium import webdriver
import time

def open_schol_link():
	browser=webdriver.Chrome()
	for i in range(len(urls)):
		if(i!=0  and urls[i]!=''):
			browser.get(urls[i])
