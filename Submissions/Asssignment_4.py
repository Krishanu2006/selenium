from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    time.sleep(5)

    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "#section1 > button"
    )

    submit_button.click()

    print("Submit button was located and clicked.")

    time.sleep(5)

finally:
    driver.quit()
