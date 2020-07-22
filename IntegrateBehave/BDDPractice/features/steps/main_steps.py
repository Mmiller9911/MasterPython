from BDDCommon.CommonSteps import webstepscommon
from BDDCommon.CommonSteps import products_api_steps
from BDDCommon.CommonSteps import users_api_steps
from BDDCommon.CommonSteps import order_api_steps
from BDDCommon.CommonSteps import coupons_api_steps
import json
from features.frontend.HomePage.steps import home_page_steps
from features.frontend.MyAccountPage.steps import my_account_steps
from features.frontend.CartPage.steps import cart_page_steps
from features.frontend.CheckoutPage.steps import checkout_page_steps
from features.frontend.OrderReceivedPage.steps import order_received_page_steps
from behave import step
import pdb


@step("I create a new user")
def i_create_user(context):
    print("creating new user")
    print("")
    print("another string")
    username = context.config.userdata.get('name')
    print(username)


@step("I access string in a step")
def i_get_string(context):
    string = context.text
    print(string)


@step("I add string of a different type")
def i_get_json_string(context):
    my_json = json.loads(context.text)
    print(my_json['first_name'])


@step("I have a failing test")
def i_need_a_fail(context):
    assert True == 0