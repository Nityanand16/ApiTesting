import pytest
import logging as logger
from nitya.src.utilities.requestUtilities import RequestUtility
import os
import json
from nitya.src.dao.dao_product import DB_product
from nitya.src.helper.order_helper import OrderHelper
from nitya.src.dao.dao_order import DB_order

@pytest.mark.tcid8

def test_get_order_list():
    customer_id = 0
    db_rs = DB_product().get_product_by_id(1)
    product_id =db_rs[0]['ID']
    #import pdb; pdb.set_trace()
    info = {"line_items":[
            {
                "product_id":product_id,
                "quantity": 1
            }
    ],
    'customer_id':customer_id,

 }

    rs_api = OrderHelper().create_order(info)
    assert rs_api,f"order not created"
    # product id and db product id
    rs_api_order = rs_api[1]['id']
    import pdb;pdb.set_trace()

    # Getting product id from db

    ds_rp = DB_order().get_product_by_order_Id(rs_api_order)
    db_order_item_id = ds_rp[0]['order_item_id']
    db_pro = DB_order().get_product_id(db_order_item_id)
    db_product_id_order =  db_pro[0]['meta_value']
    assert str(db_product_id_order) == str(product_id),f"payload product_id does not match with db_product_id"

    # guest user or cutomer_id
    # customer_id

    # payload -- create order

    # reposnse - customer_id

    # db-- order ---
