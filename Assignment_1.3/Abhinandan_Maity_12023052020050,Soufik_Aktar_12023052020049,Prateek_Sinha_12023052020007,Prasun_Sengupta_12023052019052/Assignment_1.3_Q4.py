from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

driver.maximize_window()

# Parent div
parent = driver.find_element(By.CSS_SELECTOR, "div.example")

print("Parent found:", parent.tag_name)

# Child button inside the parent
add_button = parent.find_element(
    By.CSS_SELECTOR,
    "button"
)

print("Button text:", add_button.text)

# Click Add Element
add_button.click()

time.sleep(1)

# Locate Delete button
delete_button = parent.find_element(
    By.CSS_SELECTOR,
    "button.added-manually"
)

print("Delete button:", delete_button.text)

# Click Delete
delete_button.click()

time.sleep(2)

driver.quit()