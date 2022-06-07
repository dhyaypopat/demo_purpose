from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
time.sleep(3)

right_click_ele = driver.find_element(By.XPATH , "//span[text()='right click me']")
act_chains = ActionChains(driver)
act_chains.context_click(right_click_ele).perform()
time.sleep(5)

right_click_options = driver.find_elements(By.CSS_SELECTOR,'li.context-menu-icon span')
for ele in right_click_options:
    print(ele.text)
    if ele.text == "Copy":
        ele.click()
        break

driver.quit()