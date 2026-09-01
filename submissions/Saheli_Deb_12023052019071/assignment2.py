from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")

# Find all links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")

print("Total links found:", len(links))

# Print text of all links
for link in links:
    print(link.text)

input("Press Enter to close the browser...")

driver.quit()