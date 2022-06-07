from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('---incognito')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://classic.crmpro.com/')
print(driver.title)
time.sleep(2)

driver.close()

