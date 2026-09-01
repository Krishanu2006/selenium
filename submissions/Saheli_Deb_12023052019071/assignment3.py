from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")

# 1. CSS selector using ID
first_name = driver.find_element(By.CSS_SELECTOR, "#fname")
print("CSS ID:", first_name.get_attribute("value"))

# 2. CSS selector using attribute
newsletter = driver.find_element(
    By.CSS_SELECTOR, "input[name='newsletter']"
)
print("CSS Attribute:", newsletter.get_attribute("type"))

# 3. Wildcard selector - starts with (^=)
first_name_wildcard = driver.find_element(
    By.CSS_SELECTOR, "input[id^='f']"
)
print("Starts with 'f':", first_name_wildcard.get_attribute("value"))

# 4. Wildcard selector - contains (*=)
name_fields = driver.find_elements(
    By.CSS_SELECTOR, "input[id*='name']"
)

print("IDs containing 'name':")

for element in name_fields:
    print(element.get_attribute("id"), "->", element.get_attribute("value"))

# 5. Wildcard selector - ends with ($=)
last_name = driver.find_element(
    By.CSS_SELECTOR, "input[id$='name']"
)
print("Ends with 'name':", last_name.get_attribute("value"))

input("Press Enter to close the browser...")

driver.quit()