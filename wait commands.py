from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

# implicit wait
# driver.implicitly_wait(5)
#
# search =driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
# search.send_keys("Selenium")
# search.submit()
# selenium = driver.find_element(By.XPATH,"//h3[@id='_bXATaciNIK2SseMPm5XM6QU_50']")
# selenium.submit()


# explicit wait
search =driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
search.send_keys("Selenium")
search.submit()
mywait =WebDriverWait(driver,10)
sele = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[@id='_bXATaciNIK2SseMPm5XM6QU_50']")))
# selenium = driver.find_element(By.XPATH,"//h3[@id='_bXATaciNIK2SseMPm5XM6QU_50']")
sele.submit()
