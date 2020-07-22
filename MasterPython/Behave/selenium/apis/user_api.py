from helpers.wooRequestHelper import WooRequestHelper


def create_user(data):
    return WooRequestHelper().post(wc_endpoint='customers', params=data)