from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.reddit.com/")

cookies = driver.get_cookies()
print(driver.get_cookies())

driver.add_cookie({"name":"dhyay" ,"domain":"reddit.com", "value":"BaujChe"})

cookies = driver.get_cookies()

for cook in cookies:
    print(cook)

