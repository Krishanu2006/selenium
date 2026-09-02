from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

# Find all <a> links on the main page
links = driver.find_elements(By.TAG_NAME, "a")

print("\nAll links:")
for item in links:
    print(item.text)
time.sleep(2)

# # ---------------- CheckBox ----------------
# link = driver.find_element(By.LINK_TEXT, "Checkboxes")
# print("Link:", link.text)
#
# # Click Checkboxes
# link.click()
# time.sleep(2)
#
#
# # Find all input elements
# checkboxes = driver.find_elements(By.TAG_NAME, "input")
#
# print("Total checkboxes:", len(checkboxes))
#
# # Print information about each checkbox
# for checkbox in checkboxes:
#     print("Type:", checkbox.get_attribute("type"))
#
# time.sleep(2)

driver.quit()