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
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)

    driver.find_element(By.ID, "name").send_keys("Michel Kennet")
    driver.find_element(By.NAME, "gender").click()
    driver.find_element(By.CLASS_NAME, "wikipedia-search-input").send_keys("Selenium")
    print(driver.find_element(By.TAG_NAME, "h1").text.strip())
    print(driver.find_element(By.LINK_TEXT, "Home").get_attribute("href"))

    time.sleep(3)

finally:
    driver.quit()