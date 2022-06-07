
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

driver.get("https://www.google.com/")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("apple")
optionlist = driver.find_elements(By.CSS_SELECTOR, '.erkvQe li')
print(len(optionlist))

for ele in optionlist:
    print(ele.text)
    if ele.text == "apple watch":
        ele.click()
        break

time.sleep(3)
driver.quit()

