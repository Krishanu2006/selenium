from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver =webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

openwindow=driver.find_element(
    By.CSS_SELECTOR,"#openwindow"
)
print("open window found: ",openwindow.is_displayed())

radiobutton=driver.find_element(
    By.CSS_SELECTOR,".radioButton"
)
print("Radio button found",radiobutton.is_displayed())

radio=driver.find_element(
    By.CSS_SELECTOR,"[type='radio']"
)
radio.click()
print("3.Radio button found",radio.is_displayed())

element_start=driver.find_element(
    By.CSS_SELECTOR,"[id^='auto']"
)
print("4.Id Starts with auto:",element_start.get_attribute("id"))

radio_elements=driver.find_elements(
    By.CSS_SELECTOR,"[class*='radio']"
)
print("5.Classes containing 'radio':")
for element in radio_elements:
    print(element.get_attribute("class"))

elements_end=driver.find_elements(
    By.CSS_SELECTOR,"input[name$='name']"
)
print("6.elements whose name ends with 'name:",len(elements_end))

time.sleep(4)
driver.quit()