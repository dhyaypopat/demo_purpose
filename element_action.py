from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://classic.crmpro.com/')
time.sleep(3)

username_ele = driver.find_element(By.NAME, 'username')
password_ele = driver.find_element(By.NAME, 'password')
login_button_ele = driver.find_element(By.XPATH, "//input[@type = 'submit']")

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username_ele, 'demo12@gmail.com').perform()
act_chains.send_keys_to_element(password_ele, '1234567890').perform()
act_chains.click(login_button_ele).perform()

time.sleep(2)
driver.close()
