from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

driver.maximize_window()

# Find all links
links = driver.find_elements(By.TAG_NAME, "a")

print("Total number of links:", len(links))

# Print text of every link
for link in links:
    print(link.text)

time.sleep(2)

driver.quit()