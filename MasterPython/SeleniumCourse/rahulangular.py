from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")     #start of xpath
product_title = ""
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)                  #middle of xpath
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == 'Blackberry':
        #product.find_element_by_xpath("div[2]/button").click()            #end of xpath
        product.find_element_by_xpath("div/button").click()  # end of xpath
        product_title = productName

driver.find_element_by_css_selector("a[class*='btn-primary']").click()

black = driver.find_element_by_xpath("//td[@class='col-sm-8 col-md-6']/div/div/h4/a").text
assert black == product_title
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
print(driver.find_element_by_css_selector(".alert-success").text)
alert_success = driver.find_element_by_class_name("alert-dismissible").text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in alert_success
driver.get_screenshot_as_file("screen.png")
driver.close()
