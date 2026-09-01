#ASSIGNMENT 2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
links=driver.find_elements(By.TAG_NAME, 'a')
print("The total number of links are:",len(links))
for link in links:
    print("Link Text", link.text)
    print("URL :",link.get_attribute("href"))
buttons=driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print("The total number of Radio buttons are: ",len(buttons))
for button in buttons:
    button.click()
time.sleep(5)
driver.quit()