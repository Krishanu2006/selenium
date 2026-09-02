from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/challenging_dom")

driver.maximize_window()

# CSS selector - locate buttons
buttons = driver.find_elements(By.CSS_SELECTOR, "a.button")

print("Number of buttons:", len(buttons))

for button in buttons:
    print("Button text:", button.text)

# CSS selector - locate table rows
rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

print("\nNumber of rows:", len(rows))

for row in rows:
    print(row.text)

time.sleep(2)

driver.quit()