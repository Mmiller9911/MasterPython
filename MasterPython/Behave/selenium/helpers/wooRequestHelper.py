from woocommerce import API
from helpers.credentialsHelper import CredentialsHelper
import pdb
import pprint
import logging as logger

class WooRequestHelper(object):

    def __init__(self):

        creds_helper = CredentialsHelper()
        wc_creds = creds_helper.get_wc_api_keys()

        self.response = None   # if using the pdb debugger the response can be viewed with "pp self.response.json()"
        self.endpoint = None
        self.expected_status_code = None
        self.params = None
        self.wcapi = API(
            url="http://mystore.local",
            consumer_key=wc_creds["wc_key"],
            consumer_secret=wc_creds["wc_secret"],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.response.status_code == self.expected_status_code, "Bad Status code. Endpoint: {}, Params: {}. " \
                                                                 "Actual status code: {}, Expected status code: {}," \
                                                                       "Response Body: {}".format(
            self.endpoint, self.params, self.response.status_code, self.expected_status_code, self.response.json())

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        self.response = self.wcapi.get(wc_endpoint, params=params)
        self.endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.response.json()

    def post(self, wc_endpoint, params=None, expected_status_code=201):
        logger.info("111")
        logger.info(f"Params: {params}")
        logger.info("111")
        self.response = self.wcapi.post(wc_endpoint, data=params)
        self.endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.response.json()

    def delete(self):
        pass

    def put(self):
        pass


if __name__ == "__main__":  # convert this file into a script which can run on its own, dont do this if class is imported
    myObj = WooRequestHelper()
    get_response = myObj.get("products")


    pprint.pprint(get_response)

    payload = {
        "email": "dumm1y@emails.com",
        "password": "123abv"}

    post_response = myObj.post("customers", params=payload, expected_status_code=201)
    pprint.pprint(post_response) #returns 400 as customer already exists

