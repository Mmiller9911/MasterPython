# JSDOM can access any elements on the webpage just as selenium does
# Selenium has a method to execute javascript code in it
# You can use the DOM of javascript to find things if selenium cannot
# selenium can only get text from the elements which are present when the page is located - it is not possible to get text which you have entered using .text()
# if an element is not viewable because something is over it on the page it is possible to use the DOM to click on it instead
# selenium does not support scrolling but JS does - common interview question
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
