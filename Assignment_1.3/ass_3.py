from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Find elements whose ID starts with "name"
elements = driver.find_elements(
    By.CSS_SELECTOR,
    "[id^='name']"
)

print("Number of elements found:", len(elements))

for element in elements:
    print("ID:", element.get_attribute("id"))

driver.quit()