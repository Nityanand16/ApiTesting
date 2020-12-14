import requests
import json
import logging as logger
from requests_oauthlib import OAuth1
import os
from nitya.src.config.hostconfig import API_HOST
from nitya.src.utilities.credentialUtilities import credentialUtility

class RequestUtility(object):

    # configuration - local -- qa  --- production
    def __init__(self):
        wc_credentials = credentialUtility().getCredentials()
        self.env = os.environ.get('ENV', "test")
        #import pdb;pdb.set_trace()
        self.baseurl = API_HOST[self.env]
        self.auth = OAuth1(wc_credentials['wc_key'], wc_credentials['wc_secret'])
        #import pdb;pdb.set_trace()

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code,f"Bad status code"

#post the data
    def post(self, endpoint , payload , headers = None ,expected_status_code =200):
        if not headers:
            headers = {"Content-Type":"application/json"}
        self.url = self.baseurl + endpoint

        rs_api = requests.post(url = self.url,data = json.dumps(payload),headers = headers,auth = self.auth)
        #import pdb;pdb.set_trace()
        self.status_code = rs_api.status_code
        #import pdb;pdb.set_trace()
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        #import pdb;pdb.set_trace()
        self.rs_json = rs_api.json()

        logger.debug(f"The post request response is {self.rs_json}")
        return [self.status_code ,self.rs_json]


#get or retrieve the data
    def get(self,endpoint ,payload = None,headers = None,expected_status_code =200):
        if not headers:
            headers = {"Content-Type":"application/json"}

        self.url = self.baseurl + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        self.rs_json = rs_api.json()
        logger.debug(f"The get request response is {self.rs_json}")

        return [self.status_code, self.rs_json]


    # def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
    #     if not headers:
    #         headers = {"Content-Type": "application/json"}
    #
    #     self.url = self.baseurl + endpoint
    #     rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
    #     self.status_code = rs_api.status_code
    #     self.expected_status_code = expected_status_code
    #     self.assert_status_code()
    #     self.rs_json = rs_api.json()
    #     logger.debug(f"The get request response is {self.rs_json}")
    #
    #     return [self.status_code, self.rs_json]
    #
    # def delete(self, endpoint, payload=None, expected_status_code=200):
    #     self.url = self.baseurl + endpoint
    #     rs_api = requests.delete(url=self.url, data=json.dumps(payload),auth=self.auth)
    #     self.status_code = rs_api.status_code
    #     self.expected_status_code = expected_status_code
    #     self.assert_status_code()
    #     self.rs_json = rs_api.json()
    #     logger.debug(f"The get request response is {self.rs_json}")