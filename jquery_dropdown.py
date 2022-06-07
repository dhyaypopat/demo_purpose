from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def display():
    for ele in list_choice:
        print(ele.text)


def selectvalue(list_choice, value):
    if value[0] == "all":
        try:
            for ele in list_choice:
                ele.click()
        except Exception as e:
            print(e)

    else:
        for ele in list_choice:
            # print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    time.sleep(3)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()

driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(3)

list_choice = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
display()

# list = ['choice 6 2 3' , 'choice 3' , 'choice 6 2 1' , 'choice 4']
list = ['choice 7']
# list = ['all']
selectvalue(list_choice, list)
# selectvalue(list_choice,'choice 3')
# selectvalue(list_choice,'choice 6 2 1')


driver.close()
