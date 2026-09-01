import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

# Optional fallback for webdriver-manager if installed
try:
    from webdriver_manager.firefox import GeckoDriverManager
    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False


def initialize_firefox():
    """
    Initializes and returns a Firefox WebDriver instance.
    Optimized for Arch Linux:
      - Uses geckodriver from system PATH / Selenium Manager.
      - Falls back to webdriver-manager if available.
    """
    options = FirefoxOptions()
    # options.add_argument("--headless")  # Uncomment if headless execution is needed

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


driver = None

try:
    print("=" * 60)
    print("   SELENIUM AUTOMATION: ASSIGNMENT 2 (MULTIPLE ELEMENTS)")
    print("=" * 60)
    print("Launching Firefox browser on Arch Linux...")

    driver = initialize_firefox()

    # Step 1: Open the target practice website
    target_url = "https://testautomationpractice.blogspot.com/"
    print(f"Navigating to: {target_url}")
    driver.get(target_url)
    driver.maximize_window()
    time.sleep(3)  # Short pause to ensure DOM tree is fully parsed

    # =========================================================================
    # MULTIPLE ELEMENT IDENTIFICATION: FIND ALL LINKS
    # find_elements() returns a Python list of all matching WebElements
    # =========================================================================
    print("\n" + "-" * 60)
    print("1. FINDING ALL HYPERLINKS (<a> tags)")
    print("-" * 60)

    all_links = driver.find_elements(By.TAG_NAME, "a")

    # Display total count using len()
    print(f"Total number of links found on the page: {len(all_links)}\n")
    time.sleep(1)

    # =========================================================================
    # ITERATING THROUGH THE LIST OF ELEMENTS
    # =========================================================================
    print("List of visible links on the webpage:")
    print("-" * 60)

    count = 1
    for link in all_links:
        try:
            link_text = link.text.strip()

            # Filter and print only links with visible text
            if link_text:
                print(f"{count:>3}. {link_text}")
                count += 1
        except Exception as elem_err:
            # Handle any stale elements gracefully
            continue

    time.sleep(1)

    # =========================================================================
    # ASSIGNMENT SUMMARY
    # =========================================================================
    print("\n" + "=" * 60)
    print("ASSIGNMENT 2 COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("Concepts demonstrated:")
    print("  1. driver.find_elements(By.TAG_NAME, 'a') -> Returns list of WebElements")
    print("  2. len(all_links)                          -> Gets total count of elements")
    print("  3. for link in all_links:                  -> Iterates over the list")
    print("  4. link.text                               -> Reads visible element text")
    print("=" * 60)

    # Keep browser open for inspection
    input("\nPress ENTER in your terminal to close Firefox and exit...")

except Exception as error:
    print(f"\n[Execution Error]: {error}", file=sys.stderr)

finally:
    # Safely close the browser session
    if driver is not None:
        print("\nClosing Firefox browser session...")
        driver.quit()
        print("Firefox closed successfully.")
