from behave import step
from helpers.utilitiesHelper import UtilitiesHelper
from apis import user_api
from dao.usersDAO import UsersDAO
import pdb


@step("I generate random email and password")
def i_generate_random_email_and_password(context):
    uh = UtilitiesHelper()
    random_info = uh.generate_random_email_and_password()
    context.random_email = random_info['email']
    context.random_password = random_info['password']


@step("I call 'create customer' API")
def i_call_create_customer_api(context):
    payload = {'email': context.random_email, 'password': context.random_password}
    create_user_response = user_api.create_user(payload)
    assert create_user_response, "Empty response for create user {}".format(payload)
    assert create_user_response['email'] == context.random_email, "Wrong email in response of 'create customer'" \
                                                                  "Call email {}, response email {}".format(
        context.random_email, create_user_response['email'])
    expected_user_name = context.random_email.split('@')[0]
    assert create_user_response['username'] == expected_user_name, "username does not match" \
                                                                   "Call username {}, response username {}".format(
        context.expected_user_name, create_user_response['username'])


@step("customer should be created")
def customer_should_be_created(context):
    db_user = UsersDAO().get_user_by_email(context.random_email)
    assert len(db_user) == 1, "Find db user in db found {} results.  Email: {}".format(len(db_user),
                                                                                       context.random_email)
    expected_user_name = context.random_email.split('@')[0]
    assert db_user[0]['user_login'] == expected_user_name, "user created in the db does not have the expected username" \
                                                           "Expected: {} Actual {}".format(expected_user_name,
                                                                                           db_user[0]['user_login'])
