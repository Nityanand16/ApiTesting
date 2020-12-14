from nitya.src.utilities.requestUtilities import RequestUtility
import pytest


@pytest.mark.product
@pytest.mark.tcid5
def test_get_list_of_products():

    # make a call

    rs_api = RequestUtility().get(endpoint='products',payload=None,headers=None,expected_status_code=200)
    #import pdb;  pdb.set_trace()
    assert rs_api , f"No product in the list"
