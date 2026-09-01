#MULTIPLE ELEMENT IDENTIFICATION

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

try:
    links=driver.find_elements(By.TAG_NAME, "a")
    print(f"Total links found on Google: {len(links)}")

    for index, link in enumerate(links, start=1):
        text=link.text.strip()
        href=link.get_attribute("href")
        if text:
            print(f"Link {index}: Text='{text}', URL='{href}'")

    print("Assignment 2 completed successfully.")
except Exception as e:
    print(f"Assignment 2 Error: {e}")
finally:
    time.sleep(2)
    driver.quit()