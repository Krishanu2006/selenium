from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

# 1)XPath - Username
user = driver.find_element(By.XPATH, "//input[@id='username']")
user.send_keys("tomsmith")
print("Username ID:", user.get_attribute("id"))

# 2)XPath - Password
pwd = driver.find_element(By.XPATH, "//input[@name='password']")
pwd.send_keys("SuperSecretPassword!")
print("Password Name:", pwd.get_attribute("name"))

# 3) XPath - Heading
heading = driver.find_element(By.XPATH, "//h2")
print("Heading:", heading.text)

# 4) XPath - Link
link = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print("Link:", link.text)

# 5)XPath - Login button
button = driver.find_element(By.XPATH, "//button[contains(@class,'radius')]")
print("Button text:", button.text)

driver.quit()