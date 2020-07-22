from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from SeleniumFramework.pages.Shop import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver  # add this so whenever a Homepage is created a driver object must be passed through

    go_to_shop_tab = (By.CSS_SELECTOR, "a[href*='shop']")  # create a class variable of shop with locator type and locator
    name_field = (By.XPATH, "//div[@class='form-group']/input[@name='name']")
    email_field = (By.XPATH, "//div[@class='form-group']/input[@name='email']")
    password_field = (By.XPATH, "//div[@class='form-group']/input[@type='password']")
    checkbox = (By.XPATH, "//div[@class='form-check']/input[@type='checkbox']")
    employment_radio_student = (By.XPATH, "//div[@class='form-check form-check-inline']/input[@id='inlineRadio1']")
    employment_radio_employed = (By.XPATH, "//div[@class='form-check form-check-inline']/input[@id='inlineRadio2']")
    dob = (By.XPATH, "//div[@class='form-group']/input[@name='bday']")
    submit = (By.XPATH, "//input[@type='submit']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")



    def p_go_to_shop_tab(self):
        self.driver.find_element(*HomePage.go_to_shop_tab).click()  # the star will make the class.shop item be decoded from a tuple correctly
        shop_page = ShopPage(self.driver)
        return shop_page

    def e_name_field(self):
        return self.driver.find_element(*HomePage.name_field)

    def e_email_field(self):
        return self.driver.find_element(*HomePage.email_field)

    def e_password_field(self):
        return self.driver.find_element(*HomePage.password_field)

    def e_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def e_employment_radio_student(self):
        return self.driver.find_element(*HomePage.employment_radio_student)

    def e_employment_radio_employed(self):
        return self.driver.find_element(*HomePage.employment_radio_employed)

    def e_dob(self):
        return self.driver.find_element(*HomePage.dob)

    def e_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def e_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def e_success_message(self):
        return self.driver.find_element(*HomePage.success_message)

