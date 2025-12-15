from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as requests

driver = webdriver.Chrome()
driver.get("https://launchnlift.netlify.app/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,"a")
count = 0
url = "mailto:support@launchandlift.com"
if url.startswith("http://") or url.startswith("https://"):
    res = requests.head(url)
else:
    print(f"Invalid link: {url}")

for link in all_links:
    url = link.get_attribute("href")
    res = requests.head(url)
    if res.status_code >=400:
        count+=1
        print("invalid link",url)
        print(count)
    else:
        print("valid link",url)
        print(count)

print(count)