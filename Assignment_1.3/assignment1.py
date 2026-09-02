from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

user = driver.find_element(By.ID,"name")
user.send_keys("Biswayan")
print(user.get_attribute("value"))
time.sleep(2)

button = driver.find_element(By.NAME, "start")
button.click()
time.sleep(2)

inp = driver.find_element(By.TAG_NAME, "h1")
print(inp.text)
time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Apple")
print(link.get_attribute("href"))

clswrp = driver.find_element(By.CLASS_NAME, "description")
print( clswrp.text)

driver.quit()