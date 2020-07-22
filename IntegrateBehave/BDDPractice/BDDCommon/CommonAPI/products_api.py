
from BDDCommon.CommonHelpers.wooRequestHelper import WooRequestHelper
import pdb


def list_all_products():
    all_products = []
    page = 1
    max_pages = 1000
    while page < max_pages:
        param = {'per_page': 100, 'page': page}
        response_api = WooRequestHelper().get(wc_endpoint='products', params=param)
        print("Page number: {}".format(page))

        if response_api:
            page += 1
            all_products.extend(response_api)
        else:
            print("No results on page number {}".format(page))
            break

    return all_products


def get_product_by_id(product_id):
    response_api = WooRequestHelper().get(wc_endpoint="products/{}".format(product_id))
    return response_api




