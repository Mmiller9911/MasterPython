from behave import step
from BDDCommon.CommonConfigs.locatorsconfig import CART_PAGE_LOCATORS
from BDDCommon.CommonFuncs import webcommon
import logging as logger


@step("I select 'Free Shipping' option")
def i_select_free_shipping_option(context):
    logger.info("11111")
    logger.info("about to select free shipping option")
    free_ship = CART_PAGE_LOCATORS['free_shipping_radio']
    webcommon.click(context, free_ship['type'], free_ship['locator'])
    webcommon.assert_radio_is_selected(context, free_ship['type'], free_ship['locator'])


@step("I click on 'Proceed to checkout' button on the cart page")
def and_i_click_on_proceed_to_checkout_button(context):
    proceed_button = CART_PAGE_LOCATORS['proceed_to_checkout_btn']

    max_tries = 3
    try_count = 0
    while try_count < max_tries:
        try:
            webcommon.click(context, proceed_button['type'], proceed_button['locator'])
            break
        except Exception as e:
            try_count += 1
            print(f"failed to click on proceed to checkout. Retry number: {try_count}")
    else:
        raise Exception(f"failed to click on proceed to checkout button after 3 retries")


