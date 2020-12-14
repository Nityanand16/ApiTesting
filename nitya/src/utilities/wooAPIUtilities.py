from nitya.src.config.hostconfig import API_WOO
from nitya.src.utilities.credentialUtilities import credentialUtility
from woocommerce import API
import os
import logging as logger

class WooAPIUtility(object):

    def __init__(self):

        wc_creds = credentialUtility.getCredentials()

        # self.env = os.environ.get('ENV', 'test')
        # self.base_url = API_WOO[self.env]

        self.wcapi = API(
            url="http://127.0.0.1/wp/wp-json/",
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3"
        )

        #import pdb;pdb.set_trace()

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
          f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
          f"URL: {self.endpoint}, Response Json: {self.rs_json}"

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.post(wc_endpoint, data=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

    def get(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json

    def put(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.put(wc_endpoint, data=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"PUT API response: {self.rs_json}")

        return self.rs_json


if __name__ == '__main__':

    obj = WooAPIUtility()
    rs_api = obj.get('products')
    print(rs_api)
    #import pdb; pdb.set_trace()

    # s_api = obj.get("orders")
    # print(s_api)
