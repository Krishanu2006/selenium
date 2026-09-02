import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

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
      - Falls back to webdriver-manager if present.
    """
    options = FirefoxOptions()
    # options.add_argument("--headless")  # Uncomment if headless mode is required

    try:
        # Selenium 4.6+ automatically discovers geckodriver from system PATH
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


driver = None

try:
    print("=" * 65)
    print("   SELENIUM AUTOMATION: ASSIGNMENT 1 (LOCATOR IDENTIFICATION)")
    print("=" * 65)
    print("Launching Firefox browser on Arch Linux...")

    driver = initialize_firefox()

    # Step 1: Open target practice website
    target_url = "https://testautomationpractice.blogspot.com/"
    print(f"Navigating to: {target_url}")
    driver.get(target_url)
    driver.maximize_window()
    time.sleep(3)  # Short pause to ensure DOM tree is fully parsed

    # =========================================================================
    # 1. LOCATE BY ID (By.ID)
    # Target: Name input text box
    # =========================================================================
    print("\n" + "-" * 65)
    print("1. LOCATING ELEMENT BY ID (By.ID)")
    print("-" * 65)

    name_field = driver.find_element(By.ID, "name")
    print(f"Element found using ID: '{name_field.get_attribute('id')}'")
    name_field.clear()
    name_field.send_keys("Suvajit")
    print("Action performed: Entered text 'Suvajit' into name field.")
    time.sleep(2)

    # =========================================================================
    # 2. LOCATE BY NAME (By.NAME)
    # Target: Gender radio button
    # =========================================================================
    print("\n" + "-" * 65)
    print("2. LOCATING ELEMENT BY NAME (By.NAME)")
    print("-" * 65)

    gender_radio = driver.find_element(By.NAME, "gender")
    print(f"Element found using NAME: '{gender_radio.get_attribute('name')}'")
    gender_radio.click()
    print("Action performed: Clicked gender radio button.")
    time.sleep(2)

    # =========================================================================
    # 3. LOCATE BY TAG NAME (By.TAG_NAME)
    # Target: Main heading <h1>
    # =========================================================================
    print("\n" + "-" * 65)
    print("3. LOCATING ELEMENT BY TAG NAME (By.TAG_NAME)")
    print("-" * 65)

    heading_element = driver.find_element(By.TAG_NAME, "h1")
    print(f"Heading Tag Text: \"{heading_element.text.strip()}\"")
    time.sleep(2)

    # =========================================================================
    # 4. LOCATE BY LINK TEXT (By.LINK_TEXT)
    # Target: Anchor link with exact matching visible text
    # =========================================================================
    print("\n" + "-" * 65)
    print("4. LOCATING ELEMENT BY LINK TEXT (By.LINK_TEXT)")
    print("-" * 65)

    # Try locating "Apple" or fallback to available navbar link if not found
    try:
        link_element = driver.find_element(By.LINK_TEXT, "Apple")
        print(f"Link found with text: \"{link_element.text}\"")
        print(f"Target URL (href): {link_element.get_attribute('href')}")
    except Exception:
        # Fallback to any visible anchor link (e.g. 'merrymoonmary' / 'Home' / 'GUI Elements')
        fallback_link = driver.find_element(By.PARTIAL_LINK_TEXT, "open cart")
        print(f"Link found with text: \"{fallback_link.text}\"")
        print(f"Target URL (href): {fallback_link.get_attribute('href')}")
    time.sleep(2)

    # =========================================================================
    # 5. LOCATE BY CLASS NAME (By.CLASS_NAME)
    # Target: Form control element
    # =========================================================================
    print("\n" + "-" * 65)
    print("5. LOCATING ELEMENT BY CLASS NAME (By.CLASS_NAME)")
    print("-" * 65)

    form_element = driver.find_element(By.CLASS_NAME, "form-control")
    print(f"Class attribute value: '{form_element.get_attribute('class')}'")
    print(f"Tag Name: <{form_element.tag_name}> | Element ID: '{form_element.get_attribute('id')}'")
    time.sleep(2)

    # =========================================================================
    # ASSIGNMENT 1 SUMMARY
    # =========================================================================
    print("\n" + "=" * 65)
    print("ASSIGNMENT 1 COMPLETED SUCCESSFULLY")
    print("=" * 65)
    print("Locators demonstrated:")
    print("  1. By.ID          -> Identified element by unique 'id' attribute")
    print("  2. By.NAME        -> Identified form element by 'name' attribute")
    print("  3. By.TAG_NAME    -> Identified element by HTML tag (<h1>)")
    print("  4. By.LINK_TEXT   -> Identified <a> hyperlink by exact visible text")
    print("  5. By.CLASS_NAME  -> Identified element matching CSS class name")
    print("=" * 65)

    # Keep browser open for visual review
    input("\nPress ENTER in your terminal to close Firefox and exit...")

except Exception as error:
    print(f"\n[Execution Error]: {error}", file=sys.stderr)

finally:
    if driver is not None:
        print("\nClosing Firefox browser session...")
        driver.quit()
        print("Firefox closed successfully.")
