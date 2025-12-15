from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
time.sleep(5)
print("web browser opened")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
search = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(search.is_enabled())
print(search.is_displayed())

male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female= driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(male.is_selected())
print(female.is_selected())

male.click()
print(male.is_selected())
print(female.is_selected())

# Browser commands
#
# diver.close()
# driver.quit()