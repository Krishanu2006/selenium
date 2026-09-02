from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open demo webpage
driver.get("https://the-internet.herokuapp.com/login")

# Maximize browser window
driver.maximize_window()
# 1. CSS Selector using ID

username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")

# 2. CSS Selector using Attribute
password = driver.find_element(
    By.CSS_SELECTOR,
    "input[type='password']"
)
password.send_keys("SuperSecretPassword!")

# 3. CSS Wildcard Selector
#    *= means: attribute contains this value

username_dynamic = driver.find_element(
    By.CSS_SELECTOR,
    "input[id*='user']"
)

print("Username element found:", username_dynamic.get_attribute("id"))

# 4. CSS Selector using ^= 
#    ^= means: attribute starts with this value


username_start = driver.find_element(
    By.CSS_SELECTOR,
    "input[id^='user']"
)

print("ID starts with 'user':", username_start.get_attribute("id"))

# 5. CSS Selector using $=
#    $= means: attribute ends with this value

password_end = driver.find_element(
    By.CSS_SELECTOR,
    "input[id$='word']"
)

print("ID ends with 'word':", password_end.get_attribute("id"))

# 6. Locate Login button
login_button = driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
)

login_button.click()

time.sleep(3)

print("Assignment 3 completed successfully.")

# Close browser
driver.quit()