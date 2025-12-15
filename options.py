from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=options)
driver.get("https://whatmylocation.com/")
driver.maximize_window()

