from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
time.sleep(3)
# ''''Drag & Drop element''''
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
actChain = ActionChains(driver)
#actChain.drag_and_drop(source, target).perform()
#-----Another method---------
actChain.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(3)