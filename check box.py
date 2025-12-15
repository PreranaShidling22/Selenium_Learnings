from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkbox))

# approach 1
# for i in range (len(checkbox)):
#     checkbox[i].click()

# # approach 2
# for elem in checkbox:
#     elem.click()

#to select multiple and different check checkbox


# for elem in checkbox:
#     weekname = elem.get_attribute("id")
#     if weekname== 'friday' or weekname== 'saturday' or weekname== 'sunday':
#         elem.click()
#         time.sleep(2)

#for selecting elemnts from bottom--> total no of elements - how many wants to select =starting index to start len

# for i in range(len(checkbox)-2,len(checkbox)):
#     checkbox[i].click()

# for selecting starting 2 checkboxes
for i in range(len(checkbox)):
    if i<2:
        checkbox[i].click()