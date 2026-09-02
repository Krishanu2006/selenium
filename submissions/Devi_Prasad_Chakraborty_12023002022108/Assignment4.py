from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_button_test")

# 🔹 Switch to iframe (important)
driver.switch_to.frame("iframeResult")

# 🔹 Locate button inside body (child selector)
button = driver.find_element(By.CSS_SELECTOR, "body > button")

# 🔹 Interact (click)
button.click()

print("Button clicked successfully")

input("Press Enter to close...")

driver.quit()