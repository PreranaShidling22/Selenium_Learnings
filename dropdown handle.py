from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
time.sleep(30)
drp_country = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
drp_country.select_by_visible_text("India")
drp_country.select_by_value("10")
