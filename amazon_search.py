from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

list1 = driver.find_elements(By.TAG_NAME , 'a')
print(len(list1))

for ele in list1:
    link_list1 = ele.text
    print(link_list1)
    print(ele.get_attribute('href'))

image = driver.find_elements(By.TAG_NAME,'img')
print(len(image))

for ele in image:
    print(ele.get_attribute('src'))