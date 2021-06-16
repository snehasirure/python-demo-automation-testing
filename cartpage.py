from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome(executable_path="C:\\data\webdrivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

username_standard = driver.find_element_by_id('user-name')
username_standard.send_keys('standard_user')

password_standard = driver.find_element_by_id('password')
password_standard.send_keys('secret_sauce')

login_button = driver.find_element_by_id('login-button')
login_button.submit()

time.sleep(1)

driver.get("https://www.saucedemo.com/inventory.html")

current_page = driver.current_url

defaultproductsorting = driver.find_element_by_class_name('active_option')
assert defaultproductsorting.text == "NAME (A TO Z)"

time.sleep(1)

product_sorting = Select(driver.find_element_by_class_name('product_sort_container'))
product_sorting.select_by_value('lohi')

time.sleep(1)

#Test case for adding Sauce Labs Bike Light item in cart

driver.get("https://www.saucedemo.com/inventory.html")

current_page = driver.current_url

selectitem = driver.find_element_by_xpath("//div[contains(., 'Sauce Labs Bike Light') and @class='inventory_item']")
driver.find_element_by_id('add-to-cart-sauce-labs-bike-light').click()

time.sleep(2)

#to refresh the browser
#driver.refresh()

#to close the browser
driver.close()