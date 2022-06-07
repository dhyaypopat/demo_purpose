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
driver.implicitly_wait(5) #*[@id="username"]
driver.get("https://lms.simformsolutions.com/login/index.php")
driver.find_element(By.XPATH, "//input[contains(@type,\"username\")]").send_keys("dhyay.p@simformsolutions.com")
driver.find_element(By.XPATH, '//input[contains(@type,"password")]').send_keys("Simform")
driver.find_element(By.XPATH, '//button[contains(@type,"button")]').click()
driver.get("https://assets.stageslearning.com/collections")

print(driver.title)
driver.quit()