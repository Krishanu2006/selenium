from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# =========================================================
# ASSIGNMENT 3: CSS SELECTOR CHALLENGE
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
# 1. CSS SELECTOR - TEXT INPUT
# =========================================================

text_inputs = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='text']"
)

print("\n========== TEXT INPUTS ==========")
print("Total Text Input Elements:", len(text_inputs))

for i, element in enumerate(text_inputs, start=1):
    print(
        i,
        "| ID:",
        element.get_attribute("id"),
        "| Name:",
        element.get_attribute("name")
    )


# =========================================================
# 2. CSS SELECTOR - RADIO BUTTONS
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
# 3. CSS SELECTOR - CHECKBOXES
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


# Select first checkbox
if len(checkboxes) > 0:

    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    print("First checkbox selected.")


# =========================================================
# 4. WILDCARD SELECTOR - STARTS WITH (^=)
# =========================================================

starts_with = driver.find_elements(
    By.CSS_SELECTOR,
    "input[id^='date']"
)

print("\n========== STARTS WITH (^=) ==========")
print("Elements whose ID starts with 'date':", len(starts_with))

for element in starts_with:
    print(
        "ID:",
        element.get_attribute("id")
    )


# =========================================================
# 5. WILDCARD SELECTOR - CONTAINS (*=)
# =========================================================

contains = driver.find_elements(
    By.CSS_SELECTOR,
    "input[id*='date']"
)

print("\n========== CONTAINS (*=) ==========")
print("Elements whose ID contains 'date':", len(contains))

for element in contains:
    print(
        "ID:",
        element.get_attribute("id")
    )


# =========================================================
# 6. WILDCARD SELECTOR - ENDS WITH ($=)
# =========================================================

ends_with = driver.find_elements(
    By.CSS_SELECTOR,
    "input[id$='date']"
)

print("\n========== ENDS WITH ($=) ==========")
print("Elements whose ID ends with 'date':", len(ends_with))

for element in ends_with:
    print(
        "ID:",
        element.get_attribute("id")
    )


# =========================================================
# WAIT AND CLOSE
# =========================================================

time.sleep(3)

driver.quit()