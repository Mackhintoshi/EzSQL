from ezsql.lib import QueryResult as QueryResult
from ezsql.lib import Exceptions as exceptions
import ezsql.config as config
import mysql.connector as mysql

class SQLConnection:
    def __init__(self):
        self.db_config = config.DBConfig()
        self.host = self.db_config.get_dbhost()
        self.user = self.db_config.get_dbuser()
        self.password = self.db_config.get_dbpass()
        self.db = self.db_config.get_dbname()
        self.connection = None
        self.cursor = None

    def test_db_connection(self): 
        try:
            _con = mysql.connect(
                            host = self.host,
                            user = self.user,
                            passwd = self.password,
                            database = self.db
                        )
            if(_con.is_connected()):
                _con.close()
                return True
            else:
                return False     
        except Exception as e:
            raise exceptions.DatabaseConnectionError(e)

    def execute(self,db_query):
        if(self.connection is None):
            self.create_connection()
        if(isinstance(db_query,DbQuery)):
            try:
                self.cursor.execute(db_query.getQueryString(),db_query.getQueryValues())
                query_result = QueryResult.QueryResult(self.cursor.column_names,self.cursor.fetchall())
                self.connection.close()
                return query_result
            except Exception as e:
                raise exceptions.DataBaseExecutionException(e)
        else:
            raise exceptions.DbQueryRequiredException(db_query)

    def execute_with_commit(self,db_query):
        if(self.connection is None):
            self.create_connection()
        if(isinstance(db_query,DbQuery)):
            try:
                self.cursor.execute(db_query.getQueryString(),db_query.getQueryValues())
                self.connection.commit()
                self.connection.close()
                return True
            except Exception as e:
                raise e
        else:
            raise exceptions.DbQueryRequiredException(db_query)

    def create_connection(self):
        try:
            _con = mysql.connect(
                            host = self.host,
                            user = self.user,
                            passwd = self.password,
                            database = self.db
                            )
            self.connection = _con
            self.cursor = _con.cursor(prepared=True)
            return _con
        except Exception as e:
            raise exceptions.DatabaseConnectionError(e)

    def close_connection(self):
        self.connection.close()


class DbQuery:
    def __init__(self, query_string: str, query_values: tuple) -> None:
        self.query_string = query_string
        self.query_values = query_values
        
    def getQueryString(self):
        return self.query_string

    def getQueryValues(self):
        return self.query_values