from nitya.src.utilities.requestUtilities import RequestUtility
import logging as logger


class Product_Helper():

    def __init__(self):
        self.product_utility = RequestUtility()

    def get_product_by_id(self,id):
        api_rs = self.product_utility.get(f"products/{id}")
        return api_rs

    def call_create_product(self,payload = None):
        rs_api = self.product_utility.post(endpoint='products',payload = payload,expected_status_code=201)
        return rs_api


    def call_product_by_date(self, payload=None):
        return self.product_utility.get('products', payload=payload)




    # def call_product_by_date(self, payload=None):
    #
    #     max_pages = 1000
    #     all_products = []
    #     for i in range(1, max_pages + 1):
    #         logger.debug(f"List products page number: {i}")
    #
    #         if not payload:
    #             payload = {}
    #
    #         if not 'per_page' in payload.keys():
    #             payload['per_page'] = 100
    #
    #         # add the current page number to the call
    #         payload['page'] = i
    #         rs_api = self.product_utility.get('products', payload=payload)
    #
    #         # if there is not response then stop the loop b/c there are no more products
    #         if not rs_api:
    #             break
    #         else:
    #             all_products.extend(rs_api)
    #     else:
    #         raise Exception(f"Unable to find all products after {max_pages} pages.")
    #
    #     return all_products