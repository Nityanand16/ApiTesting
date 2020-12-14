import pytest
from nitya.src.dao.dao_product import DB_product
from nitya.src.helper.product_helper import Product_Helper

@pytest.mark.product
@pytest.mark.tcid5
def test_get_product_by_id():

    # Pcreate the helper call for the dao
    # Creating the object of db_product
    db_product = DB_product()
    api_product = Product_Helper()

    # get the record form the db
    db_rs = db_product.get_product_by_id(1)
    #import pdb ; pdb.set_trace()

    # make the api call
    api_rs = api_product.get_product_by_id(db_rs[0]['ID'])
    #import pdb;pdb.set_trace()
    # validating the name of the product from db with api reponse on id
    assert api_rs[1]['name'] == db_rs[0]['post_title'],f"{api_rs[0]['name']} does not match with {db_rs[0]['post_title']}"
