import os

class DBConfig:
    def __init__(self):
        self.dbuser = os.environ['EZSQL_DBUSER']
        self.dbpass = os.environ['EZSQL_DBPASS']
        self.dbhost = os.environ['EZSQL_DBHOST']
        self.dbname = os.environ['EZSQL_DBNAME']

    
    def get_dbuser(self):
        return self.dbuser

    def get_dbpass(self):
        return self.dbpass

    def get_dbhost(self):
        return self.dbhost

    def get_dbname(self):
        return self.dbname