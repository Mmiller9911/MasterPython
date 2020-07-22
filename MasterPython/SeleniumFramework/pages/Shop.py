from selenium.webdriver.common.by import By

from SeleniumFramework.pages.Summary import SummaryPage


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    add_item_to_trolley_button = (By.CSS_SELECTOR, ".card-footer button")
    go_to_summary_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def es_products(self):
        return self.driver.find_elements(*ShopPage.products)

    def e_add_item_to_trolley_button(self):
        return self.driver.find_element(*ShopPage.add_item_to_trolley_button)

    def p_go_to_summary(self):
        self.driver.find_element(*ShopPage.go_to_summary_button).click()
        summary_page = SummaryPage(self.driver)
        return summary_page

