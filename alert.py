from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.NAME,'proceed').click()
time.sleep(5)

alert = driver.switch_to.alert
print(alert.text)
#alert.accept() # accept alert
alert.dismiss() #dismiss alert

time.sleep(3)

driver.close()