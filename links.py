from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://launchnlift.netlify.app/")

links = driver.find_elements(By.XPATH,"//a")
print(len(links))

# link= driver.find_element(By.LINK_TEXT,"FOR INVESTORS").click()
# time.sleep(2)

for link in links:
    print(link.text)
