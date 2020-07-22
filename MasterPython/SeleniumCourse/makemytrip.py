import time

from selenium import webdriver

##################################################################
#  Dynamic drop-down                                             #
##################################################################

driver = webdriver.Firefox(executable_path='C:\\seleniumdrivers\geckodriver.exe') # or #driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://www.makemytrip.com/')
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("Dimapur")
time.sleep(5)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")  # OR #cities = driver.find_elements_by_class_name("blackText")
print(len(cities))
for c in cities:
    if c.text == "Dimapur, India":
        c.click()
        break

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()

