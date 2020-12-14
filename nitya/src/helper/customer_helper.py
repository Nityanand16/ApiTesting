from nitya.src.utilities.genericUtilities import random_email_and_password
from nitya.src.utilities.requestUtilities import RequestUtility


class CustomerHelper(object):
    def __init__(self):
        self.request_utility = RequestUtility()

#For creating the new customer
    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            email = random_email_and_password()['email']

        if not password:
            password = random_email_and_password()['password']

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        #import pdb;pdb.set_trace()
        # Make the api call

        rs_pi = self.request_utility.post('customers', payload, expected_status_code=201, headers=None)
        #import pdb;pdb.set_trace()
        return rs_pi

        # request  --- url auth,payload , header