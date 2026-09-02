from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()

# 1. Locate using ID
username = driver.find_element(By.ID, "username")
print("Username field:", username.get_attribute("id"))

# 2. Locate using NAME
password = driver.find_element(By.NAME, "password")
print("Password field:", password.get_attribute("name"))

# 3. Locate using TAG_NAME
heading = driver.find_element(By.TAG_NAME, "h2")
print("Heading:", heading.text)

# 4. Locate using LINK_TEXT
logout_link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
print("Link:", logout_link.text)

# 5. Locate using CLASS_NAME
login_button = driver.find_element(By.CLASS_NAME, "radius")
print("Button:", login_button.text)

# Enter values
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# Click Login
login_button.click()

time.sleep(2)

driver.quit()