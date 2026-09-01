#CHILD NODES USING CSS

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

try:
    search_container=driver.find_element(By.CSS_SELECTOR, "div > textarea")
    footer_element=driver.find_element(By.CSS_SELECTOR, "div > a")

    print("Assignment 4 completed successfully.")
except Exception as e:
    print(f"Assignment 4 Error: {e}")
finally:
    time.sleep(2)
    driver.quit()