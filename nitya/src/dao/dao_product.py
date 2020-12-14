from nitya.src.utilities.dbUtilities import DButilit
import random


class DB_product(object):

    def __init__(self):
        self.productDB = DButilit()

    def get_product_by_id(self,qty):
        sql = f'SELECT * FROM wp724.wpv1_posts where post_type = "product" limit 10;'
        db_rs = self.productDB.execute_select(sql)
        db_rs = random.sample(db_rs,int(qty))
        return db_rs

    def get_product(self,id):
        sql = f"SELECT * FROM wp724.wpv1_posts where id = '{id}'";
        db_rs = self.productDB.execute_select(sql)
        return db_rs

    def get_actual_product_by_date(self,date):
        sql = f" SELECT * FROM wp724.wpv1_posts where post_date > '{date}';";
        db_rs = self.productDB.execute_select(sql)
        return db_rs