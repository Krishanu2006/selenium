#ASSIGNMENT 1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Browser name
browsername = "chrome"


# Browser setup
if browsername.lower() == "chrome":

    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
        )
    )

else:
    raise Exception("Invalid browser name")


try:

    # Open website
    driver.get("https://automationexercise.com/")

    time.sleep(3)



    driver.find_element(
        By.LINK_TEXT, "Signup / Login"
    ).click()

    print("LINK_TEXT: Signup / Login found successfully")

    time.sleep(2)

    driver.find_element(
        By.NAME, "email"
    )

    print("NAME: Email field found successfully")


    driver.find_element(
        By.NAME, "password"
    )

    print("NAME: Password field found successfully")


    driver.find_element(
        By.TAG_NAME, "input"
    )

    print("TAG_NAME: Input element found successfully")


    driver.find_element(
        By.CLASS_NAME, "login-form"
    )

    print("CLASS_NAME: Login form found successfully")


    # Go to Products page
    driver.get(
        "https://automationexercise.com/products"
    )

    time.sleep(3)

    driver.find_element(
        By.ID, "search_product"
    )

    print("ID: Search product field found successfully")


    time.sleep(5)


finally:

    driver.quit()