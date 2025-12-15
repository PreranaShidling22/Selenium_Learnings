from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
#
# time.sleep(2)
#
# alert = driver.switch_to.alert
# print(alert.text)
# alert.send_keys("hi")
# time.sleep(5)
# alert.accept()
# time.sleep(5)
#

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//button[normalize-space()='Simple Alert'])[1]").click()


accept=driver.switch_to.alert
accept.accept()
print("alert accepted")
time.sleep(5)

