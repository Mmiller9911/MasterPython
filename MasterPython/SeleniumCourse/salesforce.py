from selenium import webdriver

##################################################################
#  Navigating parent/child relationships                         #
##################################################################

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://login.salesforce.com/')
driver.find_element_by_css_selector("#username").send_keys('Matt')
driver.find_element_by_css_selector(".password").send_keys('Matt21554')
driver.find_element_by_css_selector("#username").clear()
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
driver.find_element_by_xpath("//div[@id='usernamegroup']/label")  #navigate to a child element using the parent and the child's tag (xpath)
driver.find_element_by_css_selector("div[id='usernamegroup'] label") #navigate to a child element using the parent and the child's tag (css)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)  #  navigate from grandparent to grandchild

print(driver.find_element_by_css_selector("form[name='login'] label").text)  #  navigate from grandparent to grandchild
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(1)").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(2)").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)