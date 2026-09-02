from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com")

time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Add/Remove Elements")
print("Link:", link.text)

# Click Form Authentication
link.click()
time.sleep(2)

# Locate the button inside div.example using CSS child selector
add_button = driver.find_element(
    By.CSS_SELECTOR,
    "div.example > button"
)

print("Button:", add_button.text)

# Click the button
add_button.click()

time.sleep(3)

# Locate the dynamically created Delete button
delete_button = driver.find_element(
    By.CLASS_NAME,
    "added-manually"
)

print("Button:", delete_button.text)

# Click Delete
delete_button.click()

time.sleep(2)

driver.quit()