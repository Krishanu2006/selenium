from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# =========================================================
# ASSIGNMENT 4: CHILD NODES USING CSS SELECTORS
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
# 1. LOCATE THE FORM
# =========================================================

form = driver.find_element(
    By.CSS_SELECTOR,
    "form"
)

print("\n========== FORM ==========")
print("Form found successfully.")


# =========================================================
# 2. FIND INPUT ELEMENTS INSIDE THE FORM
# =========================================================

inputs = form.find_elements(
    By.CSS_SELECTOR,
    "input"
)

print("\n========== INPUT ELEMENTS INSIDE FORM ==========")
print("Total input elements:", len(inputs))

for i, element in enumerate(inputs, start=1):

    print(
        i,
        "| ID:",
        element.get_attribute("id"),
        "| Type:",
        element.get_attribute("type"),
        "| Name:",
        element.get_attribute("name")
    )


# =========================================================
# 3. FIND RADIO BUTTONS INSIDE THE FORM
# =========================================================

radio_buttons = form.find_elements(
    By.CSS_SELECTOR,
    "input[type='radio']"
)

print("\n========== RADIO BUTTONS ==========")
print("Total radio buttons:", len(radio_buttons))

for i, radio in enumerate(radio_buttons, start=1):

    print(
        i,
        "| Value:",
        radio.get_attribute("value")
    )


# Select first radio button
if radio_buttons:

    radio_buttons[0].click()

    print("First radio button selected.")


# =========================================================
# 4. FIND CHECKBOXES INSIDE THE FORM
# =========================================================

checkboxes = form.find_elements(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

print("\n========== CHECKBOXES ==========")
print("Total checkboxes:", len(checkboxes))

for i, checkbox in enumerate(checkboxes, start=1):

    print(
        i,
        "| Value:",
        checkbox.get_attribute("value")
    )


# Select first checkbox
if checkboxes:

    if not checkboxes[0].is_selected():
        checkboxes[0].click()

    print("First checkbox selected.")


# =========================================================
# 5. FIND BUTTONS INSIDE THE FORM
# =========================================================

buttons = form.find_elements(
    By.CSS_SELECTOR,
    "button"
)

print("\n========== BUTTONS INSIDE FORM ==========")
print("Total buttons:", len(buttons))

for i, button in enumerate(buttons, start=1):

    print(
        i,
        "| Text:",
        button.text
    )


# =========================================================
# 6. DIRECT CHILD SELECTOR
# =========================================================

direct_children = driver.find_elements(
    By.CSS_SELECTOR,
    "form > input"
)

print("\n========== DIRECT CHILD INPUTS ==========")
print("Direct child input elements:", len(direct_children))

for i, element in enumerate(direct_children, start=1):

    print(
        i,
        "| ID:",
        element.get_attribute("id")
    )


# =========================================================
# 7. DESCENDANT SELECTOR
# =========================================================

descendant_inputs = driver.find_elements(
    By.CSS_SELECTOR,
    "form input"
)

print("\n========== DESCENDANT INPUTS ==========")
print("All input elements inside form:", len(descendant_inputs))


# =========================================================
# WAIT BEFORE CLOSING
# =========================================================

time.sleep(3)

# Close browser
driver.quit()