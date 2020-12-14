import pytest
from nitya.src.utilities.genericUtilities import get_randomString
from nitya.src.helper.product_helper import Product_Helper
from nitya.src.dao.dao_product import DB_product

@pytest.mark.tcid6
def test_create_product():

    # genereate some payload
    payload = dict()
    payload['name'] = get_randomString(10)
    payload['type'] = 'simple'
    payload['regular_price']= "10"

    # make a call
    rs_api = Product_Helper().call_create_product(payload)
    #import pdb ; pdb.set_trace()

    # verify the response is not empty
    assert rs_api[1], f"response is empty and hence the request is failed"
    rs_product_id = rs_api[1]['id']

    # verify the same product in the db
    db_rs = DB_product().get_product(rs_product_id)
    assert db_rs , f"product is not successfully created"
    #import pdb; pdb.set_trace()
    assert rs_api[1]['name'] == db_rs[0]['post_name'],f"Db and response value does not match"