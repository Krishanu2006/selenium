from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

links = driver.find_elements(By.TAG_NAME, "a")

print("Total number of links:", len(links))

for link in links:
    text = link.text.strip()

    if text:
        print(text)

time.sleep(3)

driver.quit()