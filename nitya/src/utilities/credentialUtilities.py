import os


class credentialUtility():

    def __init__(self):
        pass

    @staticmethod
    def getCredentials():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key and not wc_secret:
            raise Exception('Please set the api keys via environmental variables')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_Credentials():

        db_user = os.environ.get('DB_USER')
        db_pass = os.environ.get('DB_PASSWORD')

        if not db_user and not db_pass:
            raise Exception('Please set the api keys via environmental variables')
        else:
            return {'db_user': db_user, 'db_pass': db_pass}