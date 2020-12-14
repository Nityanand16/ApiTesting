import pytest
import logging as logger

from nitya.src.utilities.genericUtilities import random_email_and_password
from nitya.src.helper.customer_helper import CustomerHelper
from nitya.src.dao.dao_customer import DB_Customer
from nitya.src.utilities.requestUtilities import RequestUtility


@pytest.mark.customer
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
    res_api = custobj.create_customer(email, password)
    #import pdb;pdb.set_trace()

    # verifying the email for response and random email passes
    assert email == res_api[1]['email'], f"Random email and actual email does not match"
    ds_rs = DB_Customer().get_user_by_email(email)
    assert ds_rs[0]['ID'] == res_api[1]['id'], f" ID from DB and email doesnot match"
    # https://pypi.org/project/pytest-html/


@pytest.mark.customer
@pytest.mark.tcid3
def test_customer_create_same_email():
    rs_db = DB_Customer().get_random_user()
    db_email = rs_db[0]['user_email']
    payload = dict()
    payload['email'] = db_email
    payload['passowrd'] = 'password'
    rs_api = RequestUtility().post(endpoint='customers', headers=None, expected_status_code=400, payload=payload)
    # import pdb ; pdb.set_trace()
    assert rs_api[1][
               'code'] == 'registration-error-email-exists', f"Expected code message was {'registration-error-email-exists'}"
    message = f"""An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>"""
    assert len(rs_api[1]['message']) == len(message), f"Incorrect message"


@pytest.mark.customer
@pytest.mark.tcid4
def test_existing_cusomter():
    rs_db = DB_Customer().get_random_user()
    db_id = rs_db[0]['ID']
    endpoint = f"customers/{db_id}"
    db_un = rs_db[0]['display_name']
    # import pdb ; pdb.set_trace()
    rs_api = RequestUtility().post(endpoint=endpoint, headers=None, expected_status_code=200, payload=None)
    rs_un = rs_api[1]['username']
    assert db_un == rs_un, f" db user name doesnot match with rs_un"



