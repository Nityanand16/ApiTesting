import pytest
import logging as logger

from nitya.src.utilities.generalUtilities import random_email_and_password
from nitya.src.utilities.generalUtilities import random_email_and_password
from nitya.src.helper.customer_helper import CustomerHelper
from nitya.src.helper.customer_helper import CustomerHelper
@pytest.mark.tcid1
def test_create_customer():
    logger.info("TEST:create a new customer with email and password only")
    randomInfo = random_email_and_password()

    email = randomInfo['email']
    password = randomInfo['password']
    logger.debug(randomInfo)

    # create a payload
    # payload = {'email': email, 'password': password}
    # print(payload)
    # pass

    #calling the email and password
    custobj = CustomerHelper()
    cust = custobj.create_customer(email, password)
    print(cust)