import json
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