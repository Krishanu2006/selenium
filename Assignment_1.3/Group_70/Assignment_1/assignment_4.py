from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Locate the parent form
form = driver.find_element(
    By.CSS_SELECTOR,
    "form#login"
)

# Locate child input elements
username = form.find_element(
    By.CSS_SELECTOR,
    "div:nth-of-type(1) > div > input"
)

username.send_keys("tomsmith")

password = form.find_element(
    By.CSS_SELECTOR,
    "div:nth-of-type(2) > div > input"
)

password.send_keys("SuperSecretPassword!")

# Locate the button inside the form
button = form.find_element(
    By.CSS_SELECTOR,
    "button"
)

button.click()

time.sleep(3)

print("Child elements located and interacted successfully.")

driver.quit()