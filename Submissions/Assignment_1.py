""" Assignment 1 - Web Element Identification:
Identify and locate different web elements on a given webpage using 
By.ID, By.NAME, By. TAG NAME, By. LINK TEXT, and By.CLASS NAME."""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open the Chrome browser
driver = webdriver.Chrome()

# Open the website
driver.get("https://testautomationpractice.blogspot.com/")

#Maximize the browser window
driver.maximize_window()

time.sleep(5)
    

# By.ID
name = driver.find_element(By.ID, "name")
name.send_keys("Srishti")
print("1. Element located using ID")

# By.NAME
gender = driver.find_elements(By.NAME, "gender")
gender[1].click()
print("2. Female button selected using NAME")

# By.TAG_NAME
input_element = driver.find_element(By.TAG_NAME, "input")
print("3. Element located using TAG_NAME")

# By. LINK_TEXT
time.sleep(2)
apple = driver.find_element(By.LINK_TEXT, "Apple")
apple.click()
time.sleep(5)
print("4. Element located using LINK_TEXT")

# By. CLASS_NAME
element = driver.find_element(By.CLASS_NAME, "form-control")
element.send_keys("testing class")
time.sleep(5)
