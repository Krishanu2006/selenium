'''
Assignment 2: Multiple Element Identification -> Identify multiple elements of the same type
on a webpage and use Selenium to find and work with the list of elements.
Example: Find all links on a webpage and print their text.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")
print("Total number of links:", len(links))
for link in links:
    print(link.text)
time.sleep(2)

driver.quit()