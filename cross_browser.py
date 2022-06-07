import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
browser = "Chrome"
if browser == "Chrome":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
elif browser == "Safari":
    driver = webdriver.Safari()
else:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME,'txtUsername').send_keys("Admin")
driver.find_element(By.NAME,'txtPassword').send_keys("admin123")
driver.find_element(By.NAME, 'Submit').click()
time.sleep(5)
print(driver.title)
driver.quit()