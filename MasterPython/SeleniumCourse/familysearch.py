import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://www.familysearch.org/en/')
driver.maximize_window()
# clear cookies popup
driver.switch_to.frame(0)  # frame id, name, index values
driver.find_element_by_class_name("call").click()
# switch back to html
driver.switch_to.default_content()  # return the the html page
# perform an action
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//button[@class='primary-nav-text nav-menu-trigger'][contains(text(),'Search')]")).click().perform()
time.sleep(3)
action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()
#action.move_to_element(driver.find_element_by_xpath("//a[@data-test='genealogies'][contains(text(),'Genealogies')][@class='submenu-link'][1]")).click().perform()
#elements = driver.find_elements_by_link_text("Genealogies")


