from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

# ---------------- TAG_NAME ----------------
# Find all <a> links on the main page
links = driver.find_elements(By.TAG_NAME, "a")

print("\nAll links:")
for item in links:
    print(item.text)
time.sleep(2)

# ---------------- LINK_TEXT ----------------
link = driver.find_element(By.LINK_TEXT, "Form Authentication")
print("Link:", link.text)

# Click Form Authentication
link.click()
time.sleep(2)

# ---------------- ID ----------------
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
time.sleep(1)

# ---------------- NAME ----------------
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
time.sleep(1)

# ---------------- CLASS_NAME ----------------
login_button = driver.find_element(By.CLASS_NAME, "radius")
print("\nButton:", login_button.text)
login_button.click()
time.sleep(1)

logout_button = driver.find_element(By.CLASS_NAME, "button")    #button secondary radius there are three classes use only any one from them.
print("\nButton:", logout_button.text)
logout_button.click()
time.sleep(1)

time.sleep(2)

driver.quit()