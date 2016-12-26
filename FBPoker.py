#Facebook Poker 2016 UPDATE!
#Lomar Lilly
#USE AT YOUR OWN RISK
#MIGHT NOT WORK 100% ON WINDOWS MACHINES!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, getpass, os

banner="""
 _____              _                 _      ____       _             
|  ___|_ _  ___ ___| |__   ___   ___ | | __ |  _ \ ___ | | _____ _ __  
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ / | |_) / _ \| |/ / _ \ '__| 
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <  |  __/ (_) |   <  __/ |    
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ |_|   \___/|_|\_\___|_| v1.0
"""

browser = webdriver.PhantomJS()
browser.set_window_size(1024, 768)

def poke():
	browser.get("https://www.facebook.com/pokes")
	time.sleep(1)
	print("[+] Login Sucessful!")
	time.sleep(1)
	try:
		os.system("clear")
	except:
		os.system("cls")
	
	print (banner)
	while True:
		try:
			a = browser.find_elements_by_xpath("""//*[@class="_42ft _4jy0 _4jy3 _4jy1 selected _51sy"]""")
			for i in range(0,len(a)):
				pokeback = a[i].text
				if pokeback == "Poke Back":
					a[i].click()	
					try:
						os.system("clear")
					except:
						os.system("cls")
					print(banner)
					print("\n\n[+] Pokes Sent")	
					time.sleep(5)
				else:
					try:
						os.system("clear")
					except:
						os.system("cls")
					print(banner)
					print("\n\n[..] waiting on someone to poke back")
					break
		except:
			pass

def login(user,pwd):
	browser.get("https://www.facebook.com/")
	try:
		browser.find_element_by_id("email").send_keys(user + Keys.TAB)
		browser.find_element_by_id("pass").send_keys(pwd + Keys.RETURN)
		time.sleep(1)
		if browser.current_url == """https://www.facebook.com/login.php?login_attempt=1&lwv=110""":
			print("[-] Invalid Username or Password!")
			time.sleep(3)
			try:
				os.system("clear")
			except:
				os.system("cls")
			main()
		else:
			poke()
			
	except Exception:
		print("Phantomjs Not found!")
		time.sleep(10)

def main():
	try:
		os.system("clear")
	except:
		os.system("cls")
	print(banner)
	user = input("Username: ")
	pwd = getpass.getpass("Password: ")
	data=login(user,pwd)

if __name__=="__main__":
	main() 
