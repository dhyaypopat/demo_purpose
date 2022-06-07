from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
driver.maximize_window()

ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
select_con = Select(ele_country)
select_con.select_by_visible_text('India')

time.sleep(3)

ele_state = driver.find_element(By.ID, 'Form_submitForm_State')
select_state = Select(ele_state)
select_state.select_by_visible_text('Goa')

time.sleep(3)

driver.quit()