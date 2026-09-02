from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()

time.sleep(2)
driver.get("https://www.google.com/")

links=driver.find_elements(By.XPATH, "//a")
time.sleep(2)
for link in links:
    print(link.text)
    
    
time.sleep(2)
driver.quit()