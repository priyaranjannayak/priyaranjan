from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("C:\\Users\HP\PycharmProjects\selenium project\driver\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("selenium")
act=ActionChains(driver)
act.send_keys(Keys.ENTER).perform()
driver.get("http://facebook.com")
driver.maximize_window()
driver.find_element_by_name("email").send_keys("9348542303")
driver.find_element_by_name("pass").send_keys("prn006")
act.send_keys(Keys.ENTER).perform()

driver.quit(1)




