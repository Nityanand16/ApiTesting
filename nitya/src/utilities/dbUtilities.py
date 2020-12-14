import pymysql
from nitya.src.utilities.credentialUtilities import credentialUtility

class DButilit(object):

    def __init__(self):
        cred_helper = credentialUtility()
        self.db_credential =cred_helper. get_db_Credentials()
        self.host = 'localhost'
        self.port = 3306
        #self.sql = "SELECT * FROM wp759.wpv1_users  where user_email = 'testeruser_rpwczxtxxa@minskole.in';"

    def create_connection(self):
       connection = pymysql.connect(host = self.host , user = self.db_credential['db_user'],
                        password =self.db_credential['db_pass'],port =self.port)

       return connection

    def execute_select(self,sql):
        conn = self.create_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql) # rows return
        db_rs =cursor.fetchall()

        return db_rs