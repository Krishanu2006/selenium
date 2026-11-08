'''
Assignment 3: CSS Selector Challenge -> Locate web elements using CSS Selectors,
including selectors with wildcards for elements having varying or dynamic attribute values.
Example: Use a CSS wildcard selector to locate elements whose ID starts with user_.

[id^='user']   /* starts with user */
[id$='name']   /* ends with name */
[id*='user']   /* contains user */

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()

time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "#username")
print("Username found:", username.is_displayed())

password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
print("Password found:", password.is_displayed())

user_element = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
print("Wildcard element found:", user_element.is_displayed())

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print("Login button found:", login_button.is_displayed())
time.sleep(2)

driver.quit()