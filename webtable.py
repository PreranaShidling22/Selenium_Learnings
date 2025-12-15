from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

allData=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
print(len(allData))

all=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[2]")
print(all.text)

