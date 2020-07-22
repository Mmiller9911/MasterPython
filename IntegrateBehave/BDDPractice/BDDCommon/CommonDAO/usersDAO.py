import random

from BDDCommon.CommonHelpers.dbHelpers import DBHelpers


class UsersDAO(object):

    def __init__(self):
        self.dbhelper = DBHelpers()

    def get_user_by_email(self, email):
        sql = "SELECT * FROM local.wp_users where user_email = '{}';".format(email)
        return self.dbhelper.execute_select(sql)

