class QueryResult:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.row_count = len(rows)
        
    def getColumns(self):
        return self.columns

    def getRows(self):
        return self.rows

    def getRowCount(self):
        return self.row_count