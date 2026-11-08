'''
Assignment 4: Child Nodes Using CSS -> Identify and locate child/nested web elements
using CSS child selectors and interact with the required elements.
Example: Locate a button inside a specific div using a CSS child selector.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(2)

login_form = driver.find_element(By.CSS_SELECTOR, "form#login")
login_button = login_form.find_element(By.CSS_SELECTOR, "button")
print("Login button found:", login_button.is_displayed())
login_button.click()
time.sleep(2)
driver.quit()