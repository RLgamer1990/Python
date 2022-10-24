from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("C:/Users/giladv/Desktop/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=ser)

driver.get("http://demo.guru99.com/")
