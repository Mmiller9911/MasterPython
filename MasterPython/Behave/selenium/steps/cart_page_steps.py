from behave import step, when
import webcommon
import logging as logger
from helpers.webcommon import WebCommon
from config.locatorsconfig import CART_PAGE_LOCATORS


@step("I select 'Free Shipping' option")
def i_select_free_shipping_option(context):
    wc = WebCommon()
    logger.info("11111")
    logger.info("about to select free shipping option")
    free_ship = CART_PAGE_LOCATORS['free_shipping_radio']
    wc.click(context, free_ship['type'], free_ship['locator'])
    wc.assert_radio_is_selected(context, free_ship['type'], free_ship['locator'])


@step("I click on 'Proceed to checkout' button on the cart page")
def and_i_click_on_proceed_to_checkout_button(context):
    proceed_button = CART_PAGE_LOCATORS['proceed_to_checkout_btn']
    wc = WebCommon()
    max_tries = 3
    try_count = 0
    while try_count < max_tries:
        try:
            wc.click(context, proceed_button['type'], proceed_button['locator'])
            break
        except Exception as e:
            try_count += 1
            print(f"failed to click on proceed to checkout. Retry number: {try_count}")
    else:
        raise Exception(f"failed to click on proceed to checkout button after 3 retries")


@step("I get the total dollar amount of the cart")
def i_get_the_total_dollar_amount_of_the_cart(context):
    import time; time.sleep(2)
    wc = WebCommon()
    total_locator = CART_PAGE_LOCATORS['total_cart_value']
    total_raw = wc.get_element_text(context, total_locator['type'], total_locator['locator'])
    context.total = total_raw.replace('£', '')


@step("I apply coupon to the cart")
def i_apply_coupon_to_the_cart(context):
    coupon_field_locator = CART_PAGE_LOCATORS['coupon_code_field']
    apply_coupon_locator = CART_PAGE_LOCATORS['apply_coupon_button']
    wc = WebCommon()
    wc.type_into_element(context, context.coupon_code, coupon_field_locator['type'], coupon_field_locator['locator'])
    wc.click(context, apply_coupon_locator['type'], apply_coupon_locator['locator'])
    #import pdb; pdb.set_trace()


@step("the total should be reduced by {pct}%")
def the_total_should_be_reduced_by_pct(context, pct):
    original_total = context.total
    expected_new_total = float(original_total) * (float(pct)/100)

    context.execute_steps("when I get the total dollar amount of the cart")
    new_total = context.total

    assert float(new_total) == expected_new_total, f"Cart total after applying {pct}% coupon is not as expected." \
                                                   f"Original: {original_total}, Expected: {expected_new_total}" \
                                                   f" Actual: {new_total}"


