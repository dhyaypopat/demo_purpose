from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME,'upfile').send_keys('/Users/dhyaypopat/PycharmProjects/demo1/dropdown.py')
driver.find_element(By.XPATH , "//input[@type='submit']").click()

time.sleep(5)

driver.close()

