#WEB ELEMENT IDENTIFICATION

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Webdriver")

    gmail_link=driver.find_element(By.LINK_TEXT, "Gmail")

    images_link=driver.find_element(By.LINK_TEXT, "Images")

    body_tag=driver.find_element(By.TAG_NAME, "Body")

    search_button = driver.find_element(By.NAME, "btnK")

    print("Assignment 1 completed successfully.")
except Exception as e:
    print(f"Assignment 1 Error: {e}")
finally:
    time.sleep(2)
    driver.quit()