from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(2)

#time out = 10
#dynamic wait
#imp wait will be applied for all the webelements
#find element
#find elements
#only for web elements
#not for web elements : Title,URL,alerts,link


driver.get("https://app.hubspot.com/login")

print(driver.title)


username = driver.find_element(By.ID,'username')
username.send_keys("test@gmail.com")

driver.find_element(By.ID,'password').send_keys('test@123')

#driver.implicitly_wait(10)