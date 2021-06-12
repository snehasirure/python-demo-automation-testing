from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path="C:\\data\webdrivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

username = driver.find_element_by_id('user-name')
username.send_keys('standard_user')

password = driver.find_element_by_id('password')
password.send_keys('secret_sauce')

login_button = driver.find_element_by_id('login-button')
login_button.submit()

time.sleep(2)

current_page = driver.current_url

assert current_page == "https://www.saucedemo.com/inventory.html", "Expected page is incorrect"

#to refresh the browser
#driver.refresh()
#to close the browser
driver.close()