from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("https://testautomationpractice.blogspot.com/")

    button = driver.find_element(
        By.CSS_SELECTOR,
        "div.dropdown > button"
    )

    print("Button:", button.text)

finally:
    driver.quit()