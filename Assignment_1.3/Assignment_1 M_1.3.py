'''
Assignment 1: Web Element Identification

Identify and locate different web elements on a given webpage using:
By.ID
By.NAME
By.TAG_NAME
By.LINK_TEXT
By.CLASS_NAME
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()
time.sleep(2)
id_element = driver.find_element(By.ID, "my-text-id")
print("Element found using ID:", id_element.is_displayed())
text_box = driver.find_element(By.NAME, "my-text")
print("Text box found using Name:", text_box.is_displayed())
heading = driver.find_element(By.TAG_NAME, "h1")
print("Heading found using Tag Name:", heading.is_displayed())
button = driver.find_element(By.CLASS_NAME, "btn")
print("Button found using Class Name:", button.is_displayed())
link = driver.find_element(By.LINK_TEXT, "Return to index")
print("Link found using Link Text:", link.is_displayed())
time.sleep(2)
driver.quit()