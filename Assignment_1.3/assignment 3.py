from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open webpage
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()

# -----------------------------------------
# 1. ID starts with 's' (e.g. sunday, saturday, start-date)
# CSS selector: ^=
# -----------------------------------------

elements = driver.find_elements(
    By.CSS_SELECTOR, "[id^='s']"
)

print("Elements whose ID starts with 's':")

for element in elements:
    tag = element.tag_name
    eid = element.get_attribute("id")
    print(f"  Tag: {tag}, ID: {eid}")

# Close browser
driver.quit()