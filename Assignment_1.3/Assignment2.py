
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

# Find all links using XPath
links = driver.find_elements(By.XPATH, "//a")

# Print the number of links
print("Total links:", len(links))

# Print the text of every link
for link in links:
    print(link.text)

driver.quit()



