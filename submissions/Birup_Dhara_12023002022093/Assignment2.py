# Assignment 2: Multiple Element Identification -> Identify multiple elements of the same type
# on a webpage and use Selenium to find and work with the list of elements.
# Example: Find all links on a webpage and print their text.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.iana.org/help/example-domains")

# Find all links
links = driver.find_elements(By.TAG_NAME, "a")

# Print total number of links
print("Total links:", len(links))

# Print each link's text
for link in links:
    print(link.text)

driver.quit()