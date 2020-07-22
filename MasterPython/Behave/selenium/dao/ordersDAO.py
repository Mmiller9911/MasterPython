import random

from helpers.dbHelpers import DBHelpers


class OrdersDAO(object):

    def __init__(self):
        self.dbhelper = DBHelpers()

    def get_order_by_id(self, order_id):
        sql = "SELECT * FROM local.wp_posts WHERE ID = {};".format(order_id)
        return self.dbhelper.execute_select(sql)

