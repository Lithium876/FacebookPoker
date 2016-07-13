#Facebook Poker 2016
#Lomar Lilly
#USE AT YOUR OWN RISK

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys

browser = webdriver.PhantomJS("C:\Program Files (x86)\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
browser.set_window_size(1024, 768)

def poke():
	browser.get("https://www.facebook.com/pokes")
	try:
		a = browser.find_elements_by_xpath("""//*[@class="_42ft _4jy0 _4jy3 _4jy1 selected _51sy"]""")
		for i in range(0,len(a)):
			pokeback = a[i].text
			if pokeback == "Poke Back":
				a[i].click()
			else:
				break
		poke()
	except:
		poke()

def login(user,pwd):
	browser.get("https://www.facebook.com/")
	browser.find_element_by_id("email").send_keys(user + Keys.TAB)
	browser.find_element_by_id("pass").send_keys(pwd + Keys.RETURN)
	time.sleep(1)
	poke()

def main(arg):
 if len(arg)<3:
  sys.exit("script should be called with your username and password")
 user=arg[1]
 pwd=arg[2]
 data=login(user,pwd)

if __name__=="__main__":
 main(sys.argv)
