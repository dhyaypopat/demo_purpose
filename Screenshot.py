from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
options =webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)

driver.get('http://www.amazon.in')
driver.maximize_window()
'''
Screenshot
driver.get_screenshot_as_file('amazon1.png')
'''

#Full Screenshots

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width') , S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot("amazon.png")
