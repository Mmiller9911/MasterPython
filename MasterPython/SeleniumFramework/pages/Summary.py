from selenium.webdriver.common.by import By

from SeleniumFramework.pages.Checkout import CheckoutPage


class SummaryPage:

    def __init__(self, driver):
        self.driver = driver  # add this so whenever a Homepage is created a driver object must be passed through

    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def p_checkout_button(self):
        self.driver.find_element(*SummaryPage.checkout_button).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

