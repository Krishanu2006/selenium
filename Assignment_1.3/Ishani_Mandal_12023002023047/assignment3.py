from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

name_field = driver.find_element(By.CSS_SELECTOR, "#name")
print("Located using CSS ID selector:", name_field.tag_name)

name_field = driver.find_element(By.CSS_SELECTOR, "input[id='name']")
print("Located using CSS attribute selector:", name_field.tag_name)

dynamic_elements = driver.find_elements(By.CSS_SELECTOR, "[id^='input']")
print("Number of elements located using CSS wildcard selector:", len(dynamic_elements))

time.sleep(3)

driver.quit()