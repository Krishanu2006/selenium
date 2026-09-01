"""
Diagnostic helper #2: finds the REAL id / class of elements used in
Assignment 4 (mouse-hover button, dropdown links, Copy Text button,
static table) by locating them via their visible text first.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)


def describe(label, by, value):
    try:
        el = driver.find_element(by, value)
        print(f"{label}: FOUND")
        print(f"   tag='{el.tag_name}' id='{el.get_attribute('id')}' "
              f"class='{el.get_attribute('class')}'")
        # also show the parent, useful for building child selectors
        parent = el.find_element(By.XPATH, "..")
        print(f"   PARENT -> tag='{parent.tag_name}' id='{parent.get_attribute('id')}' "
              f"class='{parent.get_attribute('class')}'")
    except Exception as e:
        print(f"{label}: NOT FOUND ({e.__class__.__name__})")
    print("-" * 70)


# "Point Me" hover button
describe("Point Me button", By.XPATH, "//*[contains(text(),'Point Me')]")

# "Mobiles" / "Laptops" dropdown links
describe("Mobiles link", By.LINK_TEXT, "Mobiles")
describe("Laptops link", By.LINK_TEXT, "Laptops")

# "Copy Text" button
describe("Copy Text button", By.XPATH, "//*[contains(text(),'Copy Text')]")

# Static web table
describe("Static table", By.XPATH,
         "//table[.//td[contains(text(),'Learn Selenium')]]")

time.sleep(3)
driver.quit()
