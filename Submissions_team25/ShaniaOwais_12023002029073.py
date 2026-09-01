# ASSIGNMENT 4
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

driver.maximize_window()

time.sleep(3)

section1 = driver.find_element(
    By.XPATH,
    "//h4[normalize-space()='Section 1']/.."
)
input_box = section1.find_element(
    By.CSS_SELECTOR,
    "input"
)

input_box.send_keys("Shania")

time.sleep(1)

submit_button = section1.find_element(
    By.CSS_SELECTOR,
    ":scope > button"
)
submit_button.click()

time.sleep(2)

print("Assignment 4 completed successfully!")
print("CSS Child Selector used: :scope > button")

time.sleep(2)

driver.quit()
