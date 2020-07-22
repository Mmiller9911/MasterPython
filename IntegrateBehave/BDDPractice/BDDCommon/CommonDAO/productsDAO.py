import random

from BDDCommon.CommonHelpers.dbHelpers import DBHelpers


class ProductsDAO(object):

    def __init__(self):
        self.dbhelper = DBHelpers()

    def get_all_products_from_db(self):
        sql = "select * from wp_posts where post_type = 'product';"
        response_sql = self.dbhelper.execute_select(sql)
        return response_sql

    def get_random_products_from_db(self, qty):
        sql = "select * from local.wp_posts WHERE post_type = 'product' order by id DESC LIMIT 5000;"
        response_sql = self.dbhelper.execute_select(sql)

        return random.sample(response_sql, int(qty))


