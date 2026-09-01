name = driver.find_element(By.ID,"name")
name.send_keys("Angshul Sana")

animals = driver.find_element(By.NAME, "animals")
select= Select(animals)
select.select_by_visible_text("Cat")

adress = driver.find_element(By.TAG_NAME, "textarea")
adress.send_keys("kolkata")

apple= driver.find_element(By.LINK_TEXT, "Apple").click()