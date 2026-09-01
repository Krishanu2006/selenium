from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername="chrome"

if browsername.lower()=="chrome":
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browsername.lower()=="firefox":
    driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'chrome' or 'firefox'.")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

#Assignment 1
# name = driver.find_element(By.ID,"name")
# name.send_keys("Angshul Sana")

# animals = driver.find_element(By.NAME, "animals")
# select= Select(animals)
# select.select_by_visible_text("Cat")

# adress = driver.find_element(By.TAG_NAME, "textarea")
# adress.send_keys("kolkata")

# apple= driver.find_element(By.LINK_TEXT, "Apple").click()

# element= driver.find_element(By.CLASS_NAME, "form-control")
# element.send_keys("testing class")


#Assignment 2
# links = driver.find_elements(By.TAG_NAME, "a")
# for link in links:
#     print(link.text)

#Assignment 3
# inputs = driver.find_elements(By.CSS_SELECTOR, 'input[id^="input"]')
# for inp in inputs:
#     print(inp.get_attribute("id"))

# inputs = driver.find_elements(By.CSS_SELECTOR, 'input[id*="put"]')
# for inp in inputs:
#     print(inp.get_attribute("id"))

button = driver.find_element(By.CSS_SELECTOR, "#section1 > button").click()

time.sleep(5)