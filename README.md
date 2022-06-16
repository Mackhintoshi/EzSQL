# Welcome to EzSQL!

This python package is based from python mysql connector. It allows you to easily consume MySQL service without doing much of the code. 


# Features

	 - Perform Basic Secure prepared MySQL queries
	 - Perform SELECT queries with your return data format of choice
		 - Get a JSON formatted result
		 - Get a List formatted result
		 - Get results in Tuple
	- Supports DB Credentials from Environment Variables


## Creating a query instance

    #query_string is your prepared statement.
    query_string = "SELECT * FROM table_a WHERE id = %s"
    
    #query_values is a tuple of values
    query_values = (1,)
    
    _ezsql = EzSQL(query_string,query_values)
    
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
    
