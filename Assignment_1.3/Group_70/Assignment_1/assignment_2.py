#Assignment 2: Multiple Element Identification -> 
# Identify multiple elements of the same type on a webpage and use Selenium to find and work with the list of elements.
# "https://www.selenium.dev/"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links found:", len(links))

for link in links:
    print(link.text)

print("Multiple Element Identification completed successfully!")
time.sleep(3)  # Optional: Wait for 3 seconds to observe the results
driver.quit()
