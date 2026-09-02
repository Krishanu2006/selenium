#Assignment 1: Web Element Identification -> Identify and locate different web elements on a 
#given webpage using By.ID, By.NAME, By.TAG_NAME, By.LINK_TEXT, and By.CLASS_NAME.
# https://www.selenium.dev/selenium/web/locators_tests/locators.html

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")

# ID
last_name = driver.find_element(By.ID, "lname")
print("ID locator: Last Name found")

# NAME
newsletter = driver.find_element(By.NAME, "newsletter")
print("NAME locator: Newsletter found")

# TAG NAME
link = driver.find_element(By.TAG_NAME, "a")
print("TAG NAME locator: Link found")

# LINK TEXT
official_link = driver.find_element(By.LINK_TEXT, "Selenium Official Page")
print("LINK TEXT locator: Official link found")

# CLASS NAME
first_name = driver.find_element(By.CLASS_NAME, "information")
print("CLASS NAME locator: Element found")

time.sleep(5)  # Optional: Wait for 5 seconds to observe the results
driver.quit()