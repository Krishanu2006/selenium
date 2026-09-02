from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Wait after opening the website
time.sleep(5)

# ID
element = driver.find_element(By.ID, "name")
element.send_keys("Sayan")
time.sleep(5)

# NAME
element = driver.find_element(By.NAME, "email")
element.send_keys("test@example.com")
time.sleep(5)

# TAG NAME
element = driver.find_element(By.TAG_NAME, "textarea")
element.send_keys("This is my assignment.")
time.sleep(5)

# LINK TEXT
element = driver.find_element(By.LINK_TEXT, "Home")
element.click()
time.sleep(5)

# Wait before closing
time.sleep(10)

# Automatically close browser
driver.quit()