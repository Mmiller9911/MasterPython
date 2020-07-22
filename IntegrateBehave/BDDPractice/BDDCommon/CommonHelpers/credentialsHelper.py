
import os


class CredentialsHelper(object):

    def __init__(self):
        pass

    def get_wc_api_keys(self):
        wc_key = os.environ.get("WC_KEY")
        wc_secret = os.environ.get("WC_SECRET")

        if not wc_key or not wc_secret:
            raise Exception("The api credentials 'WC_KEY' and 'WC_SECRET' must be set as environment variables")

        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    def get_db_credentials(self):
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")

        if not db_user or not db_password:
            raise Exception("The api credentials 'DB_USER' and 'DB_PASSWORD' must be set as environment variables")

        else:
            return {'db_user': db_user, 'db_password': db_password}


if __name__ == "__main__":  # convert this file into a script which can run on its own, dont do this if class is imported
    myObj = CredentialsHelper()
    print(myObj.get_wc_api_keys())
