from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
action = ActionChains(driver)
action.context_click(driver.find_element_by_id('double-click')).perform()
action.double_click(driver.find_element_by_id('double-click')).perform()
alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice')
print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id("displayed-text").is_displayed())





