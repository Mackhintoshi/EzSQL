from ezsql.utils import Exceptions as exceptions
from ezsql.utils import SQLConnection as sql_connection
from ezsql.utils import QueryResult as QueryResult

import mysql.connector as mysql

class Query:
    #STATIC VARIABLES FOR CONFIGURATIONS
    MAXIMUM_ROWS_TO_RETURN = 100000
    MAXIMUM_SQL_COMMAND_RETRIES = 1

    def __init__(self,query_string = None,query_values = None) -> None:
        try:
            self.query_string = query_string
            self.query_values = query_values
        except Exception as e:
            raise e

    def test_db_connection(self):   
        _connection = sql_connection.SQLConnection()
        return _connection.test_db_connection()
            
            
    def set_query_string(self, query: str) -> None:
        if(type(query) is not str):
            raise exceptions.StringRequiredException(query)
        else:
            self.query_string = query
    
    def set_query_values(self, values: tuple) -> None:
        if(type(values) is not tuple):
            raise exceptions.TupleRequiredException(values)
        else:
            self.query_values = values

    def are_query_and_values_set(self):
        if(self.query_string is None):
            raise exceptions.QueryStringRequiredException(self.query_string)
        if(self.query_values is None):
            raise exceptions.QueryValuesRequiredException(self.query_values)
        return True

    def run_select(self):
        try:
            query_result = self.__execute_query()
            return query_result.getRows()
        except Exception as e:
            raise e

    def run_select_with_json(self):
        try:
            query_result = self.__execute_query()
            return self.__parse_result_to_json(query_result)
        except Exception as e:
            raise e

    def run_select_with_list(self):
        try:
            query_result = self.__execute_query()
            return self.__parse_result_to_list(query_result)
        except Exception as e:
            raise e

    def run_insert(self):
        return self.__execute_with_commit()

    def run_update(self):
        return self.__execute_with_commit()

    def run_delete(self):
        return self.__execute_with_commit()

        

    def __execute_query(self):
        try:
            if(self.are_query_and_values_set()):
                _connection = sql_connection.SQLConnection()
                _db_query = sql_connection.DbQuery(self.query_string,self.query_values)
                query_result = _connection.execute(_db_query) #returns QueryResult Object
                return query_result
        except Exception as e:
            raise exceptions.DataBaseExecutionException(e)

    def __execute_with_commit(self):
        try:
            if(self.are_query_and_values_set()):
                _connection = sql_connection.SQLConnection()
                _db_query = sql_connection.DbQuery(self.query_string,self.query_values)
                return _connection.execute_with_commit(_db_query)
        except Exception as e:
            raise e

    def __parse_result_to_json(self,query_result: QueryResult.QueryResult):
        try:
            _json_result = []
            for row in query_result.getRows():
                _json_result.append(dict(zip(query_result.getColumns(),row)))
            return _json_result
        except Exception as e:
            raise exceptions.DataBaseExecutionException(e)

    def __parse_result_to_list(self,query_result: QueryResult.QueryResult):
        try:
            _list_result = []
            for row in query_result.getRows():
                _list_result.append(list(row))
            return _list_result
        except Exception as e:
            raise exceptions.DataBaseExecutionException(e)