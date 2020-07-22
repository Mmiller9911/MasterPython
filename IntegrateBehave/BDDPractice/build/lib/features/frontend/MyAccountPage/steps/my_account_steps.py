from behave import step
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import locatorsconfig
import pdb


@step("I type '{}' into the username field of login form")
def type_email_into_username_of_login_form(context, email):

    email_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_name']['type']
    email_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_name']['locator']
    webcommon.type_into_element(context, email, email_locator_type, email_locator_string)


@step("I type '{}' into the password field of login form")
def type_password_into_password_of_login_form(context, password):
    password_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_password']['type']
    password_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_password']['locator']
    webcommon.type_into_element(context, password, password_locator_type, password_locator_string)


@step("I click on the '{btn_name}' button")
def click_on_button_name(context, btn_name):
    if btn_name.lower() in ('login', 'log in'):
        login_btn_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['login_button']['type']
        login_btn_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['login_button']['locator']
    else:
        raise Exception("Not implemented")

    webcommon.click(context, login_btn_locator_type, login_btn_locator_string)


@step("the user should be logged in")
def user_should_be_logged_in(context):
    nav_bar_type = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav']['type']
    nav_bar_text = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav']['locator']

    logout_type = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['type']
    logout_text = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['locator']

    webcommon.assert_element_visible(context, nav_bar_type, nav_bar_text)
    webcommon.assert_element_visible(context, logout_type, logout_text)


@step("error message with email '{email}' should be displayed")
def error_message_with_email_should_be_displayed(context, email):
    expected_msg = "Error: The password you entered for the email address {email} is incorrect. Lost your password?".format(email=email)
    error_box_type = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_text = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['locator']

    is_exist = webcommon.element_contains_text(context, expected_msg, error_box_type, error_box_text)

    if is_exist:
        print("pass")
    else:
        raise Exception("Incorrect message shown on failed log in.  Email: {}".format(email))


@step("error message with 'Unknown email' should be displayed")
def error_message_with_unknown_email_should_be_displayed(context):
    expected_msg = "Unknown email address. Check again or try your username."
    error_box_type = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_text = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['locator']
    is_exist = webcommon.element_contains_text(context, expected_msg, error_box_type, error_box_text)

    if is_exist:
        print("pass")
    else:
        raise Exception("Incorrect message shown for non existing user.")


@step('the "{nav_bar}" bar should be visible')
def verify_nav_bars_visible(context, nav_bar):
    expected_bars = ['main navigation', 'top navigation', 'options']
    if nav_bar not in expected_bars:
        raise Exception("The passed in nav_bar type is not one of expected."
                            "Actual: {}, Expected in: {}".format(nav_bar, expected_bars))

    locator_info = locatorsconfig.LOCATORS.get(nav_bar)
    locator_type = locator_info['type']
    locator_text = locator_info['locator']

    nav_element = webcommon.find_element(context, locator_type, locator_text)
    webcommon.is_element_visible(nav_element)

