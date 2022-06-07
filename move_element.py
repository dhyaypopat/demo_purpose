from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://corporate.spicejet.com/RedHotOffers.aspx")
driver.maximize_window()
time.sleep(2)

'''Move element'''
login_ele = driver.find_element(By.ID,'ctl00_HyperLinkLogin')
act_chains = ActionChains(driver)
act_chains.move_to_element(login_ele).perform()
time.sleep(3)

spice_club_members_ele = driver.find_element(By.LINK_TEXT,'SpiceClub Members')
act_chains.move_to_element(spice_club_members_ele).perform()
time.sleep(3)
member_login_ele = driver.find_element(By.LINK_TEXT,'Member Login')
member_login_ele.click()
time.sleep(3)
driver.close()