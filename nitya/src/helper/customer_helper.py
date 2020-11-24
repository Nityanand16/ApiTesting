from nitya.src.utilities.generalUtilities import random_email_and_password



class CustomerHelper(object):
    def __init__(self):
        pass

#For creating the new customer
    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            email = random_email_and_password()['email']

        if not password:
            password = random_email_and_password()['password']

        payload = dict()
        payload[email] = email
        payload[password] = password
        payload.update(kwargs)

        return True

