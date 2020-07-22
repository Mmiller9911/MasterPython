from behave import step
from helpers.webcommon import WebCommon
from config import locatorsconfig
import pdb
from dao.usersDAO import UsersDAO

from steps import webstepscommon


@step("I type '{}' into the username field of login form")
def type_email_into_username_of_login_form(context, email):
    wc = WebCommon()
    email_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_name']['type']
    email_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_name']['locator']
    wc.type_into_element(context, email, email_locator_type, email_locator_string)


@step("I type '{}' into the password field of login form")
def type_password_into_password_of_login_form(context, password):
    wc = WebCommon()
    password_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_password']['type']
    password_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['login_user_password']['locator']
    wc.type_into_element(context, password, password_locator_type, password_locator_string)


@step("the users can log in to mystore")
def users_can_log_in(context):
    number_of_users = len(context.users_list)
    wc = WebCommon()
    for i in range(0, number_of_users):
        type_email_into_username_of_login_form(context, context.users_list[i][7])
        type_password_into_password_of_login_form(context, context.users_list[i][8])
        click_on_button_name(context, 'login')
        registered_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_confirmed']['type']
        registered_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_confirmed']['locator']
        wc.assert_element_visible(context, registered_locator_type, registered_locator_string)
        wc.click(context, registered_locator_type, registered_locator_string)


@step('I register the users on mystore')
def step_impl(context):
    number_of_users = len(context.users_list)
    for i in range(0, number_of_users):
        type_email_into_username_of_registration_form(context, i)
    initial_db_users = context.db_users
    final_db_users = UsersDAO().get_number_of_users()
    assert final_db_users[0]['COUNT(*)'] == initial_db_users[0]['COUNT(*)'] + number_of_users


@step("I type the users email and password into registration form for user {user_number}")
def type_email_into_username_of_registration_form(context, user_number):
    #import pdb; pdb.set_trace()
    converted_user_number = int(user_number)
    wc = WebCommon()
    email = context.users_list[converted_user_number][7]
    password = context.users_list[converted_user_number][8]

    email_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_name']['type']
    email_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_name']['locator']
    wc.type_into_element(context, email, email_locator_type, email_locator_string)

    password_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_password']['type']
    password_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_password']['locator']
    wc.type_into_element(context, password, password_locator_type, password_locator_string)

    register_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_confirm']['type']
    register_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_confirm']['locator']
    wc.click(context, register_locator_type, register_locator_string)

    registered_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_confirmed']['type']
    registered_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['register_user_confirmed']['locator']
    wc.assert_element_visible(context, registered_locator_type, registered_locator_string)
    wc.click(context, registered_locator_type, registered_locator_string)


@step("I click on the '{btn_name}' button")
def click_on_button_name(context, btn_name):
    wc = WebCommon()
    if btn_name.lower() in ('login', 'log in'):
        login_btn_locator_type = locatorsconfig.MY_ACCOUNT_LOCATORS['login_button']['type']
        login_btn_locator_string = locatorsconfig.MY_ACCOUNT_LOCATORS['login_button']['locator']
    else:
        raise Exception("Not implemented")

    wc.click(context, login_btn_locator_type, login_btn_locator_string)


@step("the user should be logged in")
def user_should_be_logged_in(context):
    wc = WebCommon()
    nav_bar_type = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav']['type']
    nav_bar_text = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav']['locator']

    logout_type = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['type']
    logout_text = locatorsconfig.MY_ACCOUNT_LOCATORS['left_nav_logout_btn']['locator']

    wc.assert_element_visible(context, nav_bar_type, nav_bar_text)
    wc.assert_element_visible(context, logout_type, logout_text)


@step("error message with email '{email}' should be displayed")
def error_message_with_email_should_be_displayed(context, email):
    wc = WebCommon()
    expected_msg = "Error: The password you entered for the email address {email} is incorrect. Lost your password?".format(email=email)
    error_box_type = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_text = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['locator']

    is_exist = wc.element_contains_text(context, expected_msg, error_box_type, error_box_text)

    if is_exist:
        print("pass")
    else:
        raise Exception("Incorrect message shown on failed log in.  Email: {}".format(email))


@step("error message with 'Unknown email' should be displayed")
def error_message_with_unknown_email_should_be_displayed(context):
    wc = WebCommon()
    expected_msg = "Unknown email address. Check again or try your username."
    error_box_type = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['type']
    error_box_text = locatorsconfig.MY_ACCOUNT_LOCATORS['error_box']['locator']
    is_exist = wc.element_contains_text(context, expected_msg, error_box_type, error_box_text)

    if is_exist:
        print("pass")
    else:
        raise Exception("Incorrect message shown for non existing user.")


@step('the "{nav_bar}" bar should be visible')
def verify_nav_bars_visible(context, nav_bar):
    wc = WebCommon()
    expected_bars = ['main navigation', 'top navigation', 'options']
    if nav_bar not in expected_bars:
        raise Exception("The passed in nav_bar type is not one of expected."
                            "Actual: {}, Expected in: {}".format(nav_bar, expected_bars))

    locator_info = locatorsconfig.LOCATORS.get(nav_bar)
    locator_type = locator_info['type']
    locator_text = locator_info['locator']

    nav_element = wc.find_element(context, locator_type, locator_text)
    wc.is_element_visible(nav_element)



