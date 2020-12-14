import pytest
from nitya.src.utilities.requestUtilities import RequestUtility


@pytest.mark.customer
@pytest.mark.tcid2
def test_get_customers():

    # make a call to get all customers
    r = RequestUtility()
    rs_api =  r.get(endpoint='customers',payload=None,headers=None,expected_status_code=200)
    # verify whether the responce is not empty
    assert rs_api ,f"No customer is present"
    #import pdb ; pdb.set_trace()
    # validate response is not empty