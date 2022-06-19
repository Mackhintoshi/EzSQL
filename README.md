# Welcome to EzSQL!

This python package is based from python mysql connector. It allows you to easily consume MySQL service without doing much of the code. 


# Features

	 - Perform Basic Secure prepared MySQL queries
	 - Perform SELECT queries with your return data format of choice
		 - Get a JSON formatted result
		 - Get a List formatted result
		 - Get results in Tuple
	- Supports DB Credentials from Environment Variables
    
## Installation

    pip install python-ezsql

## Setting up your credentials

To set your credentials, you can set the following in your environment variable. You may also put it in your .env file 

    EZSQL_DBUSER=your_user
    EZSQL_DBPASS=your_pass
    EZSQL_DBHOST=your_host
    EZSQL_DBNAME=your_db
    

## Creating a query instance

    from ezsql.EzSQL import Query

    #query_string is your prepared statement.
    query_string = "SELECT * FROM table_a WHERE id = %s"
    
    #query_values is a tuple of values
    query_values = (1,)
    
    _ezsql = Query(query_string,query_values)
    
## SELECT That returns tuple

    
    _result = _ezsql.run_select()
    print(_result)

outputs

    [(1, 'foo', 18)]
    
        
## SELECT That returns a list

      
    _result = _ezsql.run_select_with_list()
    print(_result)

outputs

    [1, 'foo', 18]

## SELECT That returns a JSON

      
    _result = _ezsql.run_select_with_json()
    print(_result)

outputs

    [{'id': 1, 'name': 'foo', 'age': 18}]

## INSERT

      
    _result = _ezsql.run_insert()
    print(_result)

outputs

    True
    
## UPDATE

      
    _result = _ezsql.run_update()
    print(_result)

outputs

    True

## DELETE

      
    _result = _ezsql.run_delete()
    print(_result)

outputs

    True
    

## Running a test
To run a test, create a table like this.

    CREATE TABLE `data` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(45) DEFAULT NULL,
    `age` int DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

When the table is ready, you can use the run_test() function

    from ezsql.tests import test_ezsql
    test_ezsql.run_tests()

Test Output

    Running ezsql test.
    PENDING: Testing set_query_string()
    SUCCESS: Query string set.
    Testing set_query_values()
    SUCCESS: Query values set.
    PENDING: Testing db_connection()
    SUCCESS: Connection successful.
    PENDING: Testing run_insert()
    SUCCESS: Successfully inserted data.
    PENDING: Testing run_select()
    SUCCESS: Successfully retrieved result for select
    SUCCESS: Result: [(47, 'John', 30)]
    PENDING: Testing run_update()
    SUCCESS: Successfully updated data.
    PENDING: Testing run_select_with_json()
    SUCCESS: Successfully retrieved result for select with JSON
    Result: [{'id': 47, 'name': 'John', 'age': 31}]
    PENDING: Testing run_select_with_list()
    SUCCESS: Successfully retrieved result for select with list
    SUCCESS: Result: [[47, 'John', 31]]
    PENDING: Testing run_delete()
    SUCCESS: Successfully deleted data.