from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")

# Locate the input elements inside the form using CSS child selector
first_name = driver.find_element(
    By.CSS_SELECTOR, "form>input#fname"
)

print("First name:", first_name.get_attribute("value"))

last_name = driver.find_element(
    By.CSS_SELECTOR, "form>input#lname"
)

print("Last name:", last_name.get_attribute("value"))

newsletter = driver.find_element(
    By.CSS_SELECTOR, "form>input[name='newsletter']"
)

print("Newsletter type:", newsletter.get_attribute("type"))

input("Press Enter to close the browser...")

driver.quit()