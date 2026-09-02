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

    driver.find_element(By.CSS_SELECTOR, "input[id^='nam']").send_keys("Michel Kennet")
    driver.find_element(By.CSS_SELECTOR, "input[id*='phon']").send_keys("9876543210")
    driver.find_element(By.CSS_SELECTOR, "input[id$='mail']").send_keys("michel.kennet@example.com")

    time.sleep(3)

finally:
    driver.quit()