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


# =========================================================
# 1. TAG SELECTOR
# =========================================================

element = driver.find_element(By.CSS_SELECTOR, "input")

print("1. Tag selector: Element found")


# =========================================================
# 2. ID SELECTOR
# =========================================================

element = driver.find_element(By.CSS_SELECTOR, "#name")

print("2. ID selector: Element found")


# =========================================================
# 3. ATTRIBUTE SELECTOR
# =========================================================

element = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='text']"
)

print("3. Attribute selector: Element found")


element = driver.find_element(
    By.CSS_SELECTOR,
    "[id*='name']"
)

print("4. Wildcard selector: Element found")


# Keep browser open for screen recording
input("Press Enter to close the browser...")

# Close browser
driver.quit()