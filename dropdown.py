from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

def select_values(element,value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_values_from_dropdown(dropdown,options):
    print(len(con_options))
    #print(len(state_options))
    for ele in dropdown:
        print(ele.text)

        if ele.text == 'India':
            ele.click()
            break

con_options = driver.find_elements(By.TAG_NAME,'option')
state_options = driver.find_elements(By.XPATH,'//select[@id="Form_submitForm_State"]/option')
print(len(state_options))
#state_options = driver.find_elements(By.TAG_NAME,'State')

select_values_from_dropdown(con_options ,"India")
#select_values_from_dropdown(state_options,'Gujarat')

ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
ele_state = driver.find_element(By.ID,'Form_submitForm_State')


select_values(ele_country, 'India')
time.sleep(3)
select_values(ele_state,'Gujarat')
time.sleep(3)

driver.close()