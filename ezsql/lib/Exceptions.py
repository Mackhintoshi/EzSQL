class EzSQLInvalidArgument(Exception):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return "Invalid Arguments. EzSQL requires query_string(str) and query_values(tuple) as an argument".format(self.message)

class DatabaseConnectionError(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message

    def __str__(self):
        return "Connection to database has failed: {0}".format(self.message)

class DataBaseExecutionException(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message
    def __str__(self):
        return "Executing query has failed: {0}".format(self.message)

class StringRequiredException(Exception):
    def __init__(self, input, *args):
        super().__init__(args)
        self.input = input

    def __str__(self):
        return "The input is supposed to be STRING but got {0} which is a {1}".format(self.input,type(self.input))

    
class TupleRequiredException(Exception):
    def __init__(self, input, *args):
        super().__init__(args)
        self.input = input

    def __str__(self):
        return "The input is supposed to be TUPLE but got {0} which is a {1}".format(self.input,type(self.input))

class DatabaseConnectionError(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message

    def __str__(self):
        return "Connection to database has failed: {0}".format(self.message)

class DataBaseExecutionException(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message
    def __str__(self):
        return "Executing query has failed: {0}".format(self.message)


class DatabaseInsertException(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message
    def __str__(self):
        return "Executing INSERT Query has failed: {0}".format(self.message)

class DatabaseUpdateException(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message
    def __str__(self):
        return "Executing UPDATE Query has failed: {0}".format(self.message)

class DatabaseDeleteException(Exception):
    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message
    def __str__(self):
        return "Executing DELETE Query has failed: {0}".format(self.message)


class QueryStringRequiredException(Exception):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return "Unable to proceed with query: Query String is not defined"

class QueryValuesRequiredException(Exception):
    def __init__(self, *args):
        super().__init__(args)
    def __str__(self):
        return "Unable to proceed with query: Query Values is not defined"

class DbQueryRequiredException(Exception):
    def __init__(self,input, *args):
        super().__init__(args)
        self.input = input
    def __str__(self):
        return "Unable to proceed with query: a DbQuery Object was expected as an argument. Instead got {0}".format(type(self.input))