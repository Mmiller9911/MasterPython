from selenium import webdriver

# iframe, framset, frame - means there is a frame on the page
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame("mce_0_ifr")  # frame id, name, index values
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am automating!")
driver.switch_to.default_content()  # return the the html page
print(driver.find_element_by_tag_name("h3").text)


