from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://classic.crmpro.com/index.html")
# driver.get('https://www.amazon.in/')
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
# driver.execute_script("arguments[0].click();",best_sellers)

# title = driver.execute_script("return document.title;")
# print(title)

# driver.execute_script("history.go(0);")
# time.sleep(2)
# driver.execute_script("alert('hello Dhyay');")
# time.sleep(2)
print(driver.execute_script("return document.documentElement.innerText"))

# form = driver.find_element(By.ID,'hs-login')
driver.execute_script("arguments[0].style.border = '3px solid red'", best_sellers)
time.sleep(2)
driver.quit()
