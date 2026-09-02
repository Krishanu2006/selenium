from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
broswername="chrome"

driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("TEST")
driver.find_element(By.NAME, "show-hide").send_keys("TEST")
driver.find_element(By.TAG_NAME, "input").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Open Tab").click()
time.sleep(2)
driver.quit()