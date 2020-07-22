from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver  # add this so whenever a Homepage is created a driver object must be passed through

    location_entry_field = (By.ID, "country")
    terms_and_conditions_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    complete_purchase_button = (By.XPATH, "//input[@type='submit']")
    order_complete_dialog = (By.CLASS_NAME, "alert-dismissible")

    def e_location_entry_field(self):
        return self.driver.find_element(*CheckoutPage.location_entry_field)

    def e_text_entered(self, text):
        return self.driver.find_element(By.LINK_TEXT, text)

    def e_terms_and_conditions_checkbox(self):
        return self.driver.find_element(*CheckoutPage.terms_and_conditions_checkbox)

    def e_complete_purchase_button(self):
        return self.driver.find_element(*CheckoutPage.complete_purchase_button)

    def e_order_complete_dialog(self):
        return self.driver.find_element(*CheckoutPage.order_complete_dialog)






