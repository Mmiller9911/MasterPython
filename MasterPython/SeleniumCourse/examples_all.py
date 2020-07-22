
from selenium import webdriver
from selenium.webdriver.support.select import Select

##################################################################
#  Examples of all useful code                                   #
##################################################################
# from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
# # driver = webdriver.Firefox(executable_path='C:\\seleniumdrivers\geckodriver.exe')
# driver = webdriver.Ie(executable_path='C:\\seleniumdrivers\IEDriverServer.exe')
# driver.get('https://rahulshettyacademy.com/')
# print(driver.title)
# print(driver.current_url)
# driver.minimize_window()
# driver.maximize_window()
# driver.back()
# driver.refresh()
# driver.close()  # close current window
# driver.quit()   # close all windows

##################################################################
#  Static dropdown                                               #
##################################################################
dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)  # first entry in the list
dropdown.select_by_visible_text('Female')
#dropdown.select_by_value()  # you can pass in a specific value if it is configured


##################################################################
#  Navigating parent/child relationships                         #
##################################################################

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://login.salesforce.com/')
driver.find_element_by_css_selector("#username").send_keys('Matt')
driver.find_element_by_css_selector(".password").send_keys('Matt2103')
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

##################################################################
#  Using a list to check checkboxes                              #
##################################################################
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for option in checkboxes:
    assert option.is_selected()  # AssertionError as not checked
    option.click()
    assert option.is_selected()
#############
for option in checkboxes:
    print(option.get_attribute("value"))
    if option.get_attribute("value") == "option2":
        option.click()
        assert option.is_selected()

##################################################################
#  Using a list to check radiobuttons                            #
##################################################################
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
radioButtons = driver.find_elements_by_xpath("//input[@name='radioButton']")

print(len(radioButtons))

for option in radioButtons:
    print(option.get_attribute("value"))
    if option.get_attribute("value") == "radio3":
        option.click()
        assert option.is_selected()

##################
radioButtons = driver.find_elements_by_xpath("//input[@name='radioButton']")
radioButtons[2].click()
radioButtons[2].is_selected()

##################################################################
#  Handle a js popup                                             #
##################################################################
import time
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
validateText = 'Option3'
driver.find_element_by_css_selector('#name').send_keys('Option3')
driver.find_element_by_id('alertbtn').click()
alert = driver.switch_to.alert
print(alert.text)
assert validateText in alert.text
alert.accept()
##################
alert = driver.switch_to.alert
time.sleep(2)
print(alert.text)
alert.dismiss()

##################################################################
#  Use an Implicit wait                                          #
##################################################################
#  This means that ALL elements will wait for 5 seconds before failing
##################################################################
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
#TODO ===================================================================================================
driver.implicitly_wait(5)  # global wait until 5 seconds (maximum) if object is not displayed (all steps)
#TODO ===================================================================================================
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
time.sleep(4)
#  driver.find_element_by_css_selector('div.product').send_keys('ber')
number_items = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(number_items)
assert number_items == 3
#  driver.close()

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector(".promoInfo").text)
##################################################################
#  Use an Explicit wait                                          #
###############################################################################
#  This means that only the targeted element will wait for the specified time #
###############################################################################
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
time.sleep(4)
#  driver.find_element_by_css_selector('div.product').send_keys('ber')
number_items = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(number_items)
assert number_items == 3
#  driver.close()

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
driver.close()
###############################################################################
#  Switching across multiple tabs                                             #
###############################################################################

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element_by_link_text("Click Here").click()
parent = driver.window_handles[0]
child = driver.window_handles[1]

driver.switch_to.window(child)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(parent)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
###############################################################################
#  Switching to a frame and back                                              #
###############################################################################
# iframe, framset, frame - means there is a frame on the page
driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame("mce_0_ifr")  # frame id, name, index values
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am automating!")
driver.switch_to.default_content()  # return the the html page
print(driver.find_element_by_tag_name("h3").text)

###############################################################################
#  Switching to a frame and performing a dynamic action                       #
###############################################################################
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
###############################################################################
#  Right-click, double-click and hidden items actions                         #
###############################################################################
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

###############################################################################
#  Using Javascript events instead of selenium to scroll, click ect           #
###############################################################################

# JSDOM can access any elements on the webpage just as selenium does
# Selenium has a method to execute javascript code in it
# You can use the DOM of javascript to find things if selenium cannot
# selenium can only get text from the elements which are present when the page is located - it is not possible to get text which you have entered using .text()
# if an element is not viewable because something is over it on the page it is possible to use the DOM to click on it instead
# selenium does not support scrolling but JS does - common interview question
# DOM tree
# The backbone of an HTML document is tags.
#
# According to the Document Object Model (DOM), every HTML tag is an object. Nested tags are “children” of the enclosing one. The text inside a tag is an object as well.
#
# All these objects are accessible using JavaScript, and we can use them to modify the page.
#
# For example, document.body is the object representing the <body> tag.
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))  # value is the default to use to get the element using the DOM
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # execute this JS command - # document.getElementsByName("name")[0]
# execute JS command (selenium give over command to JS)

shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shop_button)  # use the JS to click with an event instead of using selenium directly

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # use JS to scroll to the bottom of the page
#driver.close()

###############################################################################
#  Add browser options to the browser                                         #
###############################################################################

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe',options=chrome_options)

driver.get('https://the-internet.herokuapp.com/iframe')
print(driver.title)
