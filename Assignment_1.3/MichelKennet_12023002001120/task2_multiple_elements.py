from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'chrome'.")

try:
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    time.sleep(2)

    for link in driver.find_elements(By.TAG_NAME, "a")[:5]:
        print(link.text.strip())

    for cb in driver.find_elements(By.XPATH, "//input[@type='checkbox']")[:7]:
        cb.click()

    time.sleep(3)

finally:
    driver.quit()
