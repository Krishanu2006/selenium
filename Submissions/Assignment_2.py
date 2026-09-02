""" Assignment 2 - Multiple Element Identification: 
Identify multiple elements of the same type on a webpage and use Selenium to find and 
work with the list of elements. """

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")

print("Total number of links:", len(links))

# Print the text of each link
for link in links:
    print(link.text)

driver.quit()
