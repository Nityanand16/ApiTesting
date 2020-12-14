from nitya.src.utilities.dbUtilities import DButilit



class DB_order(object):

    def __init__(self):
        self.productDB = DButilit()

    def get_product_by_order_Id(self,orderId):
        sql = f'SELECT * FROM wp724.wpv1_woocommerce_order_items where order_id = "{orderId}" and order_item_type ="line_item";'
        db_rs = self.productDB.execute_select(sql)
        # order_item_id
        return db_rs

    def get_product_id(self,order_meta_id):
        sql = f"SELECT * FROM wp724.wpv1_woocommerce_order_itemmeta where order_item_id ='{order_meta_id}' and meta_key ='_product_id';"
        db_rs = self.productDB.execute_select(sql)
        return db_rs
