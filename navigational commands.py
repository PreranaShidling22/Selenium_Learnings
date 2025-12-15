from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.get("https://www.snapdeal.com/")
# driver.get("https://www.amazon.com/")

# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element.send_keys("mac")

elements = driver.find_elements(By.XPATH,"//footer[@class='footer']//a")
print(len(elements))
print(elements[0].text)


for ele in elements:
    print(ele.text)
