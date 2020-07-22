from SeleniumFramework.pages.Home import HomePage
from SeleniumFramework.utilities.BaseClass import BaseClass


class TestOne(BaseClass):  # inherit from baseclass to get the knowledge of setup fixture (and not have to define every feature)

    def test_e2e(self):

        log = self.getLogger()

        #Home_page
        home_page = HomePage(self.driver)

        #Shop_page
        shop_page = home_page.p_go_to_shop_tab()

        log.info("getting all products")
        products = shop_page.es_products()

        i = -1
        for individual_product in products:
            i = i + 1
            if individual_product.text == 'Blackberry':
                shop_page.add_item_to_trolley().click()  # click add to trolley on the item
        summary_page = shop_page.p_go_to_summary()  # shows the items selected and the price

        #Summary_page
        checkout_page = summary_page.p_checkout_button()

        #Checkout_page
        checkout_page.e_location_entry_field().send_keys("ind")
        log.info("Entering country name")
        self.verifylinktextpresent("India")
        checkout_page.e_text_entered("India").click()
        checkout_page.e_terms_and_conditions_checkbox().click()
        checkout_page.e_complete_purchase_button().click()
        alert_success = checkout_page.e_order_complete_dialog().text
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in alert_success
        self.driver.get_screenshot_as_file("screen.png")
