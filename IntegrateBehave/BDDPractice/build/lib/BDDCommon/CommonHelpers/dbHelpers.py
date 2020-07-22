
from BDDCommon.CommonHelpers.credentialsHelper import CredentialsHelper
import pymysql


class DBHelpers(object):

    def __init__(self):
        creds_helper = CredentialsHelper()
        creds = creds_helper.get_db_credentials()
        self.host = 'localhost'
        self.db_user = creds['db_user']
        self.db_password = creds['db_password']
        self.port = 10005
        self.connection = None
        self.database = 'local'

    def create_connection(self):
        self.connection = pymysql.connect(database=self.database, host=self.host, user=self.db_user, password=self.db_password, port=self.port)

    def execute_select(self, sql):
        try:
            self.create_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception("failed running sql query {}. Error {}".format(sql, str(e)))
        finally:
            self.connection.close()

        return rs_dict



    def execute_sql(self):
        pass

