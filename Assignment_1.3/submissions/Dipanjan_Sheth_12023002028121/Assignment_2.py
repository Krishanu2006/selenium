from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# =========================================================
# ASSIGNMENT 2: MULTIPLE ELEMENT IDENTIFICATION
# =========================================================

# Start Chrome browser
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Open Automation Practice Form
driver.get(
    "https://testautomationpractice.blogspot.com/2018/09/automation-form.html"
)

# Maximize browser
driver.maximize_window()

time.sleep(2)


# =========================================================
# 1. FIND ALL INPUT ELEMENTS
# =========================================================

inputs = driver.find_elements(
    By.TAG_NAME,
    "input"
)

print("\n========== ALL INPUT ELEMENTS ==========")
print("Total Input Elements:", len(inputs))

for i, element in enumerate(inputs, start=1):
    print(
        i,
        "| Type:",
        element.get_attribute("type"),
        "| ID:",
        element.get_attribute("id"),
        "| Name:",
        element.get_attribute("name")
    )


# =========================================================
# 2. FIND ALL RADIO BUTTONS
# =========================================================

radio_buttons = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='radio']"
)

print("\n========== RADIO BUTTONS ==========")
print("Total Radio Buttons:", len(radio_buttons))

for i, radio in enumerate(radio_buttons, start=1):
    print(
        i,
        "| Value:",
        radio.get_attribute("value")
    )


# Select the first radio button
if len(radio_buttons) > 0:
    radio_buttons[0].click()
    print("First radio button selected.")


# =========================================================
# 3. FIND ALL CHECKBOXES
# =========================================================

checkboxes = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

print("\n========== CHECKBOXES ==========")
print("Total Checkboxes:", len(checkboxes))

for i, checkbox in enumerate(checkboxes, start=1):
    print(
        i,
        "| Value:",
        checkbox.get_attribute("value")
    )


# Select the first checkbox
if len(checkboxes) > 0:

    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    print("First checkbox selected.")


# =========================================================
# 4. FIND ALL LINKS
# =========================================================

links = driver.find_elements(
    By.TAG_NAME,
    "a"
)

print("\n========== ALL LINKS ==========")
print("Total Links:", len(links))

for i, link in enumerate(links, start=1):

    link_text = link.text.strip()

    if link_text:
        print(i, ":", link_text)


# =========================================================
# WAIT AND CLOSE
# =========================================================

time.sleep(3)

driver.quit()