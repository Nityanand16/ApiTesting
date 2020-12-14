import json
import os
from nitya.src.utilities.requestUtilities import RequestUtility

class OrderHelper(object):

    def __init__(self):

       # To find the path of current working directory
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))


    def create_order(self,addtion_arg=None):
        payload_path =os.path.join(self.cur_file_dir,'..','data','create_order.json')

        with open(payload_path) as f:
            payload = json.load(f)
            payload.update(addtion_arg)
            rs_api =RequestUtility().post(endpoint='orders',payload = payload,headers=None,expected_status_code=201)
            return rs_api