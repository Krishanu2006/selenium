from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

child_elements = driver.find_elements(
    By.CSS_SELECTOR,
    "div > a"
)

print("Number of child link elements found:", len(child_elements))

for element in child_elements:
    if element.text.strip():
        print("Child element text:", element.text)

time.sleep(3)

driver.quit()