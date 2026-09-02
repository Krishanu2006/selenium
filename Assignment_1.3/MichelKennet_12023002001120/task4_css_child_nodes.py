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

    driver.find_element(By.CSS_SELECTOR, "div.form-group > input#name").send_keys("Michel Kennet")
    driver.find_element(By.CSS_SELECTOR, "div.form-group textarea#textarea").send_keys("123 Main Street")
    print(driver.find_element(By.CSS_SELECTOR, "select#country > option:nth-child(2)").text)

    time.sleep(3)

finally:
    driver.quit()