from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome(executable_path="C:\\data\webdrivers\chromedriver.exe")

driver.maximize_window()

# Test Case 1 - Login with valid user
driver.get("https://www.saucedemo.com/")
time.sleep(1)

username_standard = driver.find_element_by_id('user-name')
username_standard.send_keys('standard_user')

password_standard = driver.find_element_by_id('password')
password_standard.send_keys('secret_sauce')

login_button = driver.find_element_by_id('login-button')
login_button.submit()

time.sleep(1)

current_page = driver.current_url

assert current_page == "https://www.saucedemo.com/inventory.html", "Expected page is incorrect"

# Test Case 2 - Login with locked out user
driver.get("https://www.saucedemo.com/")
time.sleep(1)

username_lockeduser = driver.find_element_by_id('user-name')
username_lockeduser.send_keys('locked_out_user')

password_lockeduser = driver.find_element_by_id('password')
password_lockeduser.send_keys('secret_sauce')

login_button = driver.find_element_by_id('login-button')
login_button.submit()

time.sleep(1)

current_page = driver.current_url
error_message = driver.find_element_by_class_name('error-message-container')
assert error_message.text == "Epic sadface: Sorry, this user has been locked out."
assert current_page == "https://www.saucedemo.com/", "Expected page is incorrect"

# Test Case 3 - Login with incorrect credentials
driver.get("https://www.saucedemo.com/")
time.sleep(1)

username_incorrectuser = driver.find_element_by_id('user-name')
username_incorrectuser.send_keys('sdfc_user')

password = driver.find_element_by_id('password')
password.send_keys('secret_sauce')

login_button = driver.find_element_by_id('login-button')
login_button.submit()

time.sleep(1)

current_page = driver.current_url
error_message = driver.find_element_by_class_name('error-message-container')
assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
assert current_page == "https://www.saucedemo.com/", "Expected page is incorrect"

#Test case 4 - Sorting items in low to high

driver.get("https://www.saucedemo.com/")
time.sleep(1)

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
print('text is = ' + defaultproductsorting.text)
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

time.sleep(3)

#to refresh the browser
#driver.refresh()
#to close the browser
driver.close()