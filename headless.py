from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.implicitly_wait(2)

driver.get('http://amazon.in/')
print(driver.title)
time.sleep(2)

driver.close()