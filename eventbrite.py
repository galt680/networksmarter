from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import time
import requests
from password import pswd
import bs4


eventbrite = "https://www.eventbrite.com/d/md--baltimore/business--events/?crt=regular&sort=best"
eventbrite = "https://www.eventbrite.com/d/md--baltimore/business/?crt=regular&page=3&sort=best"
#open the firefox browser with selenium
caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
driver = webdriver.Firefox(capabilities=caps)

#get links from eventbrite business page
def get_links(site):
	page = requests.get(site)
	soup = bs4.BeautifulSoup(page.text,'lxml')
	event_cards = soup.find_all('div', { "class" : "list-card-v2 l-mar-top-2 js-d-poster" })
	##convert event_cards back into bs4 element
	soup = (bs4.BeautifulSoup(str(event_cards),"lxml"))
	counter = 0
	link_list = []
	for link in soup.find_all('a',href = True):
		if "http" in link['href']:
			counter+=1
			link_list.append(link['href'])
	print counter
	return link_list

	
# /html/body/div[131]/div[2]/div[4]/div[4]/div[2]/div/div[2]/a ///////THIS IS ANOTHER UNIQUE ONE I"LL TRY AND IGNORE FOR NOW
#https://www.eventbrite.com/e/baltimore-career-fair-november-3-2016-tickets-18946013035?aff=es2	
#another weird one
#http://www.eventbrite.com/e/cob-leadership-academy-fy17-registration-26899529216?aff=es2
	
type1 = {
	"add_to_calendar":"/html/body/main/div[1]/div[2]/div/section/div[1]/div/div/div[2]/dl/dd[1]/time/p[3]/a",
	"google_calendar":"/html/body/div[2]/div[2]/div/div/section[2]/div/div/section/div/ul/li[2]/a",

	}

type2 = {                    
	"add_to_calendar": "/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/a",
	"google_calendar":"/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/div[2]/div[2]/a",

		
}

type3 = {					
		"add_to_calendar":"/html/body/div[131]/div/div[4]/div[4]/div[2]/a",
		"google_calendar":"/html/body/div[131]/div/div[4]/div[4]/div[2]/div[2]/div[2]/a"
}		                  
	

	
	
	
	
	
links = get_links(eventbrite)
def link_analyze():
	for i in links:
		driver.get(i)
		try:
			driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/section/div[1]/div/div/div[2]/dl/dd[1]/time/p[3]/a').text
			print "Format 1",i
		except:
			try:
				driver.find_element_by_xpath('/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/a').text
				print "Format 2",i
			except:
				try:
					driver.find_element_by_xpath('/html/body/div[131]/div/div[4]/div[4]/div[2]/a').text
					print "Format 3", i
				except:
					print "error",i
# link_analyze()		

	
def type1_click():
	driver.find_element_by_xpath(type1["add_to_calendar"]).click()
	time.sleep(2)
	driver.find_element_by_xpath(type1["google_calendar"]).click()
	time.sleep(5)
	print i

def type2_click():
	driver.find_element_by_xpath(type2["add_to_calendar"]).click()
	time.sleep(2)
	driver.find_element_by_xpath(type2["google_calendar"]).click()
	time.sleep(5)
	print i
	
def type3_click():
	driver.find_element_by_xpath(type3["add_to_calendar"]).click()
	time.sleep(2)
	driver.find_element_by_xpath(type3["google_calendar"]).click()
	time.sleep(5)
	print i

def login():
	for handle in driver.window_handles:
		driver.switch_to_window(handle)
	time.sleep(2)
	username = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div/input[1]')
	username.send_keys('routmanapp')
	driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/input').click()
	time.sleep(3)
	password = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div/input[2]')
	password.send_keys(pswd)
	driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/input[1]').click()
	time.sleep(4)
	driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
	return True
	
	
