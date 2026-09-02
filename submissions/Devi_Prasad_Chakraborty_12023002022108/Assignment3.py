from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Assignment 3: Locate element using CSS wildcard selector
# ^ means the attribute value starts with the given text

element = driver.find_element(By.CSS_SELECTOR, "[name^='q']")

element.send_keys("Selenium CSS Selectors")

print("Element found and text entered successfully!")

driver.quit()