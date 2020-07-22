import random

from helpers.dbHelpers import DBHelpers


class UsersDAO(object):

    def __init__(self):
        self.dbhelper = DBHelpers()

    def get_user_by_email(self, email):
        sql = "SELECT * FROM local.wp_users where user_email = '{}';".format(email)
        return self.dbhelper.execute_select(sql)

    def get_number_of_users(self):
        sql = "SELECT COUNT(*) FROM local.wp_users;"
        return self.dbhelper.execute_select(sql)

