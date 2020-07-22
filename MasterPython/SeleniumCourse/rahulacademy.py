import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

#driver.get('https://rahulshettyacademy.com/angularpractice/')

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element_by_css_selector('#name').send_keys('Option3')
driver.find_element_by_id('confirmbtn').click()
alert = driver.switch_to.alert
time.sleep(2)
print(alert.text)
alert.dismiss()
