# Assignment 1: Web Element Identification -> Identify and
# locate different web elements on a given webpage using By.ID,
# By.NAME, By.TAG_NAME, By.LINK_TEXT, and By.CLASS_NAME.
# Example: Locate the username field by ID, password field by Name,
# and a link by Link Text.


import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj= Service("C:/Birup/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome (service = service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
#Locator
# id Xpath,cssselector, Classname,name, linktext

#locator ID NAME
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Birup")
#driver.find_element(By.CSS_SELECTOR,"input[name=name]")
driver.find_element(By.NAME, "email").send_keys("hallow@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
#driver.find_element(By.TAG_NAME,"br").click()

#handeling static dropdown

dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_visible_text("female")
# //tagname[@attribute ='value'] --> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
message=driver.find_element(By.CLASS_NAME, "alert").text
print(message)
#assert success! in message
time.sleep(10)
