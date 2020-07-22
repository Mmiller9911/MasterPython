##############################################################################################################################################
# Locators
# xpath and css are independant of dev work, they can always be used.  the other locators may or may not have been added as html attributes by a developer.
# Selenium scans the page from the top left down, this means if multiple results exist for the locator, the FIRST one will always be selected
# it is not recommended to use class as this usually returns many results
# add chropath extension for chrome - this allows checking and return of locators
# css in fastest at finding elements on a webpage
# using the element which is most unique is best practice
# bylinktext only works when the html element 'a' is used, otherwise the text is not from a link
# if a classname attribute contains multiple classes such as 'alert alert-success alert-dismissible' you should just be able to select one of them to use
# xpath has the ability to scroll UP from a certain point as well as down (css does not)
##############################################################################################################################################

# CSS syntax
# tagname[attribute='value']
# input[name='name']
# input#username (this works for ID attribute only) works the same as - #username because the tag is optional in css

# console command in chrome -
# $('#username')

# regex - //*[contains(@class,'alert-success')]
# or      //tag -  //div[contains(@class,'alert-success')]
##############################################################################################################################################
# Xpath syntax
# //tagname[@attribute='value']
# "//input[@type='submit']"
#  //input[@id='username'] works the same as [id='username'] because the tag is optional in xpath

# console command in chrome -
# $x("//input[@type='submit']")
# $x("//input[@type='checkbox']")

# regex - [class*='alert']

##############################################################################################################################################
# Find element(s) by locator
##############################################################################################################################################
# CSS SELECTORS
# driver.find_element_by_css_selector("input[name='name']").send_keys('Matt')
# .product-name - (select everything on the page with this class name)
# driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
# driver.find_element_by_css_selector('div.product').send_keys('ber')
# driver.find_element_by_css_selector("img[alt='Cart']").click()
# driver.find_elements_by_css_selector('p.product-name')
# driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
# driver.find_element_by_css_selector(".promoBtn").click()
# print(driver.find_element_by_css_selector(".promoInfo").text)
##############################################################################################################################################
# NAME
# driver.find_element_by_name('email').send_keys('Matthew@matthew.com')


##############################################################################################################################################
# ID
# driver.find_element_by_id('exampleCheck1').click()
# driver.find_element_by_id('exampleFormControlSelect1'))


##############################################################################################################################################
# XPATH

# driver.find_element_by_xpath("//input[@type='submit']").click()
# driver.find_elements_by_xpath("//input[@type='checkbox']") - get a generic locator which is common in all options


# //div[@class='product-action']/button/parent::div - go to parent element which has a tag type of div (from any point on the page)
# //div[@class='product-action']/button/parent::div/parent::div - go to parent elements and then its parent element
# //div[@class='product-action']/button/parent::div/parent::div/h4 - go to parent elements and then its parent element and then down again to h4 tag
# buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# for button in buttons:
#     print(button.find_element_by_xpath("parent::div/parent::div/h4").text)  # get the button and then use the XPATH from THERE to go up to product
#                                                                             # and down again to get the text
#     button.click()

# number_items = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
# driver.find_elements_by_xpath("//div[@class='product-action']/button")
# driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

#var1 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tr[2]/td[5]/p[1]").text
#var2 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tr[3]/td[5]/p[1]").text
#var3 = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tr[4]/td[5]/p[1]").text
# table = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/table[1]/"
# for row in range(2, 5):
#     row_path = table+"tr["+str(row)+"]/td[5]/p[1]"
#     row_text = driver.find_element_by_xpath(row_path).text
#     print(row_text)

# select a sibling div when there are multiple
# product.find_element_by_xpath("div[2]/button").click()
# product.find_element_by_xpath("div/button").click()


##############################################################################################################################################
# driver.find_element_by_class_name("alert-success").text
##############################################################################################################################################

##############################################################################################################################################
# print(driver.find_element_by_tag_name("h3").text)
##############################################################################################################################################






