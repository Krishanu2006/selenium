#CSS SELECTOR CHALLENGE

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

try:
    textarea_starts_with = driver.find_element(By.CSS_SELECTOR, "textarea[name^='q']")

    search_input_ends_with = driver.find_element(By.CSS_SELECTOR, "textarea[name$='q']")

    btn_contains_class = driver.find_element(By.CSS_SELECTOR, "input[type*='submit']")

    print("Assignment 3 completed successfully.")
except Exception as e:
    print(f"Assignment 3 error: {e}")
finally:
    time.sleep(2)
    driver.quit()