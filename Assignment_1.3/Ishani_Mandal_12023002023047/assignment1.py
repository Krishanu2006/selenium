from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)

element_id = driver.find_element(By.ID, "name")
print("Element located using ID:", element_id.tag_name)

element_name = driver.find_element(By.NAME, "gender")
print("Element located using NAME:", element_name.tag_name)

elements_tag = driver.find_elements(By.TAG_NAME, "input")
print("Number of elements located using TAG_NAME:", len(elements_tag))

element_link = driver.find_element(By.LINK_TEXT, "Home")
print("Element located using LINK_TEXT:", element_link.text)

elements_class = driver.find_elements(By.CLASS_NAME, "form-control")
print("Number of elements located using CLASS_NAME:", len(elements_class))

time.sleep(3)

driver.quit()