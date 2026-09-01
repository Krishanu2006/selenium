from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(1)

# 1. Find all links and print their text
print("=== All Links ===")
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links: {len(links)}")
for link in links:
    if link.text.strip():
        print(f"  {link.text.strip()} -> {link.get_attribute('href')}")

# 2. Find all input fields
print("\n=== All Input Fields ===")
inputs = driver.find_elements(By.TAG_NAME, "input")
print(f"Total inputs: {len(inputs)}")
for inp in inputs:
    print(f"  Type: {inp.get_attribute('type')}, ID: {inp.get_attribute('id')}")

# 3. Find all buttons
print("\n=== All Buttons ===")
buttons = driver.find_elements(By.TAG_NAME, "button")
print(f"Total buttons: {len(buttons)}")
for btn in buttons:
    btn_text = btn.text.strip() if btn.text else ""
    if btn_text:
        print(f"  Button: {btn_text}")

# 4. Find all checkboxes and select first 3
print("\n=== Checkboxes ===")
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(f"Total checkboxes: {len(checkboxes)}")
for cb in checkboxes[:3]:
    if not cb.is_selected():
        cb.click()
        time.sleep(0.1)
    print(f"  {cb.get_attribute('id')} - Selected: {cb.is_selected()}")

# 5. Find all radio buttons and select Male
print("\n=== Radio Buttons ===")
radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print(f"Total radios: {len(radios)}")
for r in radios:
    print(f"  {r.get_attribute('id')} - Value: {r.get_attribute('value')}")
driver.find_element(By.ID, "male").click()
print("  Selected: Male")

# 6. Find all dropdown options
print("\n=== Dropdown Options (Country) ===")
options = driver.find_element(By.ID, "country").find_elements(By.TAG_NAME, "option")
print(f"Total options: {len(options)}")
for opt in options:
    print(f"  {opt.text.strip()}")

# 7. Find all rows in the Book Table
print("\n=== Book Table Data ===")
table = driver.find_element(By.XPATH, "//table[@name='BookTable']")
rows = table.find_elements(By.TAG_NAME, "tr")
print(f"Total rows: {len(rows)}")
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
    print("  " + " | ".join([c.text for c in cells]))

# 8. Find all labels
print("\n=== All Labels ===")
labels = driver.find_elements(By.TAG_NAME, "label")
print(f"Total labels: {len(labels)}")
for lbl in labels:
    label_text = lbl.text.strip() if lbl.text else ""
    if label_text:
        print(f"  {label_text}")

print("\n" + "=" * 50)
print("SUMMARY OF ALL ELEMENTS FOUND")
print("=" * 50)
print(f"  Links found        : {len(links)}")
print(f"  Input fields found : {len(inputs)}")
print(f"  Buttons found      : {len(buttons)}")
print(f"  Checkboxes found   : {len(checkboxes)}")
print(f"  Radio buttons found: {len(radios)}")
print(f"  Dropdown options   : {len(options)}")
print(f"  Table rows found   : {len(rows)}")
print(f"  Labels found       : {len(labels)}")
print("=" * 50)

time.sleep(120)
driver.quit()
