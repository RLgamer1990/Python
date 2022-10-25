from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

from selenium.webdriver.support import select

s = Service('C:/Users/gvaha/Desktop/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')

time.sleep(2)

# to find an element use find_elemnt(By.element, value='element name')
driver.find_element(By.NAME, value='name').send_keys('Gilad')

driver.find_element(By.NAME, value='email').send_keys('test.mail@g.com')

driver.find_element(By.ID, value='exampleInputPassword1').send_keys('Aa123456')

driver.find_element(By.ID, value='exampleCheck1').click()

select = Select(driver.find_element(By.ID, value='exampleFormControlSelect1'))
select.select_by_visible_text('Male')

driver.find_element(By.ID, value='inlineRadio2').click()

driver.find_element(By.NAME, value='bday').send_keys('19/07/1990')

driver.find_element(By.CLASS_NAME, value='btn-success').click()

print(driver.find_element(By.CLASS_NAME, value='alert-success').text)

time.sleep(2)
driver.close()
