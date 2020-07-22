from behave import step
from helpers.utilitiesHelper import UtilitiesHelper
from helpers.fileHelper import FileHelper
from dao.usersDAO import UsersDAO


@step('I create "{number}" new users using a test data creator')
def step_impl(context, number):
    context.users_list = []
    context.db_users = UsersDAO().get_number_of_users() ## save the current number of users before they are added in UI
    users = UtilitiesHelper()
    users.clear_all_users()
    users.generate_group_of_test_users(int(number))  #create new users and add them to users object all_users
    context.users_list = users.return_all_users()
    assert len(context.users_list) == int(number), "Five users should be created"


@step('I output the data into a CSV file')
def step_impl(context):
    data = context.users_list
    files = FileHelper()
    files.make_a_file(data)


@step('all the data is output correctly')
def step_impl(context):
    files = FileHelper()
    user1 = []
    result = files.read_a_file_and_return('users.csv')
    for i in range(0, 9):
        user1.append(result[i])
    print(user1)
