from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open Selenium locator test page
driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")

# 1. Locate element using ID
element_id = driver.find_element(By.ID, "lname")
print("ID:", element_id.get_attribute("value"))

# 2. Locate element using NAME
element_name = driver.find_element(By.NAME, "newsletter")
print("NAME:", element_name.get_attribute("type"))

# 3. Locate element using TAG_NAME
element_tag = driver.find_element(By.TAG_NAME, "a")
print("TAG NAME:", element_tag.text)

# 4. Locate element using LINK_TEXT
element_link = driver.find_element(By.LINK_TEXT, "Selenium Official Page")
print("LINK TEXT:", element_link.text)

# 5. Locate element using CLASS_NAME
element_class = driver.find_element(By.CLASS_NAME, "information")
print("CLASS NAME:", element_class.get_attribute("value"))

# Keep browser open until Enter is pressed
input("Press Enter to close the browser...")

# Close browser
driver.quit()