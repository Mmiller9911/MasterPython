import random

from helpers.dbHelpers import DBHelpers
import logging as logger


class CouponsDAO(object):

    def __init__(self):
        self.dbhelper = DBHelpers()

    def get_coupon_by_id(self, coupon_id):
        sql = "SELECT * FROM local.wp_posts WHERE ID = {} AND post_type = 'shop_coupon';".format(coupon_id)
        return self.dbhelper.execute_select(sql)

    def get_coupon_metadata_by_id(self, coupon_id):
        sql = f"SELECT * FROM local.wp_postmeta WHERE post_id = {coupon_id};"
        response_sql = self.dbhelper.execute_select(sql)

        logger.debug(f"")
        logger.debug(f"SQL Result: \n {response_sql}")
        logger.debug(f"")

        coupon_meta = dict()
        for i in response_sql:
            coupon_meta[i['meta_key']] = i['meta_value']

        return coupon_meta


