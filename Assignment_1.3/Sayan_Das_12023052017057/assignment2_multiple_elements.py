from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Wait so you can record the website opening
time.sleep(5)

# Find all links
links = driver.find_elements(By.TAG_NAME, "a")

# Print total number of links
print("Total links:", len(links))

# Print each link text
for link in links:
    print(link.text)

time.sleep(8)

# Automatically close browser
driver.quit()