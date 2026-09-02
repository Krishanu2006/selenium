"""
Assignment 4: Child Nodes and Descendants Using CSS Selectors
Sites:
  1. https://rahulshettyacademy.com/AutomationPractice/
  2. https://testautomationpractice.blogspot.com/

Goal:
  Identify and locate child and nested web elements using CSS child combinators
  and structural pseudo-classes.

CSS Combinator & Pseudo-class Cheat Sheet:
    parent > child               -> DIRECT child only (one level down)
    parent descendant            -> Any descendant at any nesting depth (space)
    parent > child:nth-child(n)  -> Target the nth sibling element
    parent > child:first-child   -> Target the very first sibling
    parent > child:last-child    -> Target the last sibling
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
      - Uses native geckodriver from system PATH / Selenium Manager.
      - Falls back to webdriver-manager if available.
    """
    options = FirefoxOptions()
    # options.add_argument("--headless")  # Uncomment for headless execution

    try:
        # Selenium 4.6+ discovers geckodriver on Arch Linux automatically
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


def part_a_direct_child_and_descendants(driver, wait):
    """
    Demonstrates:
      1. Direct Child Combinator: parent > child
      2. Descendant Combinator:   parent descendant (space)
    Target Site: Rahul Shetty Academy Practice Page
    """
    target_url = "https://rahulshettyacademy.com/AutomationPractice/"
    print("\n" + "=" * 65)
    print("PART A: DIRECT CHILD & DESCENDANT COMBINATORS")
    print("=" * 65)
    print(f"Navigating to: {target_url}")
    driver.get(target_url)

    # 1. DIRECT CHILD SELECTOR: fieldset > label
    # Locates <label> elements that are DIRECT children of <fieldset>
    print("\n1. Direct Child Selector: 'fieldset > label'")
    print("-" * 65)
    labels = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "fieldset > label")
        )
    )
    print(f"Found {len(labels)} direct-child <label> elements under fieldsets.")
    for idx, lbl in enumerate(labels[:4], start=1):
        clean_text = lbl.text.strip().replace("\n", " ")
        print(f"  {idx}. Label Text: '{clean_text}'")

    # 2. DESCENDANT SELECTOR: div#checkbox-example input[type='checkbox']
    # Locates all checkboxes nested inside the checkbox container at any depth
    print("\n2. Descendant Selector: 'div#checkbox-example input[type=\"checkbox\"]'")
    print("-" * 65)
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, "div#checkbox-example input[type='checkbox']"
    )
    print(f"Found {len(checkboxes)} checkboxes inside 'div#checkbox-example':\n")

    for idx, cb in enumerate(checkboxes, start=1):
        cb.click()
        cb_id = cb.get_attribute("id")
        cb_val = cb.get_attribute("value")
        print(f"  {idx}. Clicked checkbox id='{cb_id}' (value='{cb_val}') -> Checked: {cb.is_selected()}")
        time.sleep(1)


def part_b_table_child_and_nth_selectors(driver, wait):
    """
    Demonstrates:
      1. Multi-level Child combinator: table > tbody > tr > td
      2. Structural Pseudo-class:      :nth-child(n)
    Target Site: Test Automation Practice Static & Dynamic Tables
    """
    target_url = "https://testautomationpractice.blogspot.com/"
    print("\n" + "=" * 65)
    print("PART B: TABLE CHILD COMBINATORS & :nth-child(n)")
    print("=" * 65)
    print(f"Navigating to: {target_url}")
    driver.get(target_url)

    # 1. Direct Child Row Traversal: table[name='BookTable'] > tbody > tr
    print("\n1. Direct Child Rows: 'table[name=\"BookTable\"] > tbody > tr'")
    print("-" * 65)
    rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "table[name='BookTable'] > tbody > tr")
        )
    )
    # The first row is <th> headers, remaining are data <tr>
    print(f"Found {len(rows)} total rows (including header) in BookTable.")

    # 2. nth-child to select a specific row and cell: tr:nth-child(2) > td:nth-child(1)
    print("\n2. Specific Cell via :nth-child: 'tr:nth-child(2) > td:nth-child(1)'")
    print("-" * 65)
    first_book = driver.find_element(
        By.CSS_SELECTOR,
        "table[name='BookTable'] > tbody > tr:nth-child(2) > td:nth-child(1)"
    )
    first_price = driver.find_element(
        By.CSS_SELECTOR,
        "table[name='BookTable'] > tbody > tr:nth-child(2) > td:nth-child(4)"
    )
    print(f"First Book Name : '{first_book.text.strip()}'")
    print(f"First Book Price: '{first_price.text.strip()}'")

    # 3. Extract all Authors from Column 2 across all data rows
    print("\n3. All Authors Column via Child Selector: 'tr > td:nth-child(2)'")
    print("-" * 65)
    author_cells = driver.find_elements(
        By.CSS_SELECTOR,
        "table[name='BookTable'] > tbody > tr > td:nth-child(2)"
    )
    print("Authors List extracted from table:")
    for idx, author in enumerate(author_cells, start=1):
        print(f"  {idx}. {author.text.strip()}")
    time.sleep(1)


def main():
    driver = None
    try:
        print("=" * 65)
        print("   SELENIUM AUTOMATION: ASSIGNMENT 4 (CSS CHILD NODES)")
        print("=" * 65)
        print("Launching Firefox browser on Arch Linux...")

        driver = initialize_firefox()
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Run Part A: Direct Child & Descendant Combinators
        part_a_direct_child_checkbox(driver, wait) if False else None
        part_a_direct_child_and_descendants(driver, wait)

        # Run Part B: Table Child Nodes & nth-child Selectors
        part_b_table_child_and_nth_selectors(driver, wait)

        # Summary
        print("\n" + "=" * 65)
        print("ASSIGNMENT 4 COMPLETED SUCCESSFULLY")
        print("=" * 65)
        print("CSS Combinators Demonstrated:")
        print("  1. parent > child           -> Direct child (fieldset > label)")
        print("  2. parent descendant        -> Descendant (div#checkbox-example input)")
        print("  3. parent > child:nth-child -> Specific cell (tr:nth-child(2) > td:nth-child(1))")
        print("  4. tr > td:nth-child(2)     -> Column extraction across all rows")
        print("=" * 65)

        # Keep browser open for inspection
        input("\nPress ENTER in your terminal to close Firefox and exit...")

    except Exception as err:
        print(f"\n[Execution Error]: {err}", file=sys.stderr)

    finally:
        if driver is not None:
            print("\nClosing Firefox browser session...")
            driver.quit()
            print("Firefox closed cleanly.")


if __name__ == "__main__":
    main()
