from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

# CSS wildcard selector
# Finds elements whose ID starts with "user_"
elements = driver.find_elements(
    By.CSS_SELECTOR,
    "[id^='user_']"
)

print("Elements found:", len(elements))

for element in elements:
    print("ID:", element.get_attribute("id"))

time.sleep(2)

driver.quit()

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("https://practice.softwaretestingmentor.com/")
#
# time.sleep(2)
#
# # CSS wildcard selector
# # Finds elements whose ID starts with "user_"
# elements = driver.find_elements(
#     By.CSS_SELECTOR,
#     "[id^='user_']"
# )
#
# print("Elements found:", len(elements))
#
# for element in elements:
#     print("ID:", element.get_attribute("id"))
#
# time.sleep(2)
#
# driver.quit()