"""
Assignment 3: CSS Selector Challenge - Wildcard attribute selectors
Site: https://rahulshettyacademy.com/AutomationPractice/

Goal: Locate elements whose id/attribute value is dynamic or shares a
common prefix/suffix, using CSS wildcard selectors instead of hardcoding
a full fixed id.

CSS Wildcard Cheat Sheet:
    [attr^='value']  -> attribute STARTS WITH value
    [attr$='value']  -> attribute ENDS WITH value
    [attr*='value']  -> attribute CONTAINS value anywhere
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Optional fallback support for webdriver-manager if installed
try:
    from webdriver_manager.firefox import GeckoDriverManager
    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False


def initialize_firefox():
    """
    Initializes and returns a Firefox WebDriver instance.
    Optimized for Arch Linux:
      - Uses native geckodriver / Selenium Manager by default.
      - Falls back to webdriver-manager if available.
    """
    options = FirefoxOptions()
    # options.add_argument("--headless")  # Uncomment for headless test runs

    try:
        # Selenium 4.6+ discovers geckodriver on Arch automatically
        return webdriver.Firefox(options=options)
    except Exception as primary_err:
        if WEBDRIVER_MANAGER_AVAILABLE:
            try:
                service = FirefoxService(GeckoDriverManager().install())
                return webdriver.Firefox(service=service, options=options)
            except Exception as fallback_err:
                raise RuntimeError(
                    f"Failed to launch Firefox via webdriver-manager: {fallback_err}"
                ) from primary_err
        raise RuntimeError(
            "Could not launch Firefox WebDriver. On Arch Linux, install geckodriver via:\n"
            "  sudo pacman -S firefox geckodriver\n"
            f"Original error: {primary_err}"
        )


TARGET_URL = "https://rahulshettyacademy.com/AutomationPractice/"
driver = None

try:
    print("=" * 65)
    print("   SELENIUM AUTOMATION: ASSIGNMENT 3 (CSS WILDCARD SELECTORS)")
    print("=" * 65)
    print("Launching Firefox browser on Arch Linux...")

    driver = initialize_firefox()
    driver.maximize_window()

    print(f"Navigating to: {TARGET_URL}")
    driver.get(TARGET_URL)

    # Initialize explicit wait
    wait = WebDriverWait(driver, 10)

    # =========================================================================
    # 1. STARTS WITH: [id^='prefix']
    # Target: All checkboxes whose id starts with "checkBoxOption"
    # Expected IDs: checkBoxOption1, checkBoxOption2, checkBoxOption3
    # =========================================================================
    print("\n" + "-" * 65)
    print("1. CSS WILDCARD: STARTS WITH -> [id^='checkBoxOption']")
    print("-" * 65)

    checkboxes = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "[id^='checkBoxOption']")
        )
    )
    print(f"Found {len(checkboxes)} checkboxes via [id^='checkBoxOption']:\n")

    for index, cb in enumerate(checkboxes, start=1):
        cb.click()
        cb_id = cb.get_attribute("id")
        cb_val = cb.get_attribute("value")
        print(f"  {index}. Clicked checkbox id='{cb_id}' (value='{cb_val}') -> Checked: {cb.is_selected()}")
        time.sleep(1)

    # =========================================================================
    # 2. CONTAINS: [id*='substring']
    # Target: Checkboxes containing 'BoxOption' anywhere in the ID
    # =========================================================================
    print("\n" + "-" * 65)
    print("2. CSS WILDCARD: CONTAINS -> [id*='BoxOption']")
    print("-" * 65)

    contains_match = driver.find_elements(By.CSS_SELECTOR, "[id*='BoxOption']")
    print(f"Found {len(contains_match)} elements matching contains selector [id*='BoxOption']")
    for index, elem in enumerate(contains_match, start=1):
        print(f"  {index}. Tag: <{elem.tag_name}> | ID: '{elem.get_attribute('id')}'")

    # =========================================================================
    # 3. ENDS WITH: [id$='suffix']
    # Target: Select specifically the third checkbox ending with "Option3"
    # =========================================================================
    print("\n" + "-" * 65)
    print("3. CSS WILDCARD: ENDS WITH -> [id$='Option3']")
    print("-" * 65)

    ends_with_match = driver.find_element(By.CSS_SELECTOR, "[id$='Option3']")
    print(f"Target located: ID = '{ends_with_match.get_attribute('id')}' | Value = '{ends_with_match.get_attribute('value')}'")

    # =========================================================================
    # 4. WILDCARD ON NAME ATTRIBUTE: [name^='prefix']
    # Target: Radio buttons sharing name="radioButton"
    # =========================================================================
    print("\n" + "-" * 65)
    print("4. CSS WILDCARD ON NAME: [name^='radioButton']")
    print("-" * 65)

    radio_buttons = driver.find_elements(By.CSS_SELECTOR, "[name^='radioButton']")
    print(f"Found {len(radio_buttons)} radio buttons via [name^='radioButton']:\n")

    for index, rb in enumerate(radio_buttons, start=1):
        rb_val = rb.get_attribute("value")
        print(f"  {index}. Radio button value='{rb_val}'")

    # Click the first radio button to demonstrate interaction
    if radio_buttons:
        radio_buttons[0].click()
        print(f"\nAction: Selected first radio button (value='{radio_buttons[0].get_attribute('value')}').")
        time.sleep(1)

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 65)
    print("ASSIGNMENT 3 COMPLETED SUCCESSFULLY")
    print("=" * 65)
    print("Wildcard CSS Selectors Demonstrated:")
    print("  1. [id^='prefix']     -> Starts with (Targeted: checkBoxOption*)")
    print("  2. [id*='substring']  -> Contains    (Targeted: *BoxOption*)")
    print("  3. [id$='suffix']     -> Ends with   (Targeted: *Option3)")
    print("  4. [name^='prefix']   -> Starts with on name attribute")
    print("=" * 65)

    # Keep browser open for inspection
    input("\nPress ENTER in your terminal to close Firefox and exit...")

except Exception as err:
    print(f"\n[Execution Error]: {err}", file=sys.stderr)

finally:
    # Safely close Firefox session
    if driver is not None:
        print("\nClosing Firefox browser session...")
        driver.quit()
        print("Firefox closed successfully.")
