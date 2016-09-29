from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import time
from password import pswd

caps = DesiredCapabilities.FIREFOX


caps["marionette"] = True




caps["binary"] = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
driver = webdriver.Firefox(capabilities=caps)
driver.get('https://www.eventbrite.com/e/msu-small-business-expo-registration-27016931369?aff=es2')
time.sleep(2)

driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/section/div[1]/div/div/div[2]/dl/dd[1]/time/p[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section[2]/div/div/section/div/ul/li[2]/a/div/p').click()
time.sleep(2)
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
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
for handle in driver.window_handles:
    driver.switch_to_window(handle)
driver.get('https://www.eventbrite.com/e/business-plan-workshop-tickets-27488633242?aff=es2')
time.sleep(2)

driver.find_element_by_xpath('/html/body/main/div[1]/div[2]/div/section/div[1]/div/div/div[2]/dl/dd[1]/time/p[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/section[2]/div/div/section/div/ul/li[2]/a/div/p').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[4]/div[3]/div[1]/div/div/div[1]/div[3]/div/div/div/div/div[2]').click()
