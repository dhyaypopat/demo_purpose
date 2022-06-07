from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://londonfreelance.org/courses/frames/index.html")

frame_element = driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_element)
#driver.switch_to.frame('main')

header = driver.find_element(By.CSS_SELECTOR,'body > h2').text
print(header)

#driver.switch_to.default_content()
#driver.switch_to.parent_frame()

driver.close()