from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()

time.sleep(2)


button = driver.find_element(
    By.CSS_SELECTOR,
    "div.form-group > button"
)

print("1. Child element located successfully")

# Click the child button
button.click()

print("2. Child button clicked successfully")


# Keep browser open for screen recording
input("Press Enter to close the browser...")

# Close browser
driver.quit()
