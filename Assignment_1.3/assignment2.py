import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class LinkExtractorAutomation:
    def __init__(self, target_url: str):
        self.url = target_url
        # Configure Chrome options
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=self.options)
        self.extracted_data = []

    def fetch_page(self):
        """Navigates to the designated URL."""
        print(f"[INFO] Navigating to: {self.url}")
        self.driver.get(self.url)

    def extract_links(self, timeout=10):
        """
        Waits for all link elements to be present in the DOM,
        then iterates through them to collect text and dynamic attributes.
        """
        print("[INFO] Waiting for elements to load...")
        try:
            # Explicit Wait: Ensures DOM presence before gathering elements
            wait = WebDriverWait(self.driver, timeout)
            elements = wait.until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
            )
            
            total_found = len(elements)
            print(f"[SUCCESS] Located {total_found} total link elements on page.\n")

            # Parse elements cleanly to avoid StaleElementReferenceException
            for idx, element in enumerate(elements, start=1):
                try:
                    text = element.text.strip()
                    href = element.get_attribute("href")

                    # Handle empty/missing values gracefully
                    clean_text = text if text else "[No Visible Text / Image Link]"
                    clean_href = href if href else "[No Href Attribute]"

                    # Store parsed record
                    record = {
                        "index": idx,
                        "text": clean_text,
                        "url": clean_href
                    }
                    self.extracted_data.append(record)

                except Exception as elem_err:
                    print(f"[WARNING] Could not process element index {idx}: {elem_err}")

        except TimeoutException:
            print("[ERROR] Timed out waiting for <a> tags to load on the webpage.")
        except Exception as e:
            print(f"[ERROR] An unexpected error occurred during extraction: {e}")

    def display_results(self):
        """Prints formatted outcome of extracted dataset to terminal."""
        print("=" * 65)
        print(f"{'INDEX':<7} | {'LINK TEXT':<30} | {'URL':<25}")
        print("=" * 65)

        for record in self.extracted_data:
            # Truncate text for clean tabular console layout
            display_text = (record['text'][:27] + '...') if len(record['text']) > 30 else record['text']
            display_url = (record['url'][:22] + '...') if len(record['url']) > 25 else record['url']
            print(f"{record['index']:<7} | {display_text:<30} | {display_url:<25}")

        print("=" * 65)
        print(f"Total Extracted Records: {len(self.extracted_data)}")

    def close(self):
        """Safely terminates the browser session."""
        print("[INFO] Closing browser session...")
        self.driver.quit()


# Execution Block
if __name__ == "__main__":
    # You can change this URL to any website for testing (e.g., Wikipedia, Python.org)
    TARGET_WEBSITE = "https://www.python.org"

    bot = LinkExtractorAutomation(TARGET_WEBSITE)
    
    try:
        bot.fetch_page()
        bot.extract_links(timeout=10)
        bot.display_results()
    except WebDriverException as driver_err:
        print(f"[FATAL ERROR] Browser initialization or network issue: {driver_err}")
    finally:
        bot.close()