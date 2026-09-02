from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
broswername="chrome"

driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "[id^='name']").send_keys("TEST")
driver.find_element(By.CSS_SELECTOR, "[id$='email']").send_keys("test@example.com")
driver.find_element(By.CSS_SELECTOR, "[id*='phone']").send_keys("1234567890")
time.sleep(5)
driver.quit()
