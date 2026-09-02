from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
time.sleep(2)

start = driver.find_elements(By.CSS_SELECTOR,"input[id^='s']")
print("IDs starting with 's':",[element.get_attribute("id") for element in start])

end = driver.find_elements(By.CSS_SELECTOR,"input[id$='day']")
print("IDs ending with 'day':",[element.get_attribute("id") for element in end])

contain = driver.find_elements(By.CSS_SELECTOR,"input[id*='on']")
print("IDs containing 'on':",[element.get_attribute("id") for element in contain])

driver.quit()
