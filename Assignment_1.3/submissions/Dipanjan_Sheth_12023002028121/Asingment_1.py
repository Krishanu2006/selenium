from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# =========================================================
# ASSIGNMENT 1: WEB ELEMENT IDENTIFICATION
# =========================================================

# Start Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

# Open Automation Practice Form
driver.get(
    "https://testautomationpractice.blogspot.com/2018/09/automation-form.html"
)

# Maximize browser
driver.maximize_window()

time.sleep(5)


# =========================================================
# 1. LOCATE ELEMENT USING By.ID
# =========================================================

# Locate Name field using ID
name_field = driver.find_element(
    By.ID,
    "name"
)

name_field.clear()
name_field.send_keys("Dipanjan")

print("1. By.ID")
print("Name entered:", name_field.get_attribute("value"))


# =========================================================
# 2. LOCATE ELEMENT USING By.NAME
# =========================================================

# Locate Gender radio buttons using NAME
gender_buttons = driver.find_elements(
    By.NAME,
    "gender"
)

print("\n2. By.NAME")
print("Number of gender options:", len(gender_buttons))

# Select Male
if len(gender_buttons) > 0:
    gender_buttons[0].click()
    print("Male selected")


# =========================================================
# 3. LOCATE ELEMENT USING By.TAG_NAME
# =========================================================

# Locate all input elements using TAG_NAME
input_elements = driver.find_elements(
    By.TAG_NAME,
    "input"
)

print("\n3. By.TAG_NAME")
print("Total input elements:", len(input_elements))


# =========================================================
# 4. LOCATE ELEMENT USING By.CLASS_NAME
# =========================================================

# Locate an element using CLASS_NAME
try:
    element = driver.find_element(
        By.CLASS_NAME,
        "widget-content"
    )

    print("\n4. By.CLASS_NAME")
    print("Element found using class name: widget-content")

except Exception:
    print("\n4. By.CLASS_NAME")
    print("Element with class 'widget-content' not found")


# =========================================================
# 5. LOCATE ELEMENT USING By.LINK_TEXT
# =========================================================

# The page contains a link named "Apple"
apple_link = driver.find_element(
    By.LINK_TEXT,
    "Apple"
)

print("\n5. By.LINK_TEXT")
print("Link found:", apple_link.text)


# =========================================================
# KEEP BROWSER OPEN FOR A FEW SECONDS
# =========================================================

time.sleep(3)

# Close browser
driver.quit()