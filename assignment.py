from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
submit=driver.find_element(By.XPATH,"//input[@type='submit']")
submit.submit()
time.sleep(5)

links=driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-main-container']//a")
for link in links:
    print(link.text)

id = driver.window_handles
print(id)
print(driver.title)


# driver.get("https://en.wikipedia.org/wiki/Selenium")
# driver.get("https://en.wikipedia.org/wiki/Selenium_in_biology")
# driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")
# driver.get("https://en.wikipedia.org/wiki/Selenium_disulfide")
# driver.get("https://en.wikipedia.org/wiki/Selenium_dioxide")

driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium in biology']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium (software)']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium disulfide']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium dioxide']").click()

windows = driver.window_handles
for win in windows:
    driver.switch_to.window(win)
    time.sleep(2)
    print(driver.title)

for win in windows:
    if win.title == "Selenium disulfide":
        driver.close()
        time.sleep(5)
