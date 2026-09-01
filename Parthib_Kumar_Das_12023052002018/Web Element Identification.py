"""
Diagnostic helper: prints the REAL id / name / placeholder / type of every
<input> and <textarea> on the Data Entry Form section so we can fix the
locators in Assignment 1-4 with 100% accurate values.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

print("=" * 70)
print("INPUT ELEMENTS")
print("=" * 70)
inputs = driver.find_elements(By.TAG_NAME, "input")
for i, el in enumerate(inputs, start=1):
    print(f"{i}. id='{el.get_attribute('id')}' | name='{el.get_attribute('name')}' "
          f"| type='{el.get_attribute('type')}' | placeholder='{el.get_attribute('placeholder')}'")

print("\n" + "=" * 70)
print("TEXTAREA ELEMENTS")
print("=" * 70)
textareas = driver.find_elements(By.TAG_NAME, "textarea")
for i, el in enumerate(textareas, start=1):
    print(f"{i}. id='{el.get_attribute('id')}' | name='{el.get_attribute('name')}' "
          f"| class='{el.get_attribute('class')}'")

print("\n" + "=" * 70)
print("SELECT (dropdown) ELEMENTS")
print("=" * 70)
selects = driver.find_elements(By.TAG_NAME, "select")
for i, el in enumerate(selects, start=1):
    print(f"{i}. id='{el.get_attribute('id')}' | name='{el.get_attribute('name')}'")

time.sleep(3)
driver.quit()
