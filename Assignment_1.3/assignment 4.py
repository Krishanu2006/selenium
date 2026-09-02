from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Locate the Submit button using CSS child selectors
    button = driver.find_element(
        By.CSS_SELECTOR,
        "form > div.row > div.col-md-4.py-2 > button"
    )

    print("Button found:", button.text)

    # Interact with the button
    button.click()

    print("Button clicked successfully")

finally:
    driver.quit()