logged_in = False
for i in links:
	driver.get(i)
	time.sleep(5)
	try:
		type1_click()
		if logged_in == False:
			print "loggin in 1"
			logged_in =login()
		else:
			print "logged in 1"
			driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
			print "clicked 1"
	except:
		try:
			
			type2_click()
			if logged_in == False:
				print "logging in 2 "
				logged_in =login()
			else:
				print "logged in 2"
				driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
				print "clicked 2"
		except:
			try:
				type3_click()
				if logged_in == False:
					print "logging in 3"
					logged_in =login()
				else:
					print "logged in 3"
					driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
					print "clicked 3"
			except Exception as e:
				print e
				print ""
				print i
			
		# if logged_in == False:
			# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section[2]/div/div/section/div/ul/li[2]/a/div/p').click()
			# time.sleep(2)
			# google stuff
			# for handle in driver.window_handles:
				# driver.switch_to_window(handle)
			# time.sleep(2)
			# username = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div/input[1]')
			# username.send_keys('routmanapp')
			# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/input').click()
			# time.sleep(3)
			# password = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div/input[2]')
			# password.send_keys(pswd)
			# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/input[1]').click()
			# time.sleep(4)
			# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
			# logged_in = True
		# for handle in driver.window_handles:
			# driver.switch_to_window(handle)
		# else:
			# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section[2]/div/div/section/div/ul/li[2]/a/div/p').click()
			# time.sleep(2)
			# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()

	# except:
		# pass
		# try:
			# driver.find_element_by_xpath('/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/a').click()
			# time.sleep(3)
			# driver.find_element_by_xpath('/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/div[2]/div[2]/a').click()
			# for handle in driver.window_handles:
				# driver.switch_to_window(handle)
			# time.sleep(2)
			# username = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div/input[1]')
			# username.send_keys('routmanapp')
			# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/input').click()
			# time.sleep(3)
			# password = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div/input[2]')
			# password.send_keys(pswd)
			# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/input[1]').click()
			# time.sleep(4)
			# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
			# logged_in = True
		# except:
			# try:
				# time.sleep(4)
				# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()	
			# except:
				# pass	
				# driver.find_element_by_xpath('/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/div[2]/div[2]/a').click()
				# time.sleep(2)
				# for handle in driver.window_handles:
					# driver.switch_to_window(handle)
				# time.sleep(2)
				# username = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div/input[1]')
				# username.send_keys('routmanapp')
				# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/input').click()
				# time.sleep(3)
				# password = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div/input[2]')
				# password.send_keys(pswd)
				# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/input[1]').click()
				# logged_in = True
			# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
			# for handle in driver.window_handles:
				# driver.switch_to_window(handle)
			# else:
				# pass
		# except:
			# try:
				# driver.find_element_by_xpath('/html/body/div[131]/div/div[4]/div[4]/div[2]/a').click()
				# time.sleep(1)
				# if logged_in == False:
					# driver.find_element_by_xpath('/html/body/div[131]/div[2]/div[4]/div[4]/div[2]/div[2]/div[2]/a').click()
					# time.sleep(2)
					# for handle in driver.window_handles:
						# driver.switch_to_window(handle)
					# time.sleep(2)
					# username = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div/input[1]')
					# username.send_keys('routmanapp')
					# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[1]/div/input').click()
					# time.sleep(3)
					# password = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div/input[2]')
					# password.send_keys(pswd)
					# driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/form/div[2]/div/input[1]').click()
					# logged_in = True
					# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
					# for handle in driver.window_handles:
						# driver.switch_to_window(handle)
				# print 3
			# except Exception as e:
				# print e

	# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
	# for handle in driver.window_handles:
		# driver.switch_to_window(handle)
	# driver.get('https://www.eventbrite.com/e/business-plan-workshop-tickets-27488633242?aff=es2')
	# time.sleep(2)

	# driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/section/div[1]/div/div/div[2]/dl/dd[1]/time/p[3]/a').click()
	# time.sleep(2)
	# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section[2]/div/div/section/div/ul/li[2]/a/div/p').click()
	# time.sleep(2)
	# driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
