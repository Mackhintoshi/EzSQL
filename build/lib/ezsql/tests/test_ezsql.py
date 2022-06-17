from EzSQL import Query as EzSQL


def run_tests():
    print("Running ezsql test.")
    _ezsql = EzSQL()
    test_set_query_string(_ezsql)
    test_set_query_values(_ezsql)
    test_db_connection(_ezsql)
    test_run_insert()
    test_run_select(_ezsql)
    test_run_update()
    test_run_select_with_json(_ezsql)
    test_run_delete()
    test_run_select_with_list(_ezsql)
    
    

def test_db_connection(_ezsql):
    print("Testing db_connection()")
    try:
        if(_ezsql.test_db_connection()):
            print("Connection successful.")
            return True
        else:
            print("Connection failed.")
            return False
    except Exception as e:
        print("Exception: {0}".format(e))
        return False
    
def test_set_query_string(_ezsql):
    print("Testing set_query_string()")
    try:
        _ezsql.set_query_string("SELECT * FROM data;")
        print("Query string set.")
        return True
    except Exception as e:
        print("Exception: {0}".format(e))
        print("FAILED: Query string not set.")
        return False

def test_set_query_values(_ezsql):
    print("Testing set_query_values()")
    try:
        _ezsql.set_query_values(())
        print("Query values set.")
        return True
    except Exception as e:
        print("Exception: {0}".format(e))
        print("FAILED: Query values not set.")
        return False


def test_run_select(_ezsql):
    print("Testing run_select()")
    try:
        result = _ezsql.run_select()
        print("Successfully retrieved result for select")
        print("Result: {0}".format(result))
        return True
    except Exception as e:
        print("FAILED running select: Exception: {0}".format(e))
        return False
def test_run_select_with_json(_ezsql):
    print("Testing run_select_with_json()")
    try:
        result = _ezsql.run_select_with_json()
        print("Successfully retrieved result for select with JSON")
        print("Result: {0}".format(result))
        return True
    except Exception as e:
        print("FAILED running select with JSON: Exception: {0}".format(e))
        return False

def test_run_select_with_list(_ezsql):
    print("Testing run_select_with_list()")
    try:
        result = _ezsql.run_select_with_list()
        print("Successfully retrieved result for select with list")
        print("Result: {0}".format(result))
        return True
    except Exception as e:
        print("FAILED running select with list: Exception: {0}".format(e))
        return False

def test_run_insert():
    ___ezsql = EzSQL()
    ___ezsql.set_query_string("INSERT INTO data (name, age) VALUES (%s, %s);")
    ___ezsql.set_query_values(("John",30))
    ___ezsql.run_insert()

def test_run_update():
    ___ezsql = EzSQL()
    ___ezsql.set_query_string("UPDATE data SET age = %s WHERE name = %s;")
    ___ezsql.set_query_values((31,"John"))
    ___ezsql.run_update()

def test_run_delete():
    ___ezsql = EzSQL()
    ___ezsql.set_query_string("DELETE FROM data WHERE name = %s;")
    ___ezsql.set_query_values(("John",))
    ___ezsql.run_delete()
