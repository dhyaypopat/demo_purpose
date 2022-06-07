import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')

first_name = driver.find_element(By.ID,"firstName")
#last_name = driver.find_element(By.ID,"lastName")
email = driver.find_element(By.ID,"userEmail")
number = driver.find_element(By.ID,"userNumber")
#address = driver.find_element(By.ID,"currentAddress")


workbook = xlrd.open_workbook("Test (1).xlsx")
sheet = workbook.sheet_by_name("login")

# Get Total Number of Rows

rowCount = sheet.nrows
colCount = sheet.ncols

print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    firstname = str(sheet.cell_value(curr_row, 0))
    #lastname = str(sheet.cell_value(curr_row, 1))
    email_add = str(sheet.cell_value(curr_row, 2))
    num = str(sheet.cell_value(curr_row, 3))
    #add = str(sheet.cell_value(curr_row, 4))


first_name.send_keys(firstname)
#last_name.send_keys(lastname)
email.send_keys(email_add)
number.send_keys(num)
#address.send_keys(add)

time.sleep(5)

driver.close()