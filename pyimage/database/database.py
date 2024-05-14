from tinydb import TinyDB, Query


class Database:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)

    def get_table(self, table_name):
        return self.db.table(table_name)

    @staticmethod
    def get_query():
        return Query()
