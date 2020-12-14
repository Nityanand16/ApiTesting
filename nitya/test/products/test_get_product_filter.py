import pytest
from nitya.src.helper.product_helper import Product_Helper
from datetime import datetime, timedelta
from nitya.src.dao.dao_product import DB_product

@pytest.mark.tcid7
def test_list_product_with_filter_after():

    x_days_from_today = 5
    x = datetime.now().replace(microsecond=0)-timedelta(x_days_from_today)
    x = x.isoformat()
    #import pdb;pdb.set_trace()

    # creatiing a payload

    payload = dict()
    payload['after'] = x
    #import pdb;pdb.set_trace()

    # making a api call

    rs_api = Product_Helper().call_product_by_date(payload)
    rs_list = rs_api[1]

    api_id = []
    for item in rs_list:
        api_id.append(item['id'])
    api_id.sort()
    import pdb ; pdb.set_trace()

    # verify through the db

    db_id = []
    ds_api = DB_product().get_actual_product_by_date(x)
    for item in ds_api:
        db_id.append(item['ID'])
    db_id.sort()
    import pdb;pdb.set_trace()

    assert db_id == api_id,f"Both reponses does not have identical values "

    # compare the ID between from  api response and database
