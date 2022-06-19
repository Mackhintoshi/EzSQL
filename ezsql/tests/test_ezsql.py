from ezsql.EzSQL import Query as EzSQL

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
    test_run_select_with_list(_ezsql)
    test_run_delete()
    
    

def test_db_connection(_ezsql):
    print("PENDING: Testing db_connection()")
    try:
        if(_ezsql.test_db_connection()):
            print("SUCCESS: Connection successful.")
            return True
        else:
            print("FAILED: Connection failed.")
            return False
    except Exception as e:
        print("FAILED: EXCEPTION: {0}".format(e))
        return False
    
def test_set_query_string(_ezsql):
    print("PENDING: Testing set_query_string()")
    try:
        _ezsql.set_query_string("SELECT * FROM data;")
        print("SUCCESS: Query string set.")
        return True
    except Exception as e:
        print("EXCEPTION: {0}".format(e))
        print("FAILED: Query string not set.")
        return False

def test_set_query_values(_ezsql):
    print("Testing set_query_values()")
    try:
        _ezsql.set_query_values(())
        print("SUCCESS: Query values set.")
        return True
    except Exception as e:
        print("EXCEPTION: {0}".format(e))
        print("FAILED: Query values not set.")
        return False


def test_run_select(_ezsql):
    print("PENDING: Testing run_select()")
    try:
        result = _ezsql.run_select()
        print("SUCCESS: Successfully retrieved result for select")
        print("SUCCESS: Result: {0}".format(result))
        return True
    except Exception as e:
        print("FAILED:  Unable to run select: Exception: {0}".format(e))
        return False
def test_run_select_with_json(_ezsql):
    print("PENDING: Testing run_select_with_json()")
    try:
        result = _ezsql.run_select_with_json()
        print("SUCCESS: Successfully retrieved result for select with JSON")
        print("Result: {0}".format(result))
        return True
    except Exception as e:
        print("FAILED running select with JSON: Exception: {0}".format(e))
        return False

def test_run_select_with_list(_ezsql):
    print("PENDING: Testing run_select_with_list()")
    try:
        result = _ezsql.run_select_with_list()
        print("SUCCESS: Successfully retrieved result for select with list")
        print("SUCCESS: Result: {0}".format(result))
        return True
    except Exception as e:
        print("FAILED: Unable to run select with list: Exception: {0}".format(e))
        return False

def test_run_insert():
    ___ezsql = EzSQL()
    ___ezsql.set_query_string("INSERT INTO data (name, age) VALUES (%s, %s);")
    ___ezsql.set_query_values(("John",30))
    try:
        print("PENDING: Testing run_insert()")
        ___ezsql.run_insert()
        print("SUCCESS: Successfully inserted data.")
        return True
    except Exception as e:
        print("FAILED: Unable to insert data: Exception: {0}".format(e))
        return False

def test_run_update():
    ___ezsql = EzSQL()
    ___ezsql.set_query_string("UPDATE data SET age = %s WHERE name = %s;")
    ___ezsql.set_query_values((31,"John"))
    try:
        print("PENDING: Testing run_update()")
        ___ezsql.run_update()
        print("SUCCESS: Successfully updated data.")
        return True
    except Exception as e:
        print("FAILED: Unable to update data: Exception: {0}".format(e))
        return False

def test_run_delete():
    ___ezsql = EzSQL()
    ___ezsql.set_query_string("DELETE FROM data WHERE name = %s;")
    ___ezsql.set_query_values(("John",))
    try:
        print("PENDING: Testing run_delete()")
        ___ezsql.run_delete()
        print("SUCCESS: Successfully deleted data.")
        return True
    except Exception as e:
        print("FAILED: Unable to delete data: Exception: {0}".format(e))
        return False
