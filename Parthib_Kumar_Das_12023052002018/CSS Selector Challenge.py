"""
Assignment 3: CSS Selector Challenge
Site: https://testautomationpractice.blogspot.com/

Goal: Locate elements using CSS Selectors, including wildcard attribute
selectors for dynamic/varying attribute values.

CSS wildcard cheatsheet:
  [attr^="value"]  -> attribute STARTS WITH value
  [attr$="value"]  -> attribute ENDS WITH value
  [attr*="value"]  -> attribute CONTAINS value anywhere
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
wait = WebDriverWait(driver, 10)

# 1) Standard CSS selector -> input with id="name"
name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#name")))
name_field.send_keys("Selenium Tester")
print("CSS id selector -> Name field filled")

# 2) Wildcard: ID STARTS WITH "date" -> the jQuery datepicker fields
#    (e.g. datepicker, datepicker2)
date_fields = driver.find_elements(By.CSS_SELECTOR, "input[id^='date']")
print(f"Elements whose id starts with 'date': {len(date_fields)}")
for d in date_fields:
    print(" ->", d.get_attribute("id"))

# 3) Wildcard: ID ENDS WITH "btn" -> the alert/popup buttons
#    (e.g. alertbtn, confirmbtn, promptbtn)
btn_elements = driver.find_elements(By.CSS_SELECTOR, "[id$='btn']")
print(f"\nElements whose id ends with 'btn': {len(btn_elements)}")
for b in btn_elements:
    print(" ->", b.get_attribute("id"), "| text:", b.text)

# 4) Wildcard: ID CONTAINS "table" anywhere -> table-related elements
table_elements = driver.find_elements(By.CSS_SELECTOR, "[id*='table' i]")
print(f"\nElements whose id contains 'table': {len(table_elements)}")
for t in table_elements:
    print(" ->", t.get_attribute("id"))

# 5) Combine tag + attribute wildcard: any <input> whose id starts with a
#    common prefix pattern - here, the day-of-week checkboxes all have ids
#    ending in a fixed pattern, so demonstrate a "contains" match instead
day_checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox'][id]")
print(f"\nCheckboxes that have a non-empty id attribute: {len(day_checkboxes)}")
for c in day_checkboxes:
    print(" ->", c.get_attribute("id"))

time.sleep(2)
driver.quit()