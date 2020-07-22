from behave import step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs.locatorsconfig import CHECKOUT_PAGE_LOCATORS
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_email_and_password
from BDDCommon.CommonHelpers.utilitiesHelper import generate_random_first_and_last_name


@step("I verify 'Checkout' page is loaded")
def i_verify_checkout_page_is_loaded(context):
    webcommon.assert_url_contains(context, '/checkout/')

    expected_text = 'Checkout'
    header_locator = CHECKOUT_PAGE_LOCATORS['page_header']
    contains = webcommon.element_contains_text(context, expected_text, header_locator['type'], header_locator['locator'])
    assert contains, f"header of checkout page does not contain the text '{expected_text}'."

    form_locator = CHECKOUT_PAGE_LOCATORS['checkout_form']
    webcommon.assert_element_visible(context, form_locator['type'], form_locator['locator'])


@step("I fill in the billing details form")
def i_fill_in_the_billing_details_form(context):
    rand_name = generate_random_first_and_last_name()
    f_name = rand_name['f_name']
    l_name = rand_name['l_name']
    address_1 = '39 Queens Road'
    city = 'York'
    _zip = 'LS16 7HR'
    phone = '011427326632'
    email = generate_random_email_and_password()['email']

    f_name_locator = CHECKOUT_PAGE_LOCATORS['billing_f_name_input']
    l_name_locator = CHECKOUT_PAGE_LOCATORS['billing_l_name_input']
    street_locator = CHECKOUT_PAGE_LOCATORS['billing_address1_input']
    city_locator = CHECKOUT_PAGE_LOCATORS['billing_city_input']
    zip_locator = CHECKOUT_PAGE_LOCATORS['billing_zip_input']
    phone_locator = CHECKOUT_PAGE_LOCATORS['billing_phone_input']
    email_locator = CHECKOUT_PAGE_LOCATORS['billing_email_input']

    webcommon.type_into_element(context, f_name, f_name_locator['type'], f_name_locator['locator'])
    webcommon.type_into_element(context, l_name, l_name_locator['type'], l_name_locator['locator'])
    webcommon.type_into_element(context, address_1, street_locator['type'], street_locator['locator'])
    webcommon.type_into_element(context, city, city_locator['type'], city_locator['locator'])
    webcommon.type_into_element(context, _zip, zip_locator['type'], zip_locator['locator'])
    webcommon.type_into_element(context, phone, phone_locator['type'], phone_locator['locator'])
    webcommon.type_into_element(context, email, email_locator['type'], email_locator['locator'])


@step("I click on 'Place Order' button in the checkout page")
def i_click_on_place_order_button_in_the_checkout_page(context):
    btn_locator = CHECKOUT_PAGE_LOCATORS['place_order_button']
    webcommon.click(context, btn_locator['type'], btn_locator['locator'])